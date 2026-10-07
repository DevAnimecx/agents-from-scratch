"""Lesson 03: persistent long-term memory with NumPy cosine similarity."""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np


@dataclass
class Memory:
    text: str
    vector: list[float]
    metadata: dict[str, str]


class VectorMemory:
    def __init__(self, dimension: int) -> None:
        if dimension < 1:
            raise ValueError("dimension must be positive")
        self.dimension = dimension
        self.items: list[Memory] = []

    def add(self, text: str, vector: np.ndarray | list[float], **metadata: str) -> None:
        array = np.asarray(vector, dtype=float)
        if array.shape != (self.dimension,):
            raise ValueError(f"expected vector shape ({self.dimension},), got {array.shape}")
        self.items.append(Memory(text, array.tolist(), metadata))

    def search(self, query: np.ndarray | list[float], k: int = 3) -> list[tuple[Memory, float]]:
        if k < 1:
            return []
        q = np.asarray(query, dtype=float)
        if q.shape != (self.dimension,):
            raise ValueError(f"expected query shape ({self.dimension},), got {q.shape}")
        q_norm = np.linalg.norm(q)
        scored: list[tuple[Memory, float]] = []
        for item in self.items:
            v = np.asarray(item.vector)
            denom = q_norm * np.linalg.norm(v)
            score = float(np.dot(q, v) / denom) if denom else 0.0
            scored.append((item, score))
        return sorted(scored, key=lambda pair: pair[1], reverse=True)[:k]

    def save(self, path: str | Path) -> None:
        payload = {"dimension": self.dimension, "items": [asdict(item) for item in self.items]}
        Path(path).write_text(json.dumps(payload, indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: str | Path) -> "VectorMemory":
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        memory = cls(int(payload["dimension"]))
        memory.items = [Memory(**item) for item in payload["items"]]
        return memory


def main() -> None:
    memory = VectorMemory(3)
    memory.add("RAG retrieves context", [1, 0, 0], topic="rag")
    memory.add("Agents call tools", [0, 1, 0], topic="tools")
    for item, score in memory.search([0.9, 0.1, 0], k=2):
        print(f"{score:.3f}  {item.text}")


if __name__ == "__main__":
    main()
