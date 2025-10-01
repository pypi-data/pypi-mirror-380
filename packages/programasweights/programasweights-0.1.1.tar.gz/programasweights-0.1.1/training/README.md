# Training (scaffold)

This folder houses non-runtime code for training compilers/interpreters. It is intentionally separate from the end-user runtime package to keep imports fast and dependencies minimal.

## Layout

- `datasets/`: readers and preprocessing for training data
- `loops/`: training loops (e.g., SFT, prefix-tuning, LoRA)
- `data_generation/`: spec generation and sample synthesis (OpenAI + SQLite cache)
- `configs/`: example YAML configs

## Data format

We assume JSONL with one object per line:
- `spec`: string describing the function
- `inputs`: list of strings
- `outputs`: list of strings (same length as inputs)

Example line:
```json
{"spec": "Extract the city from a sentence.", "inputs": ["I live in Paris."], "outputs": ["Paris"]}
```

Use `training/data_generation/generate_specs.py` and `training/data_generation/synthesize_data.py` (or the CLIs `paw-generate-specs`, `paw-synthesize-data`) to create datasets.

## Datasets helpers

- `datasets/jsonl_text_pairs.py` provides utilities to iterate rows and expand to (spec, input, output) tuples.

## Training loops

- `loops/prefix_tuning_sft.py` contains a placeholder callable `train(...)`. Fill in with your preferred framework (PEFT, LoRA, etc.).

## Dependencies

Install optional extras when working on training:
```bash
pip install -e .[train]
```

## Notes

- Keep runtime-focused changes in `programasweights/` isolated from training code.
- Prefer config-driven experiments and log all hyperparameters.
- Save artifacts with a small manifest (e.g., `program.json`) next to tensors for reproducibility. 