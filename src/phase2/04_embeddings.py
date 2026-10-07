"""Lesson 04: a tiny deterministic embedding model made from token hashing."""
from __future__ import annotations

import hashlib
import re
from collections.abc import Iterable

import numpy as np

_WORD = re.compile(r"[\w']+", re.UNICODE)


def cosine_similarity(left: np.ndarray, right: np.ndarray) -> float:
    left, right = np.asarray(left, dtype=float), np.asarray(right, dtype=float)
    if left.shape != right.shape:
        raise ValueError("vectors must have equal shapes")
    denom = np.linalg.norm(left) * np.linalg.norm(right)
    return float(np.dot(left, right) / denom) if denom else 0.0


class HashingEmbedder:
    """Map words to signed buckets; useful for understanding vector search."""

    def __init__(self, dimension: int = 128) -> None:
        if dimension < 2:
            raise ValueError("dimension must be at least two")
        self.dimension = dimension

    def embed(self, text: str) -> np.ndarray:
        vector = np.zeros(self.dimension, dtype=float)
        for word in _WORD.findall(text.lower()):
            digest = hashlib.blake2b(word.encode(), digest_size=8).digest()
            index = int.from_bytes(digest[:4], "big") % self.dimension
            sign = 1 if digest[4] % 2 else -1
            vector[index] += sign
        norm = np.linalg.norm(vector)
        return vector / norm if norm else vector

    def encode(self, texts: Iterable[str]) -> np.ndarray:
        return np.vstack([self.embed(text) for text in texts])


def main() -> None:
    embedder = HashingEmbedder(32)
    query = embedder.embed("build a retrieval agent")
    for text in ["retrieval augmented generation", "a weather tool", "agent memory"]:
        print(f"{cosine_similarity(query, embedder.embed(text)):.3f}  {text}")


if __name__ == "__main__":
    main()
