Quick Start Guide
=================

Get started with ProgramAsWeights in minutes. This guide shows how to use pre-trained neural programs for common fuzzy tasks.

Basic Usage Pattern
-------------------

All ProgramAsWeights follow the same 3-step pattern:

.. code-block:: python

   import programasweights as paw
   
   # 1. Load a program (downloads once, cached forever)
   fn = paw.function("yuntian-deng/paw-text-parser")
   
   # 2. Call it like any Python function
   result = fn("Extract emails from: Contact john@example.com or mary@test.org")
   
   # 3. Get structured output
   print(result)  # → ["john@example.com", "mary@test.org"]

Common Tasks
------------

Text Parsing and Extraction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Extract quoted strings:**

.. code-block:: python

   parser = paw.function("yuntian-deng/paw-quote-extractor")
   text = 'He said "Hello" and then \'Goodbye\'.'
   quotes = parser(text)
   print(quotes)  # → ["Hello", "Goodbye"]

**Parse option blocks:**

.. code-block:: python

   option_parser = paw.function("yuntian-deng/paw-option-parser")
   text = "(A) Red (B) Blue (C) Green"
   options = option_parser(text)
   print(options)  # → [{"label": "A", "text": "Red"}, ...]

**Extract final answers from reasoning:**

.. code-block:: python

   answer_extractor = paw.function("yuntian-deng/paw-answer-extractor")
   text = "Let me think... The calculation is 2+2=4. Final Answer: 4"
   answer = answer_extractor(text)
   print(answer)  # → "4"

Content Analysis
~~~~~~~~~~~~~~~~

**Sentiment analysis:**

.. code-block:: python

   sentiment = paw.function("yuntian-deng/paw-sentiment")
   review = "This product is amazing! Best purchase ever."
   score = sentiment(review)
   print(score)  # → "positive"

**Bias detection:**

.. code-block:: python

   bias_detector = paw.function("yuntian-deng/paw-bias-detector")
   claim = "Technology companies favor young workers"
   text = "The hiring practices clearly show age discrimination..."
   support = bias_detector(f"Claim: {claim}\nText: {text}")
   print(support)  # → "strongly_supporting"

**Answer equivalence (for LLM evaluation):**

.. code-block:: python

   equiv_checker = paw.function("yuntian-deng/paw-answer-equiv")
   pred = "The capital is Washington DC"
   target = "Washington, D.C. is the capital"
   equivalent = equiv_checker(f"Prediction: {pred}\nTarget: {target}")
   print(equivalent)  # → "equivalent"

Format Conversion
~~~~~~~~~~~~~~~~~

**HTML to clean text:**

.. code-block:: python

   html_cleaner = paw.function("yuntian-deng/paw-html-cleaner")
   html = "<p>Hello <strong>world</strong>!</p>"
   clean = html_cleaner(html)
   print(clean)  # → "Hello world!"

**CSV to JSON:**

.. code-block:: python

   csv_converter = paw.function("yuntian-deng/paw-csv-to-json")
   csv = "name,age\nAlice,30\nBob,25"
   json_result = csv_converter(csv)
   print(json_result)  # → [{"name": "Alice", "age": "30"}, ...]

Batch Processing
----------------

All programs accept both single strings and lists:

.. code-block:: python

   parser = paw.function("yuntian-deng/paw-email-extractor")
   
   # Single input
   result = parser("Contact: alice@example.com")
   
   # Batch input (more efficient)
   texts = [
       "Email alice@example.com for info",
       "Reach out to bob@test.org",
       "No emails in this text"
   ]
   results = parser(texts)  # → [["alice@example.com"], ["bob@test.org"], []]

Performance Tips
----------------

**Reuse functions for better performance:**

.. code-block:: python

   # ✅ Good: Load once, use many times
   parser = paw.function("yuntian-deng/paw-parser")
   for text in large_dataset:
       result = parser(text)
   
   # ❌ Avoid: Loading repeatedly
   for text in large_dataset:
       parser = paw.function("yuntian-deng/paw-parser")  # Slow!
       result = parser(text)

**Use batch processing for large datasets:**

.. code-block:: python

   # Process 1000 texts in batches of 32
   batch_size = 32
   parser = paw.function("yuntian-deng/paw-parser")
   
   for i in range(0, len(texts), batch_size):
       batch = texts[i:i+batch_size]
       results.extend(parser(batch))

Next Steps
----------

- :doc:`using-pretrained` - Browse available pre-trained programs
- :doc:`examples/text-parsing` - Detailed examples for text processing
- :doc:`api-reference` - Complete API documentation
- :doc:`training/overview` - Train your own programs (advanced) 