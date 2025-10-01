from __future__ import annotations

import json
import os
from typing import Optional

import torch

from .dummy import compile_dummy  # noqa: F401 


def compile(
    out_dir: str,
    *,
    spec: str,
    checkpoint_dir: str = "outputs/prefix_kv/checkpoint",
    prefix_steps: Optional[int] = None,
) -> str:
    """
    Compile a spec into a KV-prefix artifact directory consumable by the runtime.

    - Loads mapper and tokenizers/models from `checkpoint_dir`
    - Saves `program.json` and `kv_prefix.pt` into `out_dir`
    - Returns `out_dir`
    """
    from training.loops.prefix_tuning_sft import JointCompilerInterpreter

    os.makedirs(out_dir, exist_ok=True)

    compiler_dir = os.path.join(checkpoint_dir, "compiler")
    interpreter_dir = os.path.join(checkpoint_dir, "interpreter")

    # Load metadata from compiler directory
    mapper_pkg = torch.load(os.path.join(compiler_dir, "mapper.pt"), map_location="cpu")
    compiler_model_name = mapper_pkg["compiler_model_name"]
    interpreter_model_name = mapper_pkg["interpreter_model_name"]
    steps = prefix_steps or mapper_pkg.get("prefix_steps", 5)

    model = JointCompilerInterpreter(
        compiler_model_name=compiler_dir if os.path.isdir(compiler_dir) else compiler_model_name,
        interpreter_model_name=interpreter_dir if os.path.isdir(interpreter_dir) else interpreter_model_name,
        prefix_steps=steps,
        max_spec_length=256,
        max_input_length=256,
        max_output_length=256,
    )
    # Load trained mapper weights for correct KV projection
    if "state_dict" in mapper_pkg:
        model.mapper.load_state_dict(mapper_pkg["state_dict"]) 
    model.eval()

    kv_per_item = model.compile_prefix([spec])  # one item
    layers = []
    for (k, v) in kv_per_item[0]:
        layers.append((k.cpu(), v.cpu()))

    torch.save({"layers": layers}, os.path.join(out_dir, "kv_prefix.pt"))

    manifest = {
        "kind": "prefix_kv",
        "base_model": interpreter_model_name,
        "prefix_steps": steps,
    }
    with open(os.path.join(out_dir, "program.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    return out_dir 