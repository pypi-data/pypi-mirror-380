#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sqlite3
import sys
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple


try:
    # OpenAI SDK v1
    from openai import OpenAI  # type: ignore
except Exception:  # pragma: no cover
    OpenAI = None  # type: ignore

from tqdm.auto import tqdm


@dataclass
class Cache:
    conn: sqlite3.Connection

    @staticmethod
    def open(path: str) -> "Cache":
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        conn = sqlite3.connect(path)
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS cache (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.commit()
        return Cache(conn)

    def get(self, key: str) -> Optional[str]:
        cur = self.conn.execute("SELECT value FROM cache WHERE key = ?", (key,))
        row = cur.fetchone()
        return row[0] if row else None

    def set(self, key: str, value: str) -> None:
        self.conn.execute("INSERT OR REPLACE INTO cache(key, value) VALUES(?, ?)", (key, value))
        self.conn.commit()


def stable_hash(obj: Any) -> str:
    data = json.dumps(obj, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def ensure_openai_client(api_key: Optional[str]) -> Any:
    if OpenAI is None:
        raise RuntimeError("openai python package not installed. Run: pip install openai")
    key = api_key or os.environ.get("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("Missing OPENAI_API_KEY. Export it or pass --openai-api-key.")
    return OpenAI(api_key=key)


def build_schema_instruction(output_mode: str) -> str:
    if output_mode == "mapping":
        return (
            "- Each pair's output must be a JSON object mapping string keys to string values (e.g., {\"A\": \"text\", ...}).\n"
        )
    if output_mode == "list_of_pairs":
        return (
            "- Each pair's output must be a JSON array of 2-item arrays [[key, value], ...], where keys and values are strings.\n"
        )
    if output_mode == "answer":
        return (
            "- Each pair's output must be a JSON string containing ONLY the final answer; do not include reasoning.\n"
        )
    return ""


def _default_templates_dir() -> str:
    return os.path.join(os.path.dirname(__file__), "templates")


def _read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _render_template(text: str, mapping: Dict[str, str]) -> str:
    out = text
    for k, v in mapping.items():
        out = out.replace(f"{{{{{k}}}}}", v)
    return out


def build_prompts(*, spec: str, n: int, schema_instruction: str) -> Dict[str, str]:
    base_dir = _default_templates_dir()
    sys_path = os.path.join(base_dir, "pairs_system.txt")
    usr_path = os.path.join(base_dir, "pairs_user.txt")

    system_template = _read_file(sys_path)
    user_template = _read_file(usr_path)

    mapping = {
        "spec": spec,
        "n": str(n),
        "schema_instruction": schema_instruction,
    }
    system_prompt = _render_template(system_template, mapping)
    user_prompt = _render_template(user_template, mapping)
    return {"system": system_prompt, "user": user_prompt}


def request_pairs(client: Any, model: str, system_prompt: str, user_prompt: str, temperature: float, *, enforce_json: bool, cache_salt: str, disable_cache: bool) -> List[Dict[str, Any]]:
    response_format = {"type": "json_object"} if enforce_json else None

    req = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": temperature,
        "response_format": response_format,
        "_cache_salt": cache_salt,
    }

    key = stable_hash(req)
    return _cached_response_pairs(client, req, key, disable_cache=disable_cache)


def _extract_text_from_responses_api(resp: Any) -> Optional[str]:
    # Heuristic extraction for Responses API
    if hasattr(resp, "output") and isinstance(resp.output, list):
        chunks: List[str] = []
        for c in resp.output:
            content = getattr(c, "content", [])
            for b in content:
                t = getattr(getattr(b, "text", None), "value", None)
                if isinstance(t, str):
                    chunks.append(t)
        if chunks:
            return "".join(chunks)
    # Fallback
    if hasattr(resp, "output_text") and isinstance(resp.output_text, str):
        return resp.output_text
    return None


def _cached_response_pairs(client: Any, req: Dict[str, Any], key: str, *, disable_cache: bool) -> List[Dict[str, Any]]:
    cache_path = os.environ.get("DATA_SYNTH_CACHE_DB", "data/cache.sqlite3")
    cache = Cache.open(cache_path)

    if not disable_cache:
        cached = cache.get(key)
        if cached is not None:
            payload = json.loads(cached)
            return payload["pairs"]

    # Use Chat Completions API so response_format is supported; let exceptions raise
    kwargs = {
        "model": req["model"],
        "messages": req["messages"],
        "temperature": req.get("temperature"),
    }
    if req.get("response_format") is not None:
        kwargs["response_format"] = req["response_format"]
    resp = client.chat.completions.create(**kwargs)
    content_text = resp.choices[0].message.content
    if not content_text:
        raise RuntimeError("Empty response content from model")

    # Parse JSON directly (no extraction needed with enforce_json)
    data = json.loads(content_text)
    if not isinstance(data, dict) or "pairs" not in data or not isinstance(data["pairs"], list):
        raise RuntimeError(f"Malformed JSON structure: expected dict with 'pairs' list. Got: {data}")

    if not disable_cache:
        cache.set(key, json.dumps(data, ensure_ascii=False))
    return data["pairs"]


def write_jsonl(path: str, rows: List[Dict[str, Any]], append: bool = False) -> None:
    os.makedirs(os.path.dirname(os.path.abspath(path)) or ".", exist_ok=True)
    mode = "a" if append else "w"
    with open(path, mode, encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def load_specs_from_args(args: argparse.Namespace) -> List[str]:
    # Priority: specs_jsonl -> spec_file -> repeated --spec
    specs: List[str] = []
    if args.specs_jsonl:
        with open(args.specs_jsonl, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                obj = json.loads(line)
                s = str(obj.get("spec", "")).strip()
                if s:
                    specs.append(s)
    elif args.spec_file:
        with open(args.spec_file, "r", encoding="utf-8") as f:
            for line in f:
                s = line.strip()
                if s:
                    specs.append(s)
    else:
        specs.extend(args.spec or [])

    if not specs:
        raise SystemExit("No specs provided. Pass --specs-jsonl (default), --spec-file, or --spec.")
    return specs


def synthesize_for_spec(client: Any, model: str, spec: str, per_spec: int, temperature: float, *, enforce_json: bool, output_mode: str, batch_size: int = 8, cache_salt: str = "", disable_cache: bool = False) -> Dict[str, Any]:
    schema = build_schema_instruction(output_mode)
    remaining = per_spec
    batch_index = 0

    inputs: List[str] = []
    outputs: List[str] = []

    # Per-spec progress bar
    spec_tag = hashlib.sha256(spec.encode("utf-8")).hexdigest()[:8]
    pbar = tqdm(total=per_spec, desc=f"Synth per-spec ({spec_tag})", unit="ex", leave=False)

    try:
        while remaining > 0:
            n = min(batch_size, remaining)
            batch_salt = f"{cache_salt}|batch:{batch_index}"
            prompts = build_prompts(spec=spec, n=n, schema_instruction=schema)
            user_prompt = prompts["user"]
            pairs = request_pairs(
                client,
                model=model,
                system_prompt=prompts["system"],
                user_prompt=user_prompt,
                temperature=temperature,
                enforce_json=enforce_json,
                cache_salt=batch_salt,
                disable_cache=disable_cache,
            )
            added = 0
            for p in pairs:
                inp = str(p.get("input", "")).strip()
                if "output_json" in p:
                    try:
                        out_json = p["output_json"]
                        out = json.dumps(out_json, ensure_ascii=False)
                    except Exception:
                        out = json.dumps(p["output_json"], ensure_ascii=False)
                else:
                    out = str(p.get("output", "")).strip()
                if inp:
                    inputs.append(inp)
                    outputs.append(out)
                    remaining -= 1
                    added += 1
                    if remaining <= 0:
                        break
            if added > 0:
                pbar.update(added)
            batch_index += 1
    finally:
        pbar.close()

    if not inputs:
        raise RuntimeError("Model produced no valid pairs")
    return {"spec": spec, "inputs": inputs, "outputs": outputs}


def split_specs(specs: List[str], train_ratio: float, val_ratio: float, test_ratio: float, seed: int) -> Dict[str, List[str]]:
    total = len(specs)
    if total == 1:
        return {"train": specs, "val": specs, "test": specs}
    rnd = random.Random(seed)
    shuffled = specs[:]
    rnd.shuffle(shuffled)
    # Normalize ratios
    s = train_ratio + val_ratio + test_ratio
    if s <= 0:
        raise ValueError("Sum of ratios must be > 0")
    tr = train_ratio / s
    vr = val_ratio / s
    # test is remainder
    n_train = int(total * tr)
    n_val = int(total * vr)
    n_test = total - n_train - n_val
    train = shuffled[:n_train]
    val = shuffled[n_train:n_train + n_val]
    test = shuffled[n_train + n_val:]
    return {"train": train, "val": val, "test": test}


def _synthesize_spec_worker(args_tuple) -> Dict[str, Any]:
    """Worker function for parallel processing of specs"""
    client, model, spec, per_spec, temperature, enforce_json, output_mode, batch_size, cache_salt, disable_cache = args_tuple
    return synthesize_for_spec(
        client=client,
        model=model,
        spec=spec,
        per_spec=per_spec,
        temperature=temperature,
        enforce_json=enforce_json,
        output_mode=output_mode,
        batch_size=batch_size,
        cache_salt=cache_salt,
        disable_cache=disable_cache,
    )


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Synthesize dataset with OpenAI and cache in SQLite.")
    # Single-file mode (legacy)
    parser.add_argument("--out", help="Output JSONL path (single combined file). If set, disables split outputs.")
    # Split mode (default)
    parser.add_argument("--out-dir", default="data", help="Directory to write split JSONL files")
    parser.add_argument("--out-prefix", default="samples_morecategories_40960examples", help="Prefix for split files (e.g., samples_train.jsonl)")

    # Spec sources
    parser.add_argument("--specs-jsonl", default="data/specs_morecategories_40960examples.jsonl", help="Specs JSONL path (default: data/specs.jsonl)")
    parser.add_argument("--spec", action="append", help="Function spec (can be repeated)")
    parser.add_argument("--spec-file", help="Path to a file with one spec per line (txt)")

    # Synthesis params
    parser.add_argument("--per-spec", type=int, default=8, help="Number of examples per spec")
    parser.add_argument("--batch-size", type=int, default=8, help="Batch size per request when per-spec is large")
    parser.add_argument("--per-spec-train", type=int, help="Override per-spec for train split")
    parser.add_argument("--per-spec-val", type=int, help="Override per-spec for val split")
    parser.add_argument("--per-spec-test", type=int, help="Override per-spec for test split")
    parser.add_argument("--model", default="gpt-5-mini", help="OpenAI model name")
    parser.add_argument("--temperature", type=float, default=1.0, help="Sampling temperature")
    parser.add_argument("--openai-api-key", help="API key (or set OPENAI_API_KEY)")
    parser.add_argument("--append", action="store_true", help="Append to output files if they exist")
    parser.add_argument("--enforce-json", action="store_true", default=True, help="Force model to return a JSON object via response_format")
    parser.add_argument("--output-mode", choices=["mapping", "list_of_pairs", "answer"], default="answer", help="Shape of each pair's output")

    # Parallel processing
    parser.add_argument("--workers", type=int, default=1, help="Number of parallel workers for API calls")

    # Splitting
    parser.add_argument("--train-ratio", type=float, default=0.8)
    parser.add_argument("--val-ratio", type=float, default=0.1)
    parser.add_argument("--test-ratio", type=float, default=0.1)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--disable-cache", action="store_true", help="Bypass SQLite cache (always call API)")

    args = parser.parse_args(argv)

    client = ensure_openai_client(args.openai_api_key)

    specs = load_specs_from_args(args)

    # Single combined file mode
    if args.out:
        rows: List[Dict[str, Any]] = []
        if args.workers == 1:
            # Sequential processing
            pbar = tqdm(total=len(specs), desc="Synthesizing (combined)", unit="spec")
            for spec in specs:
                cache_salt = f"run:{args.seed}|split:combined"
                row = synthesize_for_spec(
                    client,
                    model=args.model,
                    spec=spec,
                    per_spec=args.per_spec,
                    temperature=args.temperature,
                    enforce_json=args.enforce_json,
                    output_mode=args.output_mode,
                    batch_size=args.batch_size,
                    cache_salt=cache_salt,
                    disable_cache=args.disable_cache,
                )
                rows.append(row)
                pbar.update(1)
            pbar.close()
        else:
            # Parallel processing
            with ThreadPoolExecutor(max_workers=args.workers) as executor:
                futures = []
                for spec in specs:
                    cache_salt = f"run:{args.seed}|split:combined"
                    args_tuple = (
                        client, args.model, spec, args.per_spec, args.temperature,
                        args.enforce_json, args.output_mode, args.batch_size, cache_salt, args.disable_cache
                    )
                    future = executor.submit(_synthesize_spec_worker, args_tuple)
                    futures.append(future)
                
                pbar = tqdm(total=len(specs), desc="Synthesizing (combined)", unit="spec")
                for future in as_completed(futures):
                    row = future.result()
                    rows.append(row)
                    pbar.update(1)
                pbar.close()

        if not rows:
            print("No rows synthesized", file=sys.stderr)
            return 2
        write_jsonl(args.out, rows, append=args.append)
        print(f"Wrote {len(rows)} specs to {args.out}")
        return 0

    # Split mode
    splits = split_specs(specs, args.train_ratio, args.val_ratio, args.test_ratio, args.seed)
    os.makedirs(args.out_dir, exist_ok=True)
    split_to_path = {
        "train": os.path.join(args.out_dir, f"{args.out_prefix}_train.jsonl"),
        "val": os.path.join(args.out_dir, f"{args.out_prefix}_val.jsonl"),
        "test": os.path.join(args.out_dir, f"{args.out_prefix}_test.jsonl"),
    }

    # Per-spec overrides per split
    per_spec_map = {
        "train": args.per_spec_train or args.per_spec,
        "val": args.per_spec_val or args.per_spec,
        "test": args.per_spec_test or args.per_spec,
    }

    total_counts = {k: 0 for k in splits.keys()}
    for split_name, split_specs_list in splits.items():
        rows: List[Dict[str, Any]] = []
        if args.workers == 1:
            # Sequential processing
            pbar = tqdm(total=len(split_specs_list), desc=f"Synthesizing ({split_name})", unit="spec")
            for spec in split_specs_list:
                cache_salt = f"run:{args.seed}|split:{split_name}"
                row = synthesize_for_spec(
                    client,
                    model=args.model,
                    spec=spec,
                    per_spec=per_spec_map[split_name],
                    temperature=args.temperature,
                    enforce_json=args.enforce_json,
                    output_mode=args.output_mode,
                    batch_size=args.batch_size,
                    cache_salt=cache_salt,
                    disable_cache=args.disable_cache,
                )
                rows.append(row)
                pbar.update(1)
            pbar.close()
        else:
            # Parallel processing
            with ThreadPoolExecutor(max_workers=args.workers) as executor:
                futures = []
                for spec in split_specs_list:
                    cache_salt = f"run:{args.seed}|split:{split_name}"
                    args_tuple = (
                        client, args.model, spec, per_spec_map[split_name], args.temperature,
                        args.enforce_json, args.output_mode, args.batch_size, cache_salt, args.disable_cache
                    )
                    future = executor.submit(_synthesize_spec_worker, args_tuple)
                    futures.append(future)
                
                pbar = tqdm(total=len(split_specs_list), desc=f"Synthesizing ({split_name})", unit="spec")
                for future in as_completed(futures):
                    row = future.result()
                    rows.append(row)
                    pbar.update(1)
                pbar.close()

        if rows:
            write_jsonl(split_to_path[split_name], rows, append=args.append)
            total_counts[split_name] += len(rows)
            print(f"Wrote {len(rows)} specs to {split_to_path[split_name]}")
        else:
            print(f"No rows synthesized for split {split_name}", file=sys.stderr)

    print(f"Done. Counts → train:{total_counts['train']} val:{total_counts['val']} test:{total_counts['test']}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main()) 
