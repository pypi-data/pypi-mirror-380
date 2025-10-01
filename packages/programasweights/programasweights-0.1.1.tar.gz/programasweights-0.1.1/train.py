from __future__ import annotations

import argparse
import json
import os

from training.loops.prefix_tuning_sft import PrefixTuningConfig, train


def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Train compiler→KV-prefix→interpreter with defaults.")

    # Models
    p.add_argument("--compiler-model-name", type=str, default="Qwen/Qwen3-0.6B",
                   help="Hugging Face model id for the compiler (teacher)")
    p.add_argument("--interpreter-model-name", type=str, default="Qwen/Qwen2.5-Coder-0.5B-Instruct",
                   help="Hugging Face model id for the interpreter (student)")

    # Data
    p.add_argument("--train-jsonl", type=str, default="data/samples_8192examples_train.jsonl",
                   help="Path to training JSONL triples (spec, inputs, outputs)")
    p.add_argument("--val-jsonl", type=str, default="data/samples_8192examples_val.jsonl",
                   help="Optional path to validation JSONL triples")

    # Optimization
    p.add_argument("--learning-rate", type=float, default=5e-5)
    p.add_argument("--batch-size", type=int, default=16)
    p.add_argument("--gradient-accumulation-steps", type=int, default=2)
    p.add_argument("--num-epochs", type=int, default=10)
    p.add_argument("--warmup-steps", type=int, default=100,
                   help="Linear LR warmup steps before reaching the target LR")
    p.add_argument("--max-grad-norm", type=float, default=1.0,
                   help="Gradient clipping norm (0 disables clipping)")

    # Lengths
    p.add_argument("--max-spec-length", type=int, default=256)
    p.add_argument("--max-input-length", type=int, default=256)
    p.add_argument("--max-output-length", type=int, default=256)

    # Prefix settings
    p.add_argument("--prefix-steps", type=int, default=5,
                   help="Number of teacher time steps to convert into KV prefix")

    # Debug
    p.add_argument("--debug", action="store_true",
                   help="Enable tiny debug mode: take first N samples and use them for both train and eval")
    p.add_argument("--debug-size", type=int, default=5,
                   help="Number of samples to keep in debug mode")
    p.add_argument("--debug-nan", action="store_true",
                   help="After backward, print names of parameters with NaN grads and drop into pdb")
    p.add_argument("--debug-dump-kv", action="store_true",
                   help="After training, dump first 5 elements of K/V per layer for first batch")

    # IO
    p.add_argument("--output-dir", type=str, default="outputs/prefix_kv")
    p.add_argument("--seed", type=int, default=42)

    # Model control
    p.add_argument("--freeze-base-models", action="store_true",
                   help="Freeze compiler/interpreter; train mapper only")
    p.add_argument("--disable-dropout", default=True, action="store_true",
                   help="Disable dropout during training to match eval determinism")

    return p


def main() -> None:
    args = build_arg_parser().parse_args()

    cfg = PrefixTuningConfig(
        compiler_model_name=args.compiler_model_name,
        interpreter_model_name=args.interpreter_model_name,
        train_jsonl=args.train_jsonl,
        val_jsonl=args.val_jsonl if os.path.exists(args.val_jsonl) else None,
        learning_rate=args.learning_rate,
        batch_size=args.batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        num_epochs=args.num_epochs,
        max_spec_length=args.max_spec_length,
        max_input_length=args.max_input_length,
        max_output_length=args.max_output_length,
        warmup_steps=args.warmup_steps,
        max_grad_norm=args.max_grad_norm,
        prefix_steps=args.prefix_steps,
        debug=args.debug,
        debug_size=args.debug_size,
        debug_nan=args.debug_nan,
        debug_dump_kv=args.debug_dump_kv,
        output_dir=args.output_dir,
        seed=args.seed,
        freeze_base_models=args.freeze_base_models,
        disable_dropout=args.disable_dropout,
    )

    os.makedirs(cfg.output_dir, exist_ok=True)

    print("Training config:")
    print(json.dumps(cfg.__dict__, indent=2))

    save_dir = train(cfg)
    print(f"Saved checkpoint to: {save_dir}")


if __name__ == "__main__":
    main()
