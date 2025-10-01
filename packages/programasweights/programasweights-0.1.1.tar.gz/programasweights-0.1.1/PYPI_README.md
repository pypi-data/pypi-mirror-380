# ProgramAsWeights

A minimal runtime where programs are weight blobs run by a fixed interpreter.

## Installation

```bash
pip install programasweights
```

## Quick Start

```python
import programasweights as paw

# Load a compiled program
f = paw.function("path/to/program", interpreter_name="yuntian-deng/paw-interpreter")

# Use the program function
result = f("Your input string here")
print(result)
```

## Example Usage

```python
import programasweights as paw

# Load a program that processes key-value mappings
f = paw.function("outputs_1spec/prefix_kv/eval_program", interpreter_name="yuntian-deng/paw-interpreter")

# Process input
string = "A: b b:a, d:a"
result = f(string)
print(result)  # Output: {"A":"b":"a","D":"d":"a"}
```

## Features

- **Simple API**: Load and run neural programs with just a few lines of code
- **Flexible Interpreters**: Support for different transformer models as interpreters
- **Efficient Execution**: Optimized runtime for prefix-tuned neural programs
- **Easy Integration**: Seamlessly integrate neural programs into your Python applications

## Requirements

- Python >= 3.8
- PyTorch
- Transformers

## License

MIT License
