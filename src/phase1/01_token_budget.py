"""Lesson 01: a transparent FIFO token window, with no framework dependency."""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable

_TOKEN = re.compile(r"\w+|[^\w\s]", re.UNICODE)


def count_tokens(text: str) -> int:
    """Return a deterministic teaching approximation of model token count."""
    return len(_TOKEN.findall(text))


@dataclass(frozen=True)
class Message:
    role: str
    content: str

    @property
    def tokens(self) -> int:
        return count_tokens(self.content) + 1  # one small role/separator overhead


class TokenWindow:
    """Keep the newest messages under a token budget.

    The system message is pinned when possible. All other messages are evicted in
    FIFO order. This is deliberately explicit so an eviction policy can be tested.
    """

    def __init__(self, max_tokens: int, system: str | None = None) -> None:
        if max_tokens < 1:
            raise ValueError("max_tokens must be positive")
        self.max_tokens = max_tokens
        self._system = Message("system", system) if system else None
        self._messages: list[Message] = []

    @property
    def messages(self) -> tuple[Message, ...]:
        return tuple(([self._system] if self._system else []) + self._messages)

    @property
    def token_count(self) -> int:
        return sum(message.tokens for message in self.messages)

    def add(self, role: str, content: str) -> None:
        if not role or not content:
            raise ValueError("role and content are required")
        message = Message(role, content)
        # A single message larger than the budget is retained in truncated form;
        # silently dropping the current user request is a surprising failure mode.
        if message.tokens > self.max_tokens:
            words = content.split()
            keep = max(1, self.max_tokens - 1)
            message = Message(role, " ".join(words[-keep:]))
        self._messages.append(message)
        self._trim()

    def extend(self, messages: Iterable[Message]) -> None:
        for message in messages:
            self.add(message.role, message.content)

    def _trim(self) -> None:
        while len(self._messages) > 1 and self.token_count > self.max_tokens:
            self._messages.pop(0)
        # If the pinned system prompt itself is bigger than the budget, retain it
        # rather than creating an empty prompt; callers can choose a larger budget.
        while self._messages and self.token_count > self.max_tokens:
            self._messages.pop(0)

    def as_prompt(self) -> list[dict[str, str]]:
        return [{"role": m.role, "content": m.content} for m in self.messages]


def demo() -> TokenWindow:
    window = TokenWindow(18, "Answer concisely.")
    for role, text in [
        ("user", "What is retrieval augmented generation?"),
        ("assistant", "It retrieves relevant context before generation."),
        ("user", "How do I test the retriever?"),
        ("assistant", "Use a tiny fixed corpus and assert the top result."),
    ]:
        window.add(role, text)
    return window


def main() -> None:
    window = demo()
    print(f"{window.token_count} tokens in the window")
    for message in window.messages:
        print(f"{message.role}: {message.content}")


if __name__ == "__main__":
    main()
