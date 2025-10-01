Using Pre-trained Programs
===========================

ProgramAsWeights provides a growing library of pre-trained neural programs for common fuzzy tasks. Each program is a compact weight blob that runs locally without API calls.

Available Programs
------------------

All programs are hosted on HuggingFace under the ``yuntian-deng`` organization and can be loaded directly by name.

Text Parsing & Extraction
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Program ID
     - Description
     - Use Case
   * - ``yuntian-deng/paw-quote-extractor``
     - Extract quoted substrings (single/double quotes)
     - Parse dialogue, citations
   * - ``yuntian-deng/paw-option-parser``
     - Parse (A)/(B)/(C) style option blocks
     - Multiple choice questions
   * - ``yuntian-deng/paw-email-extractor``
     - Find email addresses in text
     - Contact info extraction
   * - ``yuntian-deng/paw-url-extractor``
     - Extract and normalize URLs
     - Link processing
   * - ``yuntian-deng/paw-date-normalizer``
     - Convert various date formats to ISO
     - Data cleaning
   * - ``yuntian-deng/paw-answer-extractor``
     - Extract final answers from reasoning
     - LLM output processing

Content Analysis
~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Program ID
     - Description
     - Use Case
   * - ``yuntian-deng/paw-sentiment``
     - Classify text sentiment
     - Review analysis
   * - ``yuntian-deng/paw-bias-detector``
     - Quantify bias and opinion strength
     - Content moderation
   * - ``yuntian-deng/paw-answer-equiv``
     - Check if answers are equivalent
     - LLM evaluation
   * - ``yuntian-deng/paw-spam-detector``
     - Identify spam content
     - Content filtering
   * - ``yuntian-deng/paw-intent-classifier``
     - Classify user intent
     - Chatbot routing

Format Conversion
~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Program ID
     - Description
     - Use Case
   * - ``yuntian-deng/paw-html-cleaner``
     - Strip HTML tags, preserve text
     - Web scraping
   * - ``yuntian-deng/paw-csv-to-json``
     - Convert CSV to structured JSON
     - Data transformation
   * - ``yuntian-deng/paw-json-fixer``
     - Repair malformed JSON
     - Data cleaning
   * - ``yuntian-deng/paw-markdown-parser``
     - Parse Markdown to structured data
     - Documentation processing

Evaluation & Comparison
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Program ID
     - Description
     - Use Case
   * - ``yuntian-deng/paw-answer-equiv``
     - Check answer equivalence beyond exact match
     - Research evaluation
   * - ``yuntian-deng/paw-quality-scorer``
     - Score response quality (1-10)
     - Automated grading
   * - ``yuntian-deng/paw-factual-checker``
     - Assess factual accuracy
     - Content verification
   * - ``yuntian-deng/paw-consistency-checker``
     - Check consistency across responses
     - Multi-turn evaluation

Usage Examples
--------------

Replacing OpenAI API Calls
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Before (expensive, requires internet):**

.. code-block:: python

   import openai
   
   def classify_sentiment(text):
       response = openai.chat.completions.create(
           model="gpt-4",
           messages=[{
               "role": "user", 
               "content": f"Classify sentiment of: {text}"
           }]
       )
       return response.choices[0].message.content

**After (free, local, faster):**

.. code-block:: python

   import programasweights as paw
   
   classify_sentiment = paw.function("yuntian-deng/paw-sentiment")

Research Evaluation Pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Replace manual evaluation with automated programs:

.. code-block:: python

   import programasweights as paw
   
   # Load evaluation programs
   equiv_checker = paw.function("yuntian-deng/paw-answer-equiv")
   quality_scorer = paw.function("yuntian-deng/paw-quality-scorer")
   
   # Evaluate model outputs
   results = []
   for pred, target in zip(predictions, ground_truth):
       equivalent = equiv_checker(f"Pred: {pred}\nTarget: {target}")
       quality = quality_scorer(pred)
       results.append({
           "equivalent": equivalent == "equivalent",
           "quality_score": float(quality)
       })
   
   # Compute metrics
   accuracy = sum(r["equivalent"] for r in results) / len(results)
   avg_quality = sum(r["quality_score"] for r in results) / len(results)

Content Moderation Pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import programasweights as paw
   
   # Load moderation programs
   spam_detector = paw.function("yuntian-deng/paw-spam-detector")
   bias_detector = paw.function("yuntian-deng/paw-bias-detector") 
   sentiment = paw.function("yuntian-deng/paw-sentiment")
   
   def moderate_content(text):
       is_spam = spam_detector(text) == "spam"
       bias_level = bias_detector(text)
       sentiment_score = sentiment(text)
       
       return {
           "approved": not is_spam and bias_level != "high_bias",
           "spam": is_spam,
           "bias": bias_level,
           "sentiment": sentiment_score
       }

Finding the Right Program
-------------------------

**Browse by task type:**

- **Text extraction:** Look for ``*-extractor`` programs
- **Classification:** Look for ``*-classifier`` or ``*-detector`` programs  
- **Conversion:** Look for ``*-converter`` or ``*-to-*`` programs
- **Evaluation:** Look for ``*-checker`` or ``*-scorer`` programs

**Check program descriptions on HuggingFace:**
Visit ``https://huggingface.co/yuntian-deng/paw-{task-name}`` for detailed docs.

**Request new programs:**
If you need a program that doesn't exist, `open an issue <https://github.com/yuntian-deng/programasweights/issues>`_ with your use case.

Performance Characteristics
---------------------------

**Typical performance (on GPU):**
- **Load time:** 2-5 seconds (first time only)
- **Inference:** 10-100ms per example
- **Batch processing:** 5-20ms per example
- **Memory:** 2-4GB VRAM for interpreter

**Compared to API calls:**
- **10-100x faster** than OpenAI API
- **100-1000x cheaper** (no per-token costs)
- **Always available** (no rate limits, no internet required)

Next: :doc:`examples/text-parsing` 