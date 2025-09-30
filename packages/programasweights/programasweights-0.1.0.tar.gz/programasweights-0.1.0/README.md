# ProgramAsWeights

**⚠️ PLACEHOLDER PACKAGE - NOT YET FUNCTIONAL ⚠️**

This package is currently a placeholder to reserve the name "programasweights" on PyPI. 

The functionality is not yet available for public use. Please check back later for updates.

---

Programs as small weight blobs; a fixed interpreter runs them.

## Development

```
pip install -e .
```

```
python test_compile.py
```

```
python test_execute.py
```


## Quickstart

```bash
pip install programasweights
```

```python
import programasweights
f = programasweights.function("/path/to/weights")
print(f("Hello"))
```

- weights = programs; base model = interpreter.
- Deterministic by default (greedy generation).

## Train a compiler→KV prefix→interpreter (defaults)

```bash
# installs training extras
pip install -e .[train]

# trains on data/samples_train.jsonl with Qwen defaults
paw-train
```

- Produces checkpoint under `outputs/prefix_kv/checkpoint/`.

## Compile then run (qualitative eval)

```bash
# compile a prompt into a KV-prefix artifact
paw-eval
```

Or programmatically:

```python
import programasweights as paw

prompt = (
    "Parse a string like '(A) ... (B) ... (C) ...' into a JSON list of options. "
    "Be robust to noise: extra spaces, bullets, and phrases like 'both (A) and (B)'."
)

artifact_dir = paw.compile(
    out_dir="outputs/prefix_kv/demo_program",
    spec=prompt,
    checkpoint_dir="outputs/prefix_kv/checkpoint",
)

f = paw.function(artifact_dir, model_name="Qwen/Qwen2.5-Coder-0.5B-Instruct", max_new_tokens=128)
print(f("(A) cat  (B) dog  (C) both (A) and (B) are possible"))
```

- The dummy compiler is still available as `compile_dummy` for tests and demos.

## API

```python
import programasweights
parse_func = programasweights.function(
    "/path/to/weights.safetensors",
    model_name="google/flan-t5-small",
    max_new_tokens=128,
)
output = parse_func("input string")
```

- Accepts `str` or `List[str]` and returns the same shape.
- Aliasing works: `import programasweights as paw`.

## Local development

```bash
pip install -e .[test]
pytest -q
```

```bash
# smoke check
python -c "import programasweights as paw; print(paw.__version__)"
```

- `pip install -e .` installs in editable mode so code changes are picked up without reinstalling.
- If you do not need editable mode: `pip install .` (you must reinstall after changes).

## Notes

- MVP runtime uses a single in-process interpreter (loads the base model once and stays warm).
- Program artifact can be a prompt/prefix (text file) or a KV-prefix directory with `program.json` and `kv_prefix.pt`.
- Device selection: CUDA if available, else CPU. Override with env var `PROGRAMASWEIGHTS_DEVICE`.
- Simple global lock around `generate()` for thread safety.

## Roadmap

- Compiler: spec → weights
- LoRA support
- JSON-constrained decoding
- Server mode (multi-tenant)
