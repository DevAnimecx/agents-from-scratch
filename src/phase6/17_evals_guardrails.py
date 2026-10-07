"""Lesson 17: lightweight evals, PII redaction, and a token rate limiter."""
from __future__ import annotations

import re
import time
from dataclasses import dataclass
from typing import Callable, Iterable

EMAIL = re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b")
PHONE = re.compile(r"(?<!\d)(?:\+?\d[\d ()-]{7,}\d)(?!\d)")


def redact_pii(text: str) -> str:
    text = EMAIL.sub("[REDACTED_EMAIL]", text)
    return PHONE.sub("[REDACTED_PHONE]", text)


@dataclass
class RateLimiter:
    capacity: int
    refill_per_second: float
    tokens: float | None = None
    last_check: float = 0.0

    def __post_init__(self) -> None:
        if self.capacity < 1 or self.refill_per_second <= 0:
            raise ValueError("capacity and refill rate must be positive")
        self.tokens = float(self.capacity) if self.tokens is None else self.tokens
        self.last_check = time.monotonic()

    def allow(self, amount: int = 1) -> bool:
        now = time.monotonic()
        self.tokens = min(self.capacity, self.tokens + (now - self.last_check) * self.refill_per_second)
        self.last_check = now
        if self.tokens >= amount:
            self.tokens -= amount
            return True
        return False


def exact_match(expected: str, actual: str) -> float:
    return float(expected.strip().lower() == actual.strip().lower())


def evaluate(cases: Iterable[tuple[str, str]], metric: Callable[[str, str], float] = exact_match) -> dict[str, float]:
    values = [metric(expected, actual) for expected, actual in cases]
    return {"count": float(len(values)), "score": sum(values) / len(values) if values else 0.0}


def main() -> None:
    print(redact_pii("Email me at learner@example.com or call +1 555 010 1234"))
    print(evaluate([("yes", "yes"), ("no", "maybe")]))


if __name__ == "__main__":
    main()
