from __future__ import annotations

import random
from typing import Optional


def compile_dummy(out_path: str, spec: Optional[str] = None, *, seed: Optional[int] = None, num_tokens: int = 32) -> str:
    """
    Dummy compiler that writes a random textual prefix to out_path.

    - Ignores `spec` (placeholder for future real compiler)
    - If `seed` is provided, generation is deterministic
    - Resulting file is a UTF-8 text file that the runtime uses as a prompt/prefix
    """
    rng = random.Random(seed)
    tokens = [f"[P{rng.randint(0, 9999):04d}]" for _ in range(num_tokens)]
    prefix = " ".join(tokens)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(prefix)
    return out_path 