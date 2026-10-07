"""Lesson 12: generate, critique, revise—bounded and observable."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Revision:
    answer: str
    critique: str
    round: int


def reflect(
    task: str,
    generate: Callable[[str, str], str],
    critique: Callable[[str, str], str],
    revise: Callable[[str, str], str],
    rounds: int = 2,
) -> list[Revision]:
    if rounds < 1:
        raise ValueError("rounds must be positive")
    answer = generate(task, "")
    history = []
    for number in range(1, rounds + 1):
        feedback = critique(task, answer)
        history.append(Revision(answer, feedback, number))
        if feedback.strip().lower() in {"ok", "pass", "accepted"}:
            break
        answer = revise(answer, feedback)
    return history


def main() -> None:
    history = reflect("write a short greeting", lambda task, _: "Hello.", lambda _, answer: "Add warmth." if len(answer) < 12 else "ok", lambda answer, _: answer + " Welcome!")
    print(history[-1].answer)


if __name__ == "__main__":
    main()
