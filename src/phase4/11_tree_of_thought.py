"""Lesson 11: breadth-first search over scored thought branches."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable


@dataclass(frozen=True)
class Thought:
    text: str
    score: float = 0.0


def tree_search(root: Thought, expand: Callable[[Thought], Iterable[Thought]], depth: int = 2, width: int = 3) -> Thought:
    if depth < 0 or width < 1:
        raise ValueError("depth must be non-negative and width must be positive")
    frontier = [root]
    best = root
    for _ in range(depth):
        candidates = [child for node in frontier for child in expand(node)]
        if not candidates:
            break
        frontier = sorted(candidates, key=lambda thought: thought.score, reverse=True)[:width]
        best = max([best, *frontier], key=lambda thought: thought.score)
    return best


def main() -> None:
    root = Thought("choose a plan")
    def expand(node: Thought) -> list[Thought]:
        return [Thought(node.text + " -> careful", node.score + 0.8), Thought(node.text + " -> fast", node.score + 0.3)]
    print(tree_search(root, expand, depth=2).text)


if __name__ == "__main__":
    main()
