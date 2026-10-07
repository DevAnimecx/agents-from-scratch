"""Lesson 06: brute-force vector, lexical, hybrid, and MMR retrieval."""
from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass
from importlib import import_module

import numpy as np

_embeddings = import_module("phase2.04_embeddings")
HashingEmbedder = _embeddings.HashingEmbedder
cosine_similarity = _embeddings.cosine_similarity


@dataclass(frozen=True)
class SearchResult:
    text: str
    score: float


def bm25(query: str, documents: list[str], k1: float = 1.5, b: float = 0.75) -> list[SearchResult]:
    tokenized = [re.findall(r"\w+", doc.lower()) for doc in documents]
    query_terms = set(re.findall(r"\w+", query.lower()))
    average_length = sum(map(len, tokenized)) / max(1, len(tokenized))
    scores = []
    for words, document in zip(tokenized, documents):
        counts = Counter(words)
        score = 0.0
        for term in query_terms:
            frequency = counts[term]
            if not frequency:
                continue
            df = sum(term in other for other in tokenized)
            idf = math.log(1 + (len(documents) - df + 0.5) / (df + 0.5))
            score += idf * frequency * (k1 + 1) / (frequency + k1 * (1 - b + b * len(words) / max(1, average_length)))
        scores.append(SearchResult(document, score))
    return sorted(scores, key=lambda result: result.score, reverse=True)


def vector_search(query: str, documents: list[str], k: int = 3, dimension: int = 128) -> list[SearchResult]:
    embedder = HashingEmbedder(dimension)
    query_vector = embedder.embed(query)
    return sorted((SearchResult(doc, cosine_similarity(query_vector, embedder.embed(doc))) for doc in documents),
                  key=lambda result: result.score, reverse=True)[:k]


def hybrid_search(query: str, documents: list[str], k: int = 3) -> list[SearchResult]:
    dense = {r.text: r.score for r in vector_search(query, documents, len(documents))}
    lexical = {r.text: r.score for r in bm25(query, documents)}
    def normalize(values: dict[str, float]) -> dict[str, float]:
        high = max(values.values(), default=0.0)
        return {key: value / high if high else 0.0 for key, value in values.items()}
    dense_scores, lexical_scores = normalize(dense), normalize(lexical)
    return sorted((SearchResult(doc, 0.6 * dense_scores[doc] + 0.4 * lexical_scores[doc]) for doc in documents),
                  key=lambda result: result.score, reverse=True)[:k]


def mmr(query_vector: np.ndarray, document_vectors: np.ndarray, k: int = 3, diversity: float = 0.5) -> list[int]:
    if not 0 <= diversity <= 1:
        raise ValueError("diversity must be between zero and one")
    selected: list[int] = []
    remaining = list(range(len(document_vectors)))
    while remaining and len(selected) < k:
        def score(index: int) -> float:
            relevance = cosine_similarity(query_vector, document_vectors[index])
            redundancy = max((cosine_similarity(document_vectors[index], document_vectors[j]) for j in selected), default=0.0)
            return (1 - diversity) * relevance - diversity * redundancy
        winner = max(remaining, key=score)
        selected.append(winner)
        remaining.remove(winner)
    return selected


def main() -> None:
    docs = ["Python agents use tools", "RAG retrieves documents", "Tools can retrieve documents"]
    for result in hybrid_search("retrieve documents", docs):
        print(f"{result.score:.3f}  {result.text}")


if __name__ == "__main__":
    main()
