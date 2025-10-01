from __future__ import annotations

import os
import json
from typing import Optional

from training.loops.prefix_tuning_sft import PrefixTuningConfig, train as train_loop


def train_default() -> str:
    """Run training with default settings and data in `data/`.
    Returns the checkpoint directory path.
    """
    cfg = PrefixTuningConfig()
    return train_loop(cfg)


def evaluate_default() -> None:
    """Qualitative evaluation on a few samples using the compile→function API."""
    import programasweights as paw

    # Example prompt from the description
    prompt = (
        "Parse a string like '(A) ... (B) ... (C) ...' into a JSON list of options. "
        "Be robust to noise: extra spaces, bullets, and phrases like 'both (A) and (B)'."
    )

    ckpt = os.path.join("outputs", "prefix_kv", "checkpoint")
    out_dir = os.path.join("outputs", "prefix_kv", "eval_program")

    paw.compile(out_dir, spec=prompt, checkpoint_dir=ckpt)

    fn = paw.function(out_dir, model_name="Qwen/Qwen2.5-Coder-0.5B-Instruct", max_new_tokens=128)

    examples = [
        "(A) cat  (B) dog  (C) both (A) and (B) are possible",
        "1) Alpha 2) Beta 3) Gamma",
        "[1] Red [2] Green [3] Blue",
    ]
    for s in examples:
        print("INPUT:", s)
        print("OUTPUT:", fn(s)) 