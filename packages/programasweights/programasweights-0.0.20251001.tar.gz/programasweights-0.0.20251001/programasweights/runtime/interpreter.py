from __future__ import annotations

import os
import threading
from dataclasses import dataclass
from typing import Callable, Dict, List, Optional, Tuple, Union

import torch
import transformers as _tf

from programasweights.artifacts import load_artifact, ProgramArtifact


# Global lock to guard generate() calls for simple thread-safety
_GLOBAL_GENERATE_LOCK = threading.RLock()


@dataclass
class RegisteredProgram:
    name: str
    path: str
    artifact: ProgramArtifact


def _ensure_list(x: Union[str, List[str]]) -> Tuple[bool, List[str]]:
    if isinstance(x, list):
        return True, x
    if isinstance(x, str):
        return False, [x]
    raise TypeError("Input must be str or List[str]")


class _Interpreter:
    def __init__(self, model_name: str, device: torch.device) -> None:
        self.model_name = model_name
        self.device = device
        self.tokenizer = _tf.AutoTokenizer.from_pretrained(model_name)

        self.model = _tf.AutoModelForCausalLM.from_pretrained(model_name)
        self.model.to(self.device)
        self._programs: Dict[str, RegisteredProgram] = {}

    def register_program(self, path: str, name: Optional[str]) -> RegisteredProgram:
        program_name = name if name is not None else os.path.basename(path)
        artifact = load_artifact(path)
        
        if artifact.kind != "prefix_kv":
            raise ValueError(f"Program artifact at {path} must be 'prefix_kv', got '{artifact.kind}'")

        program = RegisteredProgram(name=program_name, path=path, artifact=artifact)
        self._programs[program_name] = program
        return program

    def get_callable(self, program_name: str, max_new_tokens: int) -> Callable[[Union[str, List[str]]], Union[str, List[str]]]:
        if program_name not in self._programs:
            raise ValueError(f"Program '{program_name}' is not registered")

        def _call(x: Union[str, List[str]]) -> Union[str, List[str]]:
            was_list, inputs = _ensure_list(x)
            outputs = self._generate(program_name, inputs, max_new_tokens=max_new_tokens)
            return outputs if was_list else outputs[0]

        return _call

    def _maybe_load_kv_prefix(self, program: RegisteredProgram) -> Optional[List[Tuple[torch.Tensor, torch.Tensor]]]:
        if program.artifact.kind != "prefix_kv":
            return None
        mapper_path = os.path.join(program.artifact.path, "kv_prefix.pt")
        if not os.path.isfile(mapper_path):
            return None
        pkg = torch.load(mapper_path, map_location="cpu")
        kv: List[Tuple[torch.Tensor, torch.Tensor]] = []
        for item in pkg.get("layers", []):
            k = item[0].to(self.device)
            v = item[1].to(self.device)
            kv.append((k, v))
        return kv if kv else None

    def _generate(self, program_name: str, texts: List[str], *, max_new_tokens: int) -> List[str]:
        program = self._programs[program_name]

        # All programs must be KV artifacts now
        tokenized = self.tokenizer(
            texts,
            return_tensors="pt",
            padding=True,
            truncation=False,
        )
        try:
            tokenized = {k: v.to(self.device) if hasattr(v, "to") else v for k, v in tokenized.items()}
        except Exception:
            pass

        kv_prefix = self._maybe_load_kv_prefix(program)
        if kv_prefix is None:
            raise ValueError(f"Program {program_name} has no valid KV prefix")
            
        attention_mask = tokenized.get("attention_mask")
        if attention_mask is not None:
            bsz = attention_mask.size(0)
            expanded_kv: List[Tuple[torch.Tensor, torch.Tensor]] = []
            for (k, v) in kv_prefix:
                if k.dim() == 3:
                    k = k.unsqueeze(0).expand(bsz, -1, -1, -1).contiguous()
                    v = v.unsqueeze(0).expand(bsz, -1, -1, -1).contiguous()
                expanded_kv.append((k, v))
            kv_prefix = expanded_kv
            steps = kv_prefix[0][0].size(2)
            prefix_mask = torch.ones((bsz, steps), dtype=attention_mask.dtype, device=attention_mask.device)
            attention_mask = torch.cat([prefix_mask, attention_mask], dim=1)

        if attention_mask is not None:
            tokenized["attention_mask"] = attention_mask

        cache_obj = kv_prefix
        past_len = 0
        from transformers.cache_utils import DynamicCache  # type: ignore
        if cache_obj is not None:
            cache_obj = DynamicCache.from_legacy_cache(tuple(cache_obj))
            past_len = cache_obj.get_seq_length()
        # Provide position_ids and cache_position offset by past length for causal models
        bsz = tokenized["input_ids"].size(0)
        seq_len = tokenized["input_ids"].size(1)
        padding = tokenized['input_ids'].new_zeros(bsz, past_len).long()
        tokenized['input_ids'] = torch.cat((padding, tokenized['input_ids']), dim=-1)

        with _GLOBAL_GENERATE_LOCK:
            generated = self.model.generate(
                input_ids=tokenized["input_ids"],
                max_new_tokens=max_new_tokens,
                attention_mask=tokenized["attention_mask"],
                num_beams=1,
                past_key_values=cache_obj,
                use_cache=True,
            )

        input_len = tokenized["input_ids"].shape[1]
        outs = generated[:, input_len:]
        decoded: List[str] = [
            self.tokenizer.decode(seq, skip_special_tokens=True) for seq in outs
        ]
        return decoded


_INTERPRETER_SINGLETON: Optional[_Interpreter] = None


def _select_device() -> torch.device:
    override = os.environ.get("PROGRAMASWEIGHTS_DEVICE", "").strip().lower()
    if override == "cpu":
        return torch.device("cpu")
    if override == "cuda":
        if torch.cuda.is_available():
            return torch.device("cuda")
        return torch.device("cpu")
    if torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")


def _get_interpreter(model_name: str) -> _Interpreter:
    global _INTERPRETER_SINGLETON
    if _INTERPRETER_SINGLETON is None:
        device = _select_device()
        _INTERPRETER_SINGLETON = _Interpreter(model_name=model_name, device=device)
    return _INTERPRETER_SINGLETON


def function(
    path: str,
    *,
    name: Optional[str] = None,
    interpreter_name: str = "google/flan-t5-small",
    max_new_tokens: int = 128,
) -> Callable[[Union[str, List[str]]], Union[str, List[str]]]:
    """
    Register a program artifact and return a callable that runs it.
    """
    interp = _get_interpreter(model_name=interpreter_name)
    program = interp.register_program(path=path, name=name)
    return interp.get_callable(program_name=program.name, max_new_tokens=max_new_tokens) 
