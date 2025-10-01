from __future__ import annotations

import os
import math
import inspect
import json
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

import torch
import torch.nn as nn
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
)

from training.datasets.jsonl_text_pairs import load_tuples


@dataclass
class PrefixTuningConfig:
    # Base models
    compiler_model_name: str = "Qwen/Qwen3-0.6B"
    interpreter_model_name: str = "Qwen/Qwen2.5-Coder-0.5B-Instruct"

    # Data
    train_jsonl: str = "data/samples_train.jsonl"
    val_jsonl: Optional[str] = "data/samples_val.jsonl"

    # Optimization
    learning_rate: float = 5e-5
    batch_size: int = 16
    gradient_accumulation_steps: int = 2
    num_epochs: int = 1
    max_spec_length: int = 256
    max_input_length: int = 256
    max_output_length: int = 256
    warmup_steps: int = 0
    max_grad_norm: float = 1.0

    # Prefix KV settings
    prefix_steps: int = 5

    # Debugging
    debug: bool = False
    debug_size: int = 5
    debug_nan: bool = False
    debug_dump_kv: bool = False

    # Model control
    freeze_base_models: bool = False
    disable_dropout: bool = False

    # IO
    output_dir: str = "outputs/prefix_kv"
    seed: int = 42


class ProgramPrefixMapper(nn.Module):
    """
    Maps teacher hidden states (per selected layer and time step) to student's
    per-layer K/V tensors compatible with `past_key_values`.
    Outputs per layer K,V: [batch, num_kv_heads, prefix_steps, head_dim].
    """

    def __init__(
        self,
        teacher_hidden_size: int,
        student_num_layers: int,
        student_num_kv_heads: int,
        student_head_dim: int,
        prefix_steps: int,
    ) -> None:
        super().__init__()
        self.student_num_layers = student_num_layers
        self.student_num_kv_heads = student_num_kv_heads
        self.student_head_dim = student_head_dim
        self.prefix_steps = prefix_steps

        out_dim = student_num_kv_heads * student_head_dim
        self.proj_k = nn.ModuleList([nn.Linear(teacher_hidden_size, out_dim) for _ in range(student_num_layers)])
        self.proj_v = nn.ModuleList([nn.Linear(teacher_hidden_size, out_dim) for _ in range(student_num_layers)])

    def forward(self, teacher_hidden_last_T: List[torch.Tensor]) -> List[Tuple[torch.Tensor, torch.Tensor]]:
        kvs: List[Tuple[torch.Tensor, torch.Tensor]] = []
        for layer_idx in range(self.student_num_layers):
            h = teacher_hidden_last_T[layer_idx]  # [B, T, Ht]
            bsz, T, Ht = h.shape
            assert T == self.prefix_steps, f"expected {self.prefix_steps} steps, got {T}"
            h_flat = h.reshape(bsz * T, Ht)
            k_flat = self.proj_k[layer_idx](h_flat)
            v_flat = self.proj_v[layer_idx](h_flat)
            k = k_flat.reshape(bsz, T, self.student_num_kv_heads, self.student_head_dim)
            v = v_flat.reshape(bsz, T, self.student_num_kv_heads, self.student_head_dim)
            # Rearrange to [B, kv_heads, T, head_dim]
            k = k.permute(0, 2, 1, 3).contiguous()
            v = v.permute(0, 2, 1, 3).contiguous()
            kvs.append((k, v))
        return kvs


