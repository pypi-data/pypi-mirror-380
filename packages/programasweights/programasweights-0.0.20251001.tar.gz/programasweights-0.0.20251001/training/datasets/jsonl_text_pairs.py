from __future__ import annotations

import json
from typing import Any, Dict, Iterator, List, Tuple


def iter_rows(jsonl_path: str) -> Iterator[Dict[str, Any]]:
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            yield json.loads(s)


def expand_pairs(row: Dict[str, Any]) -> Iterator[Dict[str, str]]:
    spec = str(row.get("spec", ""))
    inputs = list(row.get("inputs", []))
    outputs = list(row.get("outputs", []))
    for inp, out in zip(inputs, outputs):
        yield {"spec": spec, "input": str(inp), "output": str(out)}


def load_tuples(jsonl_path: str) -> List[Tuple[str, str, str]]:
    triples: List[Tuple[str, str, str]] = []
    for row in iter_rows(jsonl_path):
        for p in expand_pairs(row):
            triples.append((p["spec"], p["input"], p["output"]))
    return triples 