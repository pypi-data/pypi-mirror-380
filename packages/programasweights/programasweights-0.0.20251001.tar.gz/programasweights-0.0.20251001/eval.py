from __future__ import annotations

import argparse
import os
import hashlib

import torch
import programasweights as paw
from training.datasets.jsonl_text_pairs import load_tuples


def compute_similarity(pred: str, target: str) -> float:
    """Normalized edit distance similarity (1.0 = identical, 0.0 = completely different)"""
    import difflib
    return difflib.SequenceMatcher(None, pred, target).ratio()


def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Qualitative evaluation: compile spec → run examples.")
    p.add_argument("--spec", type=str, default=(
        "Parse a string like '(A) ... (B) ... (C) ...' into a JSON list of options. "
        "Be robust to noise: extra spaces, bullets, and phrases like 'both (A) and (B)'."
    ))
    p.add_argument("--checkpoint-dir", type=str, default="outputs/prefix_kv/checkpoint",
                   help="Directory containing trained models, tokenizers, and mapper.pt")
    p.add_argument("--out-dir", type=str, default="outputs/prefix_kv/eval_program",
                   help="Directory to write compiled program artifact(s)")
    p.add_argument("--model-name", type=str, default="Qwen/Qwen2.5-Coder-0.5B-Instruct",
                   help="Fallback interpreter model if no fine-tuned dir is found")
    p.add_argument("--max-new-tokens", type=int, default=128)
    p.add_argument("--debug-dump-kv", action="store_true",
                   help="Print first 5 elements of K/V (last layer only) before running eval")

    # Dataset-driven eval (use same top-N examples as debug training)
    p.add_argument("--dataset-jsonl", type=str, default="",
                   help="If set, load examples from this JSONL file; uses each row's spec for compile")
    p.add_argument("--limit", type=int, default=-1,
                   help="Number of examples to take from the dataset when --dataset-jsonl is provided")
    return p


def main() -> None:
    args = build_arg_parser().parse_args()

    os.makedirs(args.out_dir, exist_ok=True)

    # Prefer fine-tuned interpreter/tokenizer if present
    finetuned_interpreter = os.path.join(args.checkpoint_dir, "interpreter")
    use_model = finetuned_interpreter
    results = []

    # If dataset is provided, compile per-example using row.spec; else compile once with --spec
    if args.dataset_jsonl and os.path.exists(args.dataset_jsonl):
        triples = load_tuples(args.dataset_jsonl)
        if args.limit > 0:
            triples = triples[: args.limit]
        if not triples:
            print("No examples found.")
            return

        # Compile per distinct spec (dedupe by hash)
        spec_to_dir: dict[str, str] = {}
        for idx, (spec, inp, tgt) in enumerate(triples):
            spec_key = hashlib.sha256(spec.encode("utf-8")).hexdigest()[:16]
            spec_dir = os.path.join(args.out_dir, f"kv_{spec_key}")
            if spec_key not in spec_to_dir:
                paw.compile(spec_dir, spec=spec, checkpoint_dir=args.checkpoint_dir)
                if args.debug_dump_kv:
                    try:
                        pkg = torch.load(os.path.join(spec_dir, "kv_prefix.pt"), map_location="cpu")
                        layers = pkg.get("layers", [])
                        if layers:
                            li = len(layers) - 1
                            k, v = layers[li]
                            print("=== DEBUG: EVAL KV DUMP (compiled, last layer only) ===")
                            print(f"SPEC={spec}")
                            print(f"EX={idx} L={li} K[:5]={k.reshape(-1)[:5].tolist()} V[:5]={v.reshape(-1)[:5].tolist()}")
                    except Exception as e:
                        print(f"DEBUG_KV_DUMP_ERROR: {e}")
                spec_to_dir[spec_key] = spec_dir

            fn = paw.function(spec_to_dir[spec_key], interpreter_name=use_model, max_new_tokens=args.max_new_tokens)
            pred = fn(inp)
            
            # Compute accuracy
            exact_match = (pred.strip() == tgt.strip())
            similarity = compute_similarity(pred, tgt)
            results.append({
                "exact_match": exact_match,
                "similarity": similarity,
                "input": inp,
                "target": tgt,
                "prediction": pred
            })
            
            print("SPEC:", spec)
            print("INPUT:", inp)
            print("TARGET:", tgt)
            print("OUTPUT:", pred)
            print(f"EXACT_MATCH: {exact_match}, SIMILARITY: {similarity:.3f}")
            print()
    else:
        # Single-compile path using provided --spec
        paw.compile(args.out_dir, spec=args.spec, checkpoint_dir=args.checkpoint_dir)
        if args.debug_dump_kv:
            try:
                pkg = torch.load(os.path.join(args.out_dir, "kv_prefix.pt"), map_location="cpu")
                layers = pkg.get("layers", [])
                if layers:
                    li = len(layers) - 1
                    k, v = layers[li]
                    print("=== DEBUG: EVAL KV DUMP (compiled, last layer only) ===")
                    print(f"SPEC={args.spec}")
                    print(f"L={li} K[:5]={k.reshape(-1)[:5].tolist()} V[:5]={v.reshape(-1)[:5].tolist()}")
            except Exception as e:
                print(f"DEBUG_KV_DUMP_ERROR: {e}")

        # No dataset provided; just run a couple of canned examples
        fn = paw.function(args.out_dir, interpreter_name=use_model, max_new_tokens=args.max_new_tokens)
        for s in [
            "(A) cat  (B) dog  (C) both (A) and (B) are possible",
            "1) Alpha 2) Beta 3) Gamma",
            "[1] Red [2] Green [3] Blue",
        ]:
            pred = fn(s)
            print("SPEC:", args.spec)
            print("INPUT:", s)
            print("OUTPUT:", pred)

    # Print overall accuracy if we have targets
    if results:
        exact_matches = sum(r["exact_match"] for r in results)
        avg_similarity = sum(r["similarity"] for r in results) / len(results)
        
        print("=== EVALUATION SUMMARY ===")
        print(f"Total examples: {len(results)}")
        print(f"Exact matches: {exact_matches}/{len(results)} ({exact_matches/len(results)*100:.1f}%)")
        print(f"Average similarity: {avg_similarity:.3f}")


if __name__ == "__main__":
    main() 