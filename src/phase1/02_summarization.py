"""Lesson 02: compress old conversation turns into a durable summary."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol


@dataclass(frozen=True)
class Message:
    role: str
    content: str

    @property
    def tokens(self) -> int:
        return len(self.content.split()) + 1


class Summarizer(Protocol):
    def __call__(self, previous_summary: str, turns: list[Message]) -> str: ...


def deterministic_summary(previous_summary: str, turns: list[Message]) -> str:
    """Offline fallback: keep the first sentence of each turn.

    A real local model (for example Ollama) can implement the same callable
    contract. Keeping the protocol tiny makes the lesson provider-independent.
    """
    snippets = []
    if previous_summary:
        snippets.append(previous_summary)
    for turn in turns:
        sentence = turn.content.strip().split(".", 1)[0].strip()
        if sentence:
            snippets.append(f"{turn.role}: {sentence}")
    return ". ".join(snippets)[:1200]


@dataclass
class SummarizationChain:
    max_tokens: int = 80
    keep_recent: int = 2
    summarizer: Summarizer = deterministic_summary
    summary: str = ""
    recent: list[Message] = field(default_factory=list)

    def add(self, role: str, content: str) -> None:
        self.recent.append(Message(role, content))
        if self._recent_tokens() > self.max_tokens:
            cutoff = max(1, len(self.recent) - self.keep_recent)
            old, self.recent = self.recent[:cutoff], self.recent[cutoff:]
            self.summary = self.summarizer(self.summary, old)

    def _recent_tokens(self) -> int:
        return sum(message.tokens for message in self.recent)

    def prompt(self) -> list[dict[str, str]]:
        messages: list[dict[str, str]] = []
        if self.summary:
            messages.append({"role": "system", "content": f"Conversation summary: {self.summary}"})
        messages.extend({"role": m.role, "content": m.content} for m in self.recent)
        return messages


def ollama_summarizer(model: str = "llama3.2") -> Summarizer:
    """Return an optional Ollama adapter; import the SDK only when requested."""
    try:
        import ollama  # type: ignore
    except ImportError as exc:
        raise RuntimeError("Install the lesson-02 extra or use deterministic_summary") from exc

    def summarize(previous_summary: str, turns: list[Message]) -> str:
        transcript = "\n".join(f"{t.role}: {t.content}" for t in turns)
        response = ollama.chat(model=model, messages=[{
            "role": "user",
            "content": f"Summarize this conversation in 80 words. Existing summary: {previous_summary}\n{transcript}",
        }])
        return response["message"]["content"].strip()

    return summarize


def main() -> None:
    chain = SummarizationChain(max_tokens=20, keep_recent=2)
    for role, text in [("user", "I am building a RAG tutor."), ("assistant", "Start with a tiny corpus."),
                       ("user", "Remember that citations matter."), ("assistant", "Use source IDs in every result.")]:
        chain.add(role, text)
    print(chain.prompt())


if __name__ == "__main__":
    main()
