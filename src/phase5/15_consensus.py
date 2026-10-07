"""Lesson 15: majority voting and Borda count for agent proposals."""
from __future__ import annotations

from collections import Counter, defaultdict
from typing import Sequence


def majority_vote(votes: Sequence[str]) -> str:
    if not votes:
        raise ValueError("at least one vote is required")
    counts = Counter(votes)
    return min(counts, key=lambda option: (-counts[option], option))


def borda_count(rankings: Sequence[Sequence[str]]) -> str:
    if not rankings:
        raise ValueError("at least one ranking is required")
    scores: defaultdict[str, int] = defaultdict(int)
    for ranking in rankings:
        for position, option in enumerate(ranking):
            scores[option] += len(ranking) - position - 1
    return min(scores, key=lambda option: (-scores[option], option))


def debate(votes: Sequence[str], rounds: int = 1) -> dict[str, object]:
    if rounds < 1:
        raise ValueError("rounds must be positive")
    winner = majority_vote(votes)
    return {"winner": winner, "rounds": rounds, "counts": dict(Counter(votes))}


def main() -> None:
    print(debate(["RAG", "RAG", "tools", "tools", "RAG"]))


if __name__ == "__main__":
    main()
