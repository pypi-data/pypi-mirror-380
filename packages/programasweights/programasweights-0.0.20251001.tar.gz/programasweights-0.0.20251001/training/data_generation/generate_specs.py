#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sqlite3
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

from openai import OpenAI
from tqdm.auto import tqdm


@dataclass
class Cache:
    conn: sqlite3.Connection

    @staticmethod
    def open(path: str) -> "Cache":
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        conn = sqlite3.connect(path)
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS cache (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.commit()
        return Cache(conn)

    def get(self, key: str) -> Optional[str]:
        cur = self.conn.execute("SELECT value FROM cache WHERE key = ?", (key,))
        row = cur.fetchone()
        return row[0] if row else None

    def set(self, key: str, value: str) -> None:
        self.conn.execute("INSERT OR REPLACE INTO cache(key, value) VALUES(?, ?)", (key, value))
        self.conn.commit()


def stable_hash(obj: Any) -> str:
    data = json.dumps(obj, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def ensure_openai_client(api_key: Optional[str]) -> Any:
    if OpenAI is None:
        raise RuntimeError("openai python package not installed. Run: pip install openai")
    key = api_key or os.environ.get("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("Missing OPENAI_API_KEY. Export it or pass --openai-api-key.")
    return OpenAI(api_key=key)


def build_prompts(
    *,
    category: str,
    num: int,
    include_examples: bool = False,
) -> Dict[str, str]:
    base_dir = _default_templates_dir()
    sys_path = os.path.join(base_dir, "specs_system.txt")
    
    # Choose user template based on whether examples are requested
    if include_examples:
        usr_path = os.path.join(base_dir, "specs_user_with_examples.txt")
    else:
        usr_path = os.path.join(base_dir, "specs_user.txt")

    system_template = _read_file(sys_path)
    user_template = _read_file(usr_path)

    mapping = {
        "category": category,
        "num": str(num),
    }
    system_prompt = _render_template(system_template, mapping)
    user_prompt = _render_template(user_template, mapping)
    return {"system": system_prompt, "user": user_prompt}


def request_specs(
    client: Any,
    model: str,
    system_prompt: str,
    user_prompt: str,
    temperature: float,
    *,
    disable_cache: bool,
    cache_salt: str,
    enforce_json: bool,
) -> List[Dict[str, str]]:
    response_format = {"type": "json_object"} if enforce_json else None
    req = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": temperature,
        "response_format": response_format,
        "_cache_salt": cache_salt,
    }
    key = stable_hash(req)
    return _cached_response_specs(client, req, key, disable_cache=disable_cache)


def _cached_response_specs(client: Any, req: Dict[str, Any], key: str, *, disable_cache: bool, max_retries: int = 3) -> List[Dict[str, str]]:
    cache_path = os.environ.get("DATA_SYNTH_CACHE_DB", "data/cache.sqlite3")
    cache = Cache.open(cache_path)

    if not disable_cache:
        cached = cache.get(key)
        if cached is not None:
            payload = json.loads(cached)
            return payload["specs"]

    # Retry logic for API errors
    for attempt in range(max_retries):
        try:
            # Use Chat Completions API; let exceptions raise
            kwargs = {
                "model": req["model"],
                "messages": req["messages"],
                "temperature": req.get("temperature", 0.7),
            }
            if req.get("response_format") is not None:
                kwargs["response_format"] = req["response_format"]
            resp = client.chat.completions.create(**kwargs)
            content_text = resp.choices[0].message.content
            if not content_text:
                raise RuntimeError("Empty response content from model")

            # Parse JSON directly (no extraction needed with enforce_json)
            data = json.loads(content_text)
            
            # Check for API error responses
            if isinstance(data, dict) and "error" in data:
                error_msg = data["error"]
                if "malformed" in error_msg.lower() or "too long" in error_msg.lower():
                    raise RuntimeError(f"API error (attempt {attempt+1}/{max_retries}): {error_msg}")
                else:
                    raise RuntimeError(f"API error: {error_msg}")
            
            if not isinstance(data, dict) or "specs" not in data or not isinstance(data["specs"], list):
                raise RuntimeError(f"Malformed JSON structure: expected dict with 'specs' list. Got: {data}")

            if not disable_cache:
                cache.set(key, json.dumps(data, ensure_ascii=False))
            return data["specs"]
            
        except Exception as e:
            if attempt == max_retries - 1:
                # Last attempt failed, re-raise
                raise e
            else:
                print(f"Attempt {attempt+1} failed: {e}. Retrying...")
                import time
                time.sleep(2 ** attempt)  # Exponential backoff
    
    # Should never reach here
    raise RuntimeError("All retry attempts failed")


def write_specs(path: str, specs: List[Dict[str, str]], fmt: str, append: bool = False) -> None:
    os.makedirs(os.path.dirname(os.path.abspath(path)) or ".", exist_ok=True)
    mode = "a" if append else "w"
    if fmt == "txt":
        with open(path, mode, encoding="utf-8") as f:
            for s in specs:
                f.write(s.get("spec", "").strip() + "\n")
    elif fmt == "jsonl":
        with open(path, mode, encoding="utf-8") as f:
            for s in specs:
                f.write(json.dumps({
                    "spec": s.get("spec").strip(),
                    "category": s.get("category"),
                    "difficulty": s.get("difficulty"),
                    "includes_examples": s.get("includes_examples"),
                }, ensure_ascii=False) + "\n")
    else:
        raise SystemExit(f"Unsupported format: {fmt}")


def _default_templates_dir() -> str:
    return os.path.join(os.path.dirname(__file__), "templates")


def _read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _render_template(text: str, mapping: Dict[str, str]) -> str:
    out = text
    for k, v in mapping.items():
        out = out.replace(f"{{{{{k}}}}}", v)
    return out


def _generate_batch_worker(args_tuple) -> List[Dict[str, str]]:
    """Worker function for parallel batch processing"""
    client, model, system_prompt, user_prompt, temperature, disable_cache, cache_salt, enforce_json = args_tuple
    return request_specs(
        client=client,
        model=model,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        temperature=temperature,
        disable_cache=disable_cache,
        cache_salt=cache_salt,
        enforce_json=enforce_json,
    )


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Generate function specs with OpenAI and cache in SQLite.")
    parser.add_argument("--out", default="data/specs_morecategories_81920examples.jsonl", help="Output path (.txt for one-per-line or .jsonl)")
    parser.add_argument("--num", type=int, default=64, help="Number of specs to generate")
    parser.add_argument("--categories", nargs="+", default=[
        # Core text processing
        "parsing_text",
        "option_block_parsing", 
        "final_answer_extraction",
        "format_conversion",
        "regex_hard",
        "date_time_normalization",
        "number_normalization",
        "unit_conversion",
        "key_value_extraction",
        "table_parsing",
        "url_query_parsing",
        "json_fixup",
        "markdown_structuring",
        "html_text_cleanup",
        "log_parsing",
        
        # Academic & Bibliography Management
        "bibtex_normalization",
        "conference_name_standardization", 
        "journal_name_normalization",
        "author_name_standardization",
        "bibtex_generation_from_text",
        "citation_format_conversion",
        "bibtex_capitalization_fixing",
        "doi_extraction_and_formatting",
        "publication_venue_disambiguation",
        "reference_deduplication",
        "citation_style_conversion",
        "academic_title_normalization",
        "publication_year_extraction",
        "page_number_standardization",
        "isbn_issn_validation",
        "arxiv_id_extraction",
        "google_scholar_parsing",
        "pubmed_citation_processing",
        "latex_citation_cleanup",
        
        # Natural Language Inference & Reasoning
        "textual_entailment",
        "contradiction_detection",
        "premise_conclusion_analysis",
        "logical_inference",
        "causal_reasoning",
        "temporal_reasoning",
        "spatial_reasoning",
        "numerical_reasoning",
        "commonsense_inference",
        "analogical_reasoning",
        
        # Traditional NLP Tasks
        "named_entity_recognition",
        "relation_extraction",
        "coreference_resolution",
        "dependency_parsing_interpretation",
        "semantic_role_labeling",
        "word_sense_disambiguation",
        "text_summarization",
        "question_answering",
        "reading_comprehension",
        "information_retrieval",
        "document_classification",
        "topic_modeling_interpretation",
        "keyword_extraction",
        "phrase_extraction",
        "collocation_detection",
        
        # Fuzzy classification (hard to specify precisely)
        "sentiment_analysis",
        "review_classification", 
        "content_quality_assessment",
        "spam_detection",
        "intent_classification",
        "topic_categorization",
        "urgency_detection",
        "formality_assessment",
        "writing_style_classification",
        "language_detection",
        
        # Reasoning and answer extraction
        "reasoning_step_extraction",
        "final_answer_identification",
        "explanation_parsing",
        "step_by_step_breakdown",
        "conclusion_extraction",
        "evidence_identification",
        "assumption_detection",
        "logical_flow_parsing",
        
        # Robustness to variations (fuzzy matching)
        "typo_tolerant_parsing",
        "format_agnostic_extraction",
        "noise_robust_processing",
        "case_insensitive_matching",
        "whitespace_tolerant_parsing",
        "synonym_aware_extraction",
        "abbreviation_expansion",
        "informal_language_processing",
        
        # Content understanding
        "semantic_similarity",
        "paraphrase_detection",
        "contradiction_identification",
        "relevance_scoring",
        "completeness_assessment",
        "coherence_evaluation",
        
        # Content Safety & Quality
        "toxicity_detection",
        "hate_speech_identification",
        "dog_whistle_detection",
        "offensive_content_classification",
        "inappropriate_content_flagging",
        "grammaticality_checking",
        "fluency_assessment",
        "coherence_scoring",
        "naturalness_evaluation",
        "style_appropriateness",
        "register_detection",
        
        # Format Validation & Compliance
        "format_adherence_checking",
        "schema_compliance_validation",
        "template_matching",
        "structure_validation",
        "pattern_conformance",
        "format_specification_checking",
        "data_type_validation",
        "regex_pattern_matching",
        "constraint_verification",
        "protocol_compliance",
        
        # LLM evaluation and comparison
        "answer_equivalence_checking",
        "response_quality_scoring",
        "factual_accuracy_assessment",
        "completeness_evaluation",
        "relevance_judgment",
        "hallucination_detection",
        "consistency_checking",
        "ground_truth_comparison",
        "automated_grading",
        "rubric_based_evaluation",
        
        # Bias and opinion analysis
        "bias_quantification",
        "opinion_strength_measurement",
        "claim_support_analysis",
        "stance_detection",
        "political_leaning_assessment",
        "cultural_bias_identification",
        "gender_bias_detection",
        "racial_bias_analysis",
        "ideological_slant_measurement",
        "neutrality_assessment",
        
        # HTML and web content processing
        "html_tag_removal",
        "html_text_extraction",
        "web_scraping_cleanup",
        "html_attribute_extraction",
        "link_extraction",
        "image_alt_text_extraction",
        "table_extraction_from_html",
        "form_data_parsing",
        "css_selector_based_extraction",
        "html_structure_analysis",
        
        # Linguistic analysis (simple concepts, hard implementation)
        "part_of_speech_counting",
        "noun_verb_counting",
        "sentence_complexity_scoring",
        "readability_assessment",
        "grammar_error_detection",
        "word_frequency_analysis",
        "syllable_counting",
        "phonetic_analysis",
        "morphological_analysis",
        "syntactic_pattern_detection",
        
        # PII & Privacy
        "pii_removal",
        "pii_masking", 
        "data_anonymization",
        "sensitive_data_detection",
        
        # Business logic & constraints
        "constraint_satisfaction",
        "preference_ranking",
        "content_filtering",
        "policy_compliance",
        "data_validation",
        "schema_enforcement",
        "business_rule_application",
        "conditional_processing",
        "threshold_based_decisions",
        "multi_criteria_selection",
        
        # Integration with existing code
        "api_response_parsing",
        "config_file_processing",
        "error_message_interpretation",
        "log_analysis",
        "input_sanitization",
        "output_formatting",
        "data_transformation_pipelines",
        "batch_processing_logic",
    ], help="Categories to cover")
    parser.add_argument("--model", default="gpt-5-mini", help="OpenAI model name")
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--openai-api-key", help="API key (or set OPENAI_API_KEY)")
    parser.add_argument("--append", action="store_true", help="Append to output file")
    parser.add_argument("--batch-size", type=int, default=8, help="Specs requested per API call (also affects caching)")
    parser.add_argument("--disable-cache", action="store_true", help="Bypass SQLite cache (always call API)")
    parser.add_argument("--seed", type=int, default=42, help="Random seed to tag cache keys and prompts for this run")
    parser.add_argument("--format", choices=["jsonl", "txt"], default="jsonl", help="Output format (default jsonl)")
    parser.add_argument("--enforce-json", action="store_true", default=True, help="Force model to return a JSON object via response_format")
    parser.add_argument("--workers", type=int, default=1, help="Number of parallel workers for API calls")
    args = parser.parse_args(argv)

    client = ensure_openai_client(args.openai_api_key)

    # Calculate specs per category for balanced distribution
    num_categories = len(args.categories)
    specs_per_category = max(1, args.num // num_categories)
    specs_per_category = max(1, args.num // (num_categories-1))
    print ('Reducing specs_per_category by 1 to match cache!')
    half_specs = max(1, specs_per_category // 2)
    
    all_specs: List[Dict[str, str]] = []
    
    # Generate specs for each category (both with and without examples)
    for category in args.categories:
        # Generate specs without examples (preserves old cache)
        for include_examples in [False, True]:
            remaining = half_specs
            batch_size = max(1, int(args.batch_size))
            total_batches = (remaining + batch_size - 1) // batch_size
            
            run_id = str(args.seed if args.seed is not None else int(time.time() * 1000))
            
            example_suffix = "_with_examples" if include_examples else ""
            
            if args.workers == 1:
                # Sequential processing
                pbar = tqdm(total=half_specs, desc=f"Generating ({category}{example_suffix})", unit="spec")
                batch_index = 1
                while remaining > 0:
                    take = min(batch_size, remaining)
                    batch_prompts = build_prompts(
                        category=category,
                        num=take,
                        include_examples=include_examples,
                    )
                    cache_salt = f"run:{run_id}|category:{category}|batch:{batch_index}"
                    specs = request_specs(
                        client,
                        model=args.model,
                        system_prompt=batch_prompts["system"],
                        user_prompt=batch_prompts["user"],
                        temperature=args.temperature,
                        disable_cache=args.disable_cache,
                        cache_salt=cache_salt,
                        enforce_json=args.enforce_json,
                    )
                    # Add includes_examples field to each spec
                    for spec in specs:
                        if isinstance(spec, dict):
                            spec["includes_examples"] = include_examples
                    all_specs.extend(specs)
                    remaining -= len(specs)
                    pbar.update(len(specs))
                    batch_index += 1
                pbar.close()
            else:
                # Parallel processing
                with ThreadPoolExecutor(max_workers=args.workers) as executor:
                    futures = []
                    batch_index = 1
                    temp_remaining = remaining
                    while temp_remaining > 0:
                        take = min(batch_size, temp_remaining)
                        batch_prompts = build_prompts(
                            category=category,
                            num=take,
                            include_examples=include_examples,
                        )
                        cache_salt = f"run:{run_id}|category:{category}|batch:{batch_index}"
                        args_tuple = (
                            client, args.model, batch_prompts["system"], batch_prompts["user"],
                            args.temperature, args.disable_cache, cache_salt, args.enforce_json
                        )
                        future = executor.submit(_generate_batch_worker, args_tuple)
                        futures.append((future, take))
                        temp_remaining -= take
                        batch_index += 1
                    
                    pbar = tqdm(total=half_specs, desc=f"Generating ({category}{example_suffix})", unit="spec")
                    for future, expected_count in futures:
                        specs = future.result()
                        # Add includes_examples field to each spec
                        for spec in specs:
                            if isinstance(spec, dict):
                                spec["includes_examples"] = include_examples
                        all_specs.extend(specs)
                        pbar.update(len(specs))
                    pbar.close()

    # Deduplicate by spec text
    seen: set[str] = set()
    uniq_specs: List[Dict[str, str]] = []
    num_invalid = 0
    for s in all_specs:
        # Debug unexpected structure
        if not isinstance(s, dict):
            print(f"WARNING: spec item is {type(s)}, expected dict. Value: {s}")
            # If it's a list, try to flatten
            #import pdb; pdb.set_trace()
            num_invalid += 1
            continue
        if 'spec' not in s:
            print(f"WARNING: spec is missing from {s}")
            #import pdb; pdb.set_trace()
            num_invalid += 1
            continue
        if 'category' not in s:
            print(f"WARNING: category is missing from {s}")
            #import pdb; pdb.set_trace()
            num_invalid += 1
            continue
        if 'difficulty' not in s:
            #print(f"WARNING: difficulty is missing from {s}")
            #import pdb; pdb.set_trace()
            num_invalid += 1
            continue
        text = s.get("spec", "").strip()
        if text and text not in seen:
            seen.add(text)
            uniq_specs.append(s)
    print(f"WARNING: {num_invalid} invalid specs found")
    fmt = args.format
    write_specs(args.out, uniq_specs, fmt=fmt, append=args.append)
    print(f"Collected {len(all_specs)} specs across {len(args.categories)} categories (both with/without examples); unique {len(uniq_specs)} written to {args.out}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main()) 
