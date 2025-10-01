ProgramAsWeights Documentation
==============================

**Programs as small weight blobs; a fixed interpreter runs them.**

ProgramAsWeights (PAW) is a new programming paradigm where fuzzy functions—like "determine if a review is positive" or "extract the final answer from reasoning text"—are represented as compact neural weight blobs that execute locally without external API calls.

Quick Start
-----------

Install and use a pre-trained program in 3 lines:

.. code-block:: python

   import programasweights as paw
   
   # Load a pre-trained program for parsing options
   fn = paw.function("yuntian-deng/paw-option-parser")
   
   # Use it like any Python function
   result = fn("(A) cat (B) dog (C) both (A) and (B)")
   print(result)  # → ["(A) cat", "(B) dog", "(C) both (A) and (B)"]

No internet connection required after download. No API keys. No external dependencies.

Why ProgramAsWeights?
--------------------

**Replace expensive LLM API calls** with lightweight local execution:

- ❌ **Before:** ``openai.chat.completions.create(...)`` - $$$, internet-dependent, fragile
- ✅ **After:** ``paw.function("task")("input")`` - local, fast, reproducible

**Perfect for fuzzy functions** that are conceptually simple but hard to code precisely:

- Sentiment analysis, bias detection, answer extraction
- HTML cleaning, format conversion, typo-tolerant parsing  
- Evaluation tasks like checking answer equivalence
- Linguistic analysis (counting nouns/verbs, readability scoring)

Documentation Sections
======================

.. toctree::
   :maxdepth: 2
   :caption: User Guide:

   installation
   quickstart
   using-pretrained
   api-reference

.. toctree::
   :maxdepth: 2
   :caption: Examples:

   examples/text-parsing
   examples/evaluation-tasks
   examples/bias-analysis
   examples/html-processing

.. toctree::
   :maxdepth: 1
   :caption: Advanced (Researchers):

   training/overview
   training/custom-datasets
   training/model-architecture
   
.. toctree::
   :maxdepth: 1
   :caption: Reference:

   api
   troubleshooting
   contributing

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