class JointCompilerInterpreter(nn.Module):
    """
    End-to-end module:
    - Compiler (teacher) encodes spec
    - ProgramPrefixMapper converts last `prefix_steps` teacher states into student K/V per layer (with RoPE on K)
    - Interpreter consumes KV cache and predicts output text
    """

    def __init__(
        self,
        compiler_model_name: str,
        interpreter_model_name: str,
        prefix_steps: int,
        max_spec_length: int,
        max_input_length: int,
        max_output_length: int,
        *,
        debug_nan: bool = False,
        compiler_tokenizer_path: Optional[str] = None,
        interpreter_tokenizer_path: Optional[str] = None,
        freeze_base_models: bool = False,
        disable_dropout: bool = False,
    ) -> None:
        super().__init__()
        self.debug_nan = debug_nan
        self.freeze_base_models = freeze_base_models
        self.disable_dropout = disable_dropout
        # Load tokenizers
        self.compiler_tokenizer = AutoTokenizer.from_pretrained(
            compiler_tokenizer_path if compiler_tokenizer_path is not None else compiler_model_name
        )
        self.interpreter_tokenizer = AutoTokenizer.from_pretrained(
            interpreter_tokenizer_path if interpreter_tokenizer_path is not None else interpreter_model_name
        )
        if self.compiler_tokenizer.pad_token is None:
            self.compiler_tokenizer.pad_token = self.compiler_tokenizer.eos_token
        if self.interpreter_tokenizer.pad_token is None:
            self.interpreter_tokenizer.pad_token = self.interpreter_tokenizer.eos_token

        self.compiler = AutoModelForCausalLM.from_pretrained(compiler_model_name)
        self.interpreter = AutoModelForCausalLM.from_pretrained(interpreter_model_name)

        if self.freeze_base_models:
            for p in self.compiler.parameters():
                p.requires_grad = False
            for p in self.interpreter.parameters():
                p.requires_grad = False

        teacher_hidden_size = self.compiler.config.hidden_size
        student_hidden_size = self.interpreter.config.hidden_size
        student_num_layers = getattr(self.interpreter.config, "num_hidden_layers", None) or getattr(
            self.interpreter.config, "n_layer", None
        )
        student_num_heads = getattr(self.interpreter.config, "num_attention_heads", None) or getattr(
            self.interpreter.config, "n_head", None
        )
        student_num_kv_heads = getattr(self.interpreter.config, "num_key_value_heads", None) or student_num_heads
        if student_num_heads is None or student_num_layers is None:
            raise ValueError("Cannot infer student model layers/heads from config")
        student_head_dim = student_hidden_size // student_num_heads

        self.prefix_steps = prefix_steps
        self.max_spec_length = max_spec_length
        self.max_input_length = max_input_length
        self.max_output_length = max_output_length

        self.mapper = ProgramPrefixMapper(
            teacher_hidden_size=teacher_hidden_size,
            student_num_layers=student_num_layers,
            student_num_kv_heads=student_num_kv_heads,
            student_head_dim=student_head_dim,
            prefix_steps=prefix_steps,
        )

    def build_student_inputs(
        self, inputs: List[str], outputs: List[str]
    ) -> Tuple[Dict[str, torch.Tensor], Dict[str, torch.Tensor]]:
        # Tokenize once per example: [prompt + target + EOS], then pad once per batch
        prompt_texts = [s for s in inputs]
        target_texts = [t for t in outputs]
        eos_tok = self.interpreter_tokenizer.eos_token
        combined_texts = [p + t + eos_tok for p, t in zip(prompt_texts, target_texts)]

        max_total_len = self.max_input_length + self.max_output_length
        tok = self.interpreter_tokenizer(
            combined_texts,
            padding=True,
            truncation=True,
            max_length=max_total_len,
            return_tensors="pt",
        )

        # Compute prompt lengths without padding/specials
        prompt_lens: List[int] = []
        for p in prompt_texts:
            ids = self.interpreter_tokenizer(p, add_special_tokens=False)["input_ids"]
            prompt_lens.append(len(ids))

        input_ids = tok.input_ids
        attention_mask = tok.attention_mask

        # Labels: copy input_ids, then mask prompt span and padding to -100 (EOS remains supervised)
        labels = input_ids.clone()
        for i, pl in enumerate(prompt_lens):
            labels[i, :pl] = -100
        labels = labels.masked_fill(attention_mask == 0, -100)

        return {"input_ids": input_ids, "attention_mask": attention_mask}, {"labels": labels}

    def build_teacher_inputs(self, specs: List[str]) -> Dict[str, torch.Tensor]:
        return self.compiler_tokenizer(
            specs,
            padding=True,
            truncation=True,
            max_length=self.max_spec_length,
            return_tensors="pt",
        )

    def compute_prefix_kv(self, teacher_outputs, teacher_attention_mask: torch.Tensor) -> List[Tuple[torch.Tensor, torch.Tensor]]:
        # Use last teacher layer only and select last non-pad tokens per example
        last_layer = list(teacher_outputs.hidden_states)[-1]  # [B, S, Ht]
        attn = teacher_attention_mask  # [B, S]
        lengths = attn.long().sum(dim=1)  # [B]
        bsz, S, Ht = last_layer.shape
        slices: List[torch.Tensor] = []
        for i in range(bsz):
            end = int(lengths[i].item())
            end = max(0, min(end, S))
            start = max(0, end - self.prefix_steps)
            h_i = last_layer[i, start:end, :]  # [t_i, Ht]
            t_i = h_i.size(0)
            if t_i < self.prefix_steps:
                if t_i == 0:
                    # no valid tokens: fallback to first hidden or zeros
                    pad_vec = last_layer[i, :1, :]
                else:
                    pad_vec = h_i[:1, :]
                pad = pad_vec.expand(self.prefix_steps - t_i, -1)
                h_i = torch.cat([pad, h_i], dim=0)
            slices.append(h_i)
        last_T = torch.stack(slices, dim=0)  # [B, T, Ht]

        # Duplicate for top student_num_layers layers to map per layer
        teacher_hidden_last_T = [last_T for _ in range(len(self.mapper.proj_k))]
        kvs = self.mapper(teacher_hidden_last_T)  # list of (k,v), k/v: [B, Hkv, T, D]
        return kvs

    def forward(
        self,
        specs: List[str],
        inputs: List[str],
        outputs: List[str],
    ) -> Dict[str, torch.Tensor]:
        # Optionally disable dropout during training
        if self.disable_dropout:
            self.compiler.train(False)
            self.interpreter.train(False)
        
        teacher_batch = self.build_teacher_inputs(specs)
        student_inputs, student_labels = self.build_student_inputs(inputs, outputs)

        device = next(self.parameters()).device
        teacher_batch = {k: v.to(device) for k, v in teacher_batch.items()}
        student_inputs = {k: v.to(device) for k, v in student_inputs.items()}
        student_labels = {k: v.to(device) for k, v in student_labels.items()}

        teacher_outputs = self.compiler(
            **teacher_batch,
            use_cache=False,
            output_hidden_states=True,
        )
        kv_prefix = self.compute_prefix_kv(teacher_outputs, teacher_batch["attention_mask"])

        attention_mask = student_inputs["attention_mask"]

        from transformers.cache_utils import DynamicCache  # type: ignore
        cache_obj = DynamicCache.from_legacy_cache(tuple(kv_prefix))
        bsz = student_inputs["input_ids"].size(0)
        seq_len = student_inputs["input_ids"].size(1)
        past_len = cache_obj.get_seq_length()
        position_ids = torch.arange(past_len, past_len + seq_len, device=device).unsqueeze(0).expand(bsz, -1)
        #import pdb; pdb.set_trace()

        outputs_student = self.interpreter(
            input_ids=student_inputs["input_ids"],
            #attention_mask=attention_mask,
            #position_ids=position_ids,
            labels=student_labels["labels"],
            past_key_values=cache_obj,
            use_cache=True,
        )
        return {"loss": outputs_student.loss, "logits": outputs_student.logits, "labels": student_labels["labels"]}

    @torch.no_grad()
    def compile_prefix(self, specs: List[str]) -> List[List[Tuple[torch.Tensor, torch.Tensor]]]:
        # Ensure deterministic behavior by disabling dropout
        was_training = self.compiler.training
        self.compiler.eval()
        try:
            teacher_batch = self.build_teacher_inputs(specs)
            device = next(self.parameters()).device
            teacher_batch = {k: v.to(device) for k, v in teacher_batch.items()}
            teacher_outputs = self.compiler(
                **teacher_batch,
                use_cache=False,
                output_hidden_states=True,
            )
            kv_prefix = self.compute_prefix_kv(teacher_outputs, teacher_batch["attention_mask"])
            # Split per batch
            bsz = teacher_batch["input_ids"].size(0)
            per_item: List[List[Tuple[torch.Tensor, torch.Tensor]]] = [[] for _ in range(bsz)]
            for (k, v) in kv_prefix:
                for i in range(bsz):
                    per_item[i].append((k[i].cpu(), v[i].cpu()))
            return per_item
        finally:
            if was_training:
                self.compiler.train()


