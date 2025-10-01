# Data Generation (for training)

This directory contains scripts for generating training/evaluation data using OpenAI models, with SQLite caching. It replaces the previous `scripts/` location for better organization under training.

## Overview

- `generate_specs.py`: Generate function specs (parsing, format conversion, regex-hard, etc.)
- `synthesize_data.py`: Given specs, synthesize input/output pairs per spec
- Output JSONL lines: `{ "spec": str, "inputs": [str], "outputs": [str] }`
- SQLite cache (`data/cache.sqlite3` by default) avoids repeated API calls.

## Setup

```bash
pip install -e .[data]
export OPENAI_API_KEY=your_key_here
export DATA_SYNTH_CACHE_DB=data/cache.sqlite3  # optional custom path
```

## Templates

Specs templates (used by `generate_specs.py`) under `training/data_generation/templates/`:
- `specs_system.txt`
- `specs_user.txt`

Placeholders:
- `{{num}}`: number of specs to generate in a batch
- `{{categories_text}}`: comma-separated categories list
- `{{batch_index}}`, `{{total_batches}}`, `{{run_id}}`: batch/run identifiers

Pairs templates (used by `synthesize_data.py`) under `training/data_generation/templates/`:
- `pairs_system.txt`
- `pairs_user.txt`

Placeholders:
- `{{spec}}`: the function spec
- `{{n}}`: number of pairs to generate for this spec
- `{{schema_instruction}}`: one of the predefined schema rules based on `--output-mode`

Override with flags:
```bash
# specs
python training/data_generation/generate_specs.py --templates-dir training/data_generation/templates --system-template custom/specs_system.txt --user-template custom/specs_user.txt
# pairs
python training/data_generation/synthesize_data.py --templates-dir training/data_generation/templates --system-template custom/pairs_system.txt --user-template custom/pairs_user.txt
```

## Pipeline

1) Generate specs
```bash
python training/data_generation/generate_specs.py --out data/specs.jsonl --num 100 --model gpt-5-mini
```

2) Synthesize examples for each spec (split into train/val/test by default)
```bash
python training/data_generation/synthesize_data.py \
  --out-dir data \
  --out-prefix samples \
  --specs-jsonl data/specs.jsonl \
  --per-spec 8 \
  --model gpt-5-mini \
  --temperature 1.0 \
  --enforce-json \
  --output-mode mapping
```

## Formats

- Specs file (`.jsonl`): objects with fields `spec`, `category`, `difficulty`
- Samples file (`.jsonl`): objects with fields `spec`, `inputs`, `outputs`

Notes on outputs:
- With `--enforce-json`, each pair can include `output_json` (object/array/string) or `output` (string). The script serializes `output_json` to a string in JSONL. 