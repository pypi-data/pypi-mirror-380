from collections import defaultdict
import json
import time
from typing import Any, Dict, List

from bs4 import BeautifulSoup
from prefect import get_run_logger
from transformers import (
    pipeline,
    AutoModelForSequenceClassification,
    AutoTokenizer,
)


class SentimentAnalyzer:

    def __init__(self):

        self.logger = get_run_logger()
        model_name = "oliverguhr/german-sentiment-bert"

        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSequenceClassification.from_pretrained(model_name)

        self.nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

        super().__init__()

    def analyze_sentiment_batch(
        self,
        records: List[Dict[str, Any]],
        sentiment_analysis_fields: List[str] | None,
        *,
        max_plain_len: int = 512,
        chunk_len: int = 512,
        add_distribution: bool = True,
        add_counts: bool = True,
        json_serialize_stats: bool = True,
    ) -> List[Dict[str, Any]]:
        """
        Enrich a batch of records in place with sentiment columns:
          - plain_html_<field>
          - <field>__sentiment_label
          - <field>__sentiment_score
          - (optional) <field>__sentiment_distribution_json, <field>__sentiment_counts_json

        Notes:
          - Expects records already chunked at dataset level (outer batching).
          - Still chunks long texts internally into pieces of 'chunk_len' characters.
        """
        if not sentiment_analysis_fields:
            self.logger.warning(
                "No sentiment analysis fields provided. Skipping sentiment analysis."
            )
            return records

        start_time = time.time()
        total = len(records)

        for idx, element in enumerate(records, start=1):
            for field in sentiment_analysis_fields:
                # Source may be nested like {"Value": "<html>..."}, keep compatibility with your old shape
                src = element.get(field)
                html = None
                if isinstance(src, dict):
                    html = src.get("Value")
                elif isinstance(src, str):
                    html = src

                if not html:
                    continue

                # Extract plain text from HTML
                soup = BeautifulSoup(html, "html.parser")
                text = soup.get_text(separator=" ", strip=True)
                if not text:
                    continue

                # Store truncated plain text (for auditing / lightweight BI)
                element[f"plain_html_{field.lower()}"] = text[:max_plain_len]

                # Chunk long text into <= chunk_len characters (keeps old behavior)
                chunks = [
                    text[i : i + chunk_len] for i in range(0, len(text), chunk_len)
                ]

                if not chunks:
                    continue

                sentiments = self.nlp(
                    chunks
                )  # returns list of {"label": ..., "score": ...}

                # Aggregate per label
                label_scores = defaultdict(float)
                label_counts = defaultdict(int)
                for s in sentiments:
                    label = s["label"]
                    label_scores[label] += float(s["score"])
                    label_counts[label] += 1

                if not label_scores:
                    continue

                average_scores = {
                    label: (label_scores[label] / label_counts[label])
                    for label in label_scores
                }
                dominant_label, dominant_score = max(
                    average_scores.items(), key=lambda x: x[1]
                )

                # Flat, DB-friendly columns
                element[f"{field}__sentiment_label"] = dominant_label
                element[f"{field}__sentiment_score"] = float(dominant_score)

                if add_distribution:
                    val = (
                        average_scores
                        if not json_serialize_stats
                        else json.dumps(average_scores, ensure_ascii=False)
                    )
                    element[f"{field}__sentiment_distribution_json"] = val
                if add_counts:
                    val = (
                        dict(label_counts)
                        if not json_serialize_stats
                        else json.dumps(label_counts, ensure_ascii=False)
                    )
                    element[f"{field}__sentiment_counts_json"] = val

                # Drop the big original HTML field in the curated output (keeps raw table untouched)
                element.pop(field, None)

            if idx % 1000 == 0 or idx == total:
                elapsed = time.time() - start_time
                self.logger.info(
                    f"[sentiment analysis] Processed {idx:,}/{total:,} ({idx/total:.2%}) - elapsed: {elapsed/60:.1f} min"
                )

        return records