class TextTriplesDataset(torch.utils.data.Dataset):
    def __init__(self, triples: List[Tuple[str, str, str]]):
        self.triples = triples

    def __len__(self) -> int:
        return len(self.triples)

    def __getitem__(self, idx: int) -> Dict[str, str]:
        spec, inp, out = self.triples[idx]
        return {"spec": spec, "input": inp, "output": out}


class Collator:
    def __init__(self, model: JointCompilerInterpreter):
        self.model = model

    def __call__(self, batch: List[Dict[str, str]]) -> Dict[str, List[str]]:
        specs = [b["spec"] for b in batch]
        inputs = [b["input"] for b in batch]
        outputs = [b["output"] for b in batch]
        return {"specs": specs, "inputs": inputs, "outputs": outputs}


def _to_device(inputs: Dict[str, torch.Tensor], device: torch.device) -> Dict[str, torch.Tensor]:
    return {k: (v.to(device) if isinstance(v, torch.Tensor) else v) for k, v in inputs.items()}


def _compute_token_metrics(eval_pred) -> Dict[str, float]:
    import numpy as _np
    import torch as _t

    pred_ids = eval_pred.predictions  # [batch, seq] - already argmaxed in prediction_step
    labels = eval_pred.label_ids     # [batch, seq]

    # Convert to torch tensors
    pred_ids_t = _t.from_numpy(pred_ids) if isinstance(pred_ids, _np.ndarray) else pred_ids
    labels_t = _t.from_numpy(labels) if isinstance(labels, _np.ndarray) else labels

    # Causal LM: predictions[i] correspond to labels[i+1], so shift for alignment
    pred_ids = pred_ids_t[:, :-1]  # [batch, seq-1]
    target_labels = labels_t[:, 1:]    # [batch, seq-1]
    
    mask = target_labels.ne(-100)
    if mask.sum() == 0:
        assert False, "No valid tokens in target labels"

    correct = pred_ids.eq(target_labels) & mask
    acc = correct.sum().float() / mask.sum().float()
    return {"token_accuracy": float(acc.item())}
    

class TrainerWrapper(Trainer):
    def __init__(self, joint_model: JointCompilerInterpreter, *args, **kwargs):
        self._debug_nan = kwargs.pop("debug_nan", False)
        super().__init__(model=joint_model, *args, **kwargs)

    def compute_loss(self, model: JointCompilerInterpreter, inputs, return_outputs=False, **kwargs):
        loss_dict = model(inputs["specs"], inputs["inputs"], inputs["outputs"])
        loss = loss_dict["loss"]
        return (loss, None) if return_outputs else loss

    def prediction_step(self, model: JointCompilerInterpreter, inputs, prediction_loss_only: bool, ignore_keys=None):
        model.eval()
        with torch.no_grad():
            out = model(inputs["specs"], inputs["inputs"], inputs["outputs"])
        loss = out["loss"].detach()
        logits = out.get("logits")
        labels = out.get("labels")
        if prediction_loss_only:
            return (loss, None, None)
        # Argmax on GPU then move to CPU to save massive RAM (vocab_size ~150K reduction)
        pred_ids = logits.argmax(dim=-1).detach().cpu() if logits is not None else None
        labels_cpu = labels.detach().cpu() if labels is not None else None
        return (loss, pred_ids, labels_cpu)

    def log(self, logs, start_time=None):
        if "loss" in logs:
            try:
                loss_val = float(logs["loss"]) if not isinstance(logs["loss"], (list, tuple)) else float(logs["loss"][0])
                if math.isfinite(loss_val):
                    logs["perplexity"] = math.exp(max(loss_val, 0.0))
            except Exception:
                pass
        if "eval_loss" in logs:
            try:
                eval_loss_val = float(logs["eval_loss"]) if not isinstance(logs["eval_loss"], (list, tuple)) else float(logs["eval_loss"][0])
                if math.isfinite(eval_loss_val):
                    logs["eval_perplexity"] = math.exp(max(eval_loss_val, 0.0))
            except Exception:
                pass
        return super().log(logs, start_time)

    def training_step(self, model: JointCompilerInterpreter, inputs, num_items_in_batch=None, **kwargs):
        # Honor disable_dropout flag by not flipping to train() mode
        if getattr(model, "disable_dropout", False):
            model.eval()
        else:
            model.train()
        inputs = self._prepare_inputs(inputs)
        loss = self.compute_loss(model, inputs)
        try:
            self.accelerator.backward(loss)
        except Exception:
            loss.backward()

        if self._debug_nan:
            try:
                found = False
                for name, param in model.named_parameters():
                    if param.grad is not None and torch.isnan(param.grad).any():
                        print(f"NAN_GRAD: {name} {tuple(param.grad.shape)}")
                        found = True
                if found:
                    import pdb; pdb.set_trace()
            except Exception:
                pass

        if self.args.gradient_accumulation_steps and self.args.gradient_accumulation_steps > 1:
            return loss.detach() / self.args.gradient_accumulation_steps
        return loss.detach()


