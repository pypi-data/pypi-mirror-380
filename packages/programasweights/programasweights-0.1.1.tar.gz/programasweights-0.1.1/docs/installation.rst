Installation
============

ProgramAsWeights requires Python 3.8+ and PyTorch.

Quick Install
-------------

.. code-block:: bash

   pip install programasweights

That's it! The package automatically handles model downloads when you first use a program.

Requirements
------------

**Minimal requirements** (automatically installed):

- ``torch`` - Neural network runtime
- ``transformers`` - Model loading and inference
- ``safetensors`` - Efficient tensor storage

**Optional dependencies** for advanced users:

.. code-block:: bash

   # For training your own models (researchers only)
   pip install programasweights[train]
   
   # For generating new datasets
   pip install programasweights[data]

System Requirements
-------------------

**Memory:**
- **CPU:** 4GB+ RAM recommended
- **GPU:** 8GB+ VRAM for larger models (optional, falls back to CPU)

**Storage:**
- ~2-4GB per interpreter model (downloaded once, cached locally)
- ~100MB per compiled program

**Network:**
- Internet connection for initial model download
- Offline execution after download

Verify Installation
-------------------

.. code-block:: python

   import programasweights as paw
   print(paw.__version__)  # Should print version number

**Test with a dummy program:**

.. code-block:: python

   # Create a test program (uses dummy compiler for demo)
   paw.compile_dummy("test.weights", seed=42)
   
   # Load and run it
   fn = paw.function("test.weights")
   print(fn("hello world"))

GPU Setup (Optional)
--------------------

ProgramAsWeights automatically uses GPU if available. To force CPU-only:

.. code-block:: bash

   export PROGRAMASWEIGHTS_DEVICE=cpu

To verify GPU usage:

.. code-block:: python

   import torch
   print(f"CUDA available: {torch.cuda.is_available()}")
   print(f"Device: {torch.cuda.get_device_name() if torch.cuda.is_available() else 'CPU'}")

Troubleshooting
---------------

**Common issues:**

- **"No module named 'programasweights'"** → Run ``pip install programasweights``
- **Model download fails** → Check internet connection and disk space
- **Out of memory** → Set ``PROGRAMASWEIGHTS_DEVICE=cpu`` or use smaller models
- **Slow execution** → Enable GPU or use smaller input batches

See :doc:`troubleshooting` for detailed solutions. 