"""Small, deterministic benchmark harness for lesson regressions."""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable


@dataclass(frozen=True)
class BenchmarkCase:
    prompt: str
    expected: str


def load_cases(path: str | Path) -> list[BenchmarkCase]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return [BenchmarkCase(item["prompt"], item["expected"]) for item in data]


def run(cases: Iterable[BenchmarkCase], answer: Callable[[str], str]) -> dict[str, float]:
    cases = list(cases)
    correct = sum(answer(case.prompt).strip().lower() == case.expected.strip().lower() for case in cases)
    return {"count": float(len(cases)), "correct": float(correct), "accuracy": correct / len(cases) if cases else 0.0}


if __name__ == "__main__":
    path = Path(__file__).parent / "datasets" / "smoke.json"
    print(run(load_cases(path), lambda prompt: "rag" if "retrieval" in prompt else "agent"))