def train(config: PrefixTuningConfig) -> str:
    os.makedirs(config.output_dir, exist_ok=True)

    # Seed
    torch.manual_seed(config.seed)

    # Load data
    train_triples = load_tuples(config.train_jsonl)

    val_triples: Optional[List[Tuple[str, str, str]]] = None
    if config.val_jsonl and os.path.exists(config.val_jsonl):
        val_triples = load_tuples(config.val_jsonl)

    # Debug: use a small subset for both train and eval to test overfitting
    if config.debug:
        train_triples = train_triples[: max(1, config.debug_size)]
        val_triples = list(train_triples)

    train_ds = TextTriplesDataset(train_triples)
    eval_ds = TextTriplesDataset(val_triples) if val_triples else None

    # Model
    model = JointCompilerInterpreter(
        compiler_model_name=config.compiler_model_name,
        interpreter_model_name=config.interpreter_model_name,
        prefix_steps=config.prefix_steps,
        max_spec_length=config.max_spec_length,
        max_input_length=config.max_input_length,
        max_output_length=config.max_output_length,
        debug_nan=config.debug_nan,
        freeze_base_models=config.freeze_base_models,
        disable_dropout=config.disable_dropout,
    )

    # Training args
    kwargs = dict(
        output_dir=config.output_dir,
        per_device_train_batch_size=config.batch_size,
        per_device_eval_batch_size=config.batch_size,
        gradient_accumulation_steps=config.gradient_accumulation_steps,
        learning_rate=config.learning_rate,
        num_train_epochs=config.num_epochs,
        save_steps=50 if config.debug else 500,
        save_total_limit=1,
        logging_steps=1 if config.debug else 20,
        remove_unused_columns=False,
        report_to=[],
        fp16=False,
        bf16=False,
    )
    
    sig = inspect.signature(TrainingArguments.__init__)
    assert "eval_strategy" in sig.parameters, "TrainingArguments must accept eval_strategy"
    kwargs["eval_strategy"] = "epoch" if eval_ds is not None else "no"
    assert "save_strategy" in sig.parameters, "TrainingArguments must accept save_strategy"
    kwargs["save_strategy"] = "epoch" if not config.debug else "no"
    assert "warmup_steps" in sig.parameters, "TrainingArguments must accept warmup_steps"
    kwargs["warmup_steps"] = config.warmup_steps
    assert "lr_scheduler_type" in sig.parameters, "TrainingArguments must accept lr_scheduler_type"
    kwargs["lr_scheduler_type"] = "linear"
    assert "max_grad_norm" in sig.parameters, "TrainingArguments must accept max_grad_norm"
    kwargs["max_grad_norm"] = config.max_grad_norm
    assert "save_safetensors" in sig.parameters, "TrainingArguments must accept save_safetensors"
    kwargs["save_safetensors"] = False
    assert "load_best_model_at_end" in sig.parameters, "TrainingArguments must accept load_best_model_at_end"
    kwargs["load_best_model_at_end"] = True
    assert "metric_for_best_model" in sig.parameters, "TrainingArguments must accept metric_for_best_model"
    kwargs["metric_for_best_model"] = "eval_loss"
    assert "greater_is_better" in sig.parameters, "TrainingArguments must accept greater_is_better"
    kwargs["greater_is_better"] = False
    assert "save_only_model" in sig.parameters, "TrainingArguments must accept save_only_model"
    kwargs["save_only_model"] = True

    args = TrainingArguments(**kwargs)

    collator = Collator(model)

    trainer = TrainerWrapper(
        joint_model=model,
        args=args,
        data_collator=collator,
        train_dataset=train_ds,
        eval_dataset=eval_ds,
        compute_metrics=_compute_token_metrics if eval_ds is not None else None,
        debug_nan=config.debug_nan,
    )

    # Pre-training validation
    if eval_ds is not None:
        print("=== Pre-training validation ===")
        metrics = trainer.evaluate()
        print(metrics)

    trainer.train()

    # Save checkpoint (models+tokenizers co-located) and mapper
    save_dir = os.path.join(config.output_dir, "checkpoint")
    os.makedirs(save_dir, exist_ok=True)

    compiler_dir = os.path.join(save_dir, "compiler")
    model.compiler.save_pretrained(compiler_dir, safe_serialization=False)
    model.compiler_tokenizer.save_pretrained(compiler_dir)

    interpreter_dir = os.path.join(save_dir, "interpreter")
    model.interpreter.save_pretrained(interpreter_dir, safe_serialization=False)
    model.interpreter_tokenizer.save_pretrained(interpreter_dir)
    # Override generation_config.json to set do_sample=false (deterministic by default)
    gen_config_path = os.path.join(interpreter_dir, "generation_config.json")
    if os.path.exists(gen_config_path):
        with open(gen_config_path, "r", encoding="utf-8") as f:
            gen_config = json.load(f)
        gen_config["do_sample"] = False
        # Remove sampling-only params that cause warnings with do_sample=False
        gen_config.pop("temperature", None)
        gen_config.pop("top_k", None)
        gen_config.pop("top_p", None)
        gen_config.pop("repetition_penalty", None)
        with open(gen_config_path, "w", encoding="utf-8") as f:
            json.dump(gen_config, f, indent=2)

    # Save mapper with compiler (since it maps from compiler to interpreter)
    torch.save(
        {
            "state_dict": model.mapper.state_dict(),
            "prefix_steps": config.prefix_steps,
            "compiler_model_name": config.compiler_model_name,
            "interpreter_model_name": config.interpreter_model_name,
        },
        os.path.join(compiler_dir, "mapper.pt"),
    )

    with open(os.path.join(config.output_dir, "LATEST"), "w", encoding="utf-8") as f:
        f.write(save_dir)

    return save_dir 
