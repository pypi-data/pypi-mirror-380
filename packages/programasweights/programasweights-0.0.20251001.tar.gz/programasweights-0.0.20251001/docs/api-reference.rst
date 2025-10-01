API Reference
=============

This page documents the main ProgramAsWeights API for end users.

Core Functions
--------------

paw.function()
~~~~~~~~~~~~~~

Load and execute a neural program.

.. code-block:: python

   paw.function(path, *, name=None, interpreter_name="google/flan-t5-small", 
                tokenizer_name=None, max_new_tokens=128)

**Parameters:**

- **path** (*str*) - HuggingFace model ID (e.g., "yuntian-deng/paw-parser") or local directory path
- **name** (*str, optional*) - Custom name for the program (defaults to basename of path)
- **interpreter_name** (*str*) - Interpreter model to use (defaults to "google/flan-t5-small")
- **tokenizer_name** (*str, optional*) - Custom tokenizer path (defaults to interpreter's tokenizer)
- **max_new_tokens** (*int*) - Maximum tokens to generate (default: 128)

**Returns:**
``Callable[[Union[str, List[str]]], Union[str, List[str]]]`` - Function that accepts string or list of strings

**Examples:**

.. code-block:: python

   # Basic usage
   fn = paw.function("yuntian-deng/paw-sentiment")
   result = fn("This is great!")
   
   # Batch processing
   results = fn(["Good product", "Bad service", "Okay experience"])
   
   # Custom interpreter
   fn = paw.function("yuntian-deng/paw-parser", 
                     interpreter_name="yuntian-deng/paw-interpreter")

paw.compile()
~~~~~~~~~~~~~

Compile a natural language spec into a neural program (requires trained models).

.. code-block:: python

   paw.compile(out_dir, *, spec, checkpoint_dir="outputs/prefix_kv/checkpoint", 
               prefix_steps=None)

**Parameters:**

- **out_dir** (*str*) - Directory to save the compiled program
- **spec** (*str*) - Natural language description of the desired function
- **checkpoint_dir** (*str*) - Path to trained compiler/interpreter checkpoints
- **prefix_steps** (*int, optional*) - Override prefix length (defaults to trained value)

**Returns:**
*str* - Path to the compiled program directory

**Example:**

.. code-block:: python

   # Compile a custom program
   program_dir = paw.compile(
       out_dir="my_custom_parser",
       spec="Extract email addresses from text and return as JSON array"
   )
   
   # Use the compiled program
   fn = paw.function(program_dir)
   emails = fn("Contact: alice@example.com or bob@test.org")

Utility Functions
-----------------

paw.compile_dummy()
~~~~~~~~~~~~~~~~~~~

Create a dummy program for testing (legacy).

.. code-block:: python

   paw.compile_dummy(out_path, spec=None, *, seed=None, num_tokens=32)

**Parameters:**

- **out_path** (*str*) - Output file path
- **spec** (*str, optional*) - Ignored (for API compatibility)
- **seed** (*int, optional*) - Random seed for deterministic output
- **num_tokens** (*int*) - Number of dummy tokens to generate

**Returns:**
*str* - Path to the created dummy program

**Example:**

.. code-block:: python

   # Create deterministic dummy for testing
   paw.compile_dummy("test.weights", seed=42)
   fn = paw.function("test.weights")
   print(fn("test input"))

Configuration
-------------

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

**PROGRAMASWEIGHTS_DEVICE**
   Force device selection:
   
   - ``"cpu"`` - Use CPU only
   - ``"cuda"`` - Use GPU if available, fallback to CPU
   - Not set - Auto-detect (GPU if available)

   .. code-block:: bash
   
      export PROGRAMASWEIGHTS_DEVICE=cpu
      python my_script.py

**HF_TOKEN**
   HuggingFace authentication token for accessing private models:
   
   .. code-block:: bash
   
      export HF_TOKEN=your_token_here

Error Handling
--------------

Common Exceptions
~~~~~~~~~~~~~~~~~

**ValueError**
   - Invalid program artifact type
   - Missing KV prefix in program
   - Malformed program directory

**FileNotFoundError**
   - Program path doesn't exist
   - Missing program.json manifest
   - Missing kv_prefix.pt file

**RuntimeError**
   - Model loading failures
   - GPU out of memory
   - Generation errors

**Example error handling:**

.. code-block:: python

   import programasweights as paw
   
   try:
       fn = paw.function("yuntian-deng/paw-nonexistent")
   except FileNotFoundError:
       print("Program not found - check the model ID")
   except ValueError as e:
       print(f"Invalid program: {e}")
   
   try:
       result = fn("input text")
   except RuntimeError as e:
       print(f"Execution failed: {e}")

Type Hints
----------

For better IDE support:

.. code-block:: python

   from typing import Union, List, Callable
   import programasweights as paw
   
   # Type hints for program functions
   ProgramFunction = Callable[[Union[str, List[str]]], Union[str, List[str]]]
   
   def load_parser() -> ProgramFunction:
       return paw.function("yuntian-deng/paw-parser")
   
   def process_texts(texts: List[str]) -> List[str]:
       parser = load_parser()
       return parser(texts)

Next: :doc:`examples/text-parsing` 