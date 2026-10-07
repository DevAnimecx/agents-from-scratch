"""Lesson 05: compare fixed, recursive, and semantic chunking."""
from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Chunk:
    text: str
    start: int
    end: int


def fixed_chunks(text: str, size: int = 400, overlap: int = 40) -> list[Chunk]:
    if size < 1 or not 0 <= overlap < size:
        raise ValueError("require size > 0 and 0 <= overlap < size")
    chunks, start = [], 0
    while start < len(text):
        end = min(len(text), start + size)
        chunks.append(Chunk(text[start:end], start, end))
        if end == len(text):
            break
        start = end - overlap
    return chunks


def recursive_chunks(text: str, size: int = 400) -> list[Chunk]:
    """Split on paragraph, sentence, then whitespace boundaries."""
    if size < 1:
        raise ValueError("size must be positive")
    pieces = [p.strip() for p in re.split(r"\n\s*\n|(?<=[.!?])\s+", text) if p.strip()]
    chunks: list[Chunk] = []
    cursor = 0
    current = ""
    current_start = 0
    for piece in pieces:
        if current and len(current) + 1 + len(piece) > size:
            chunks.append(Chunk(current, current_start, current_start + len(current)))
            cursor = text.find(piece, cursor)
            current_start = cursor
            current = piece
        else:
            if not current:
                cursor = text.find(piece, cursor)
                current_start = cursor
            current = f"{current} {piece}".strip()
        cursor += len(piece)
    if current:
        chunks.append(Chunk(current, current_start, current_start + len(current)))
    return chunks


def semantic_chunks(text: str, similarity_threshold: float = 0.15) -> list[Chunk]:
    """Group adjacent sentences sharing enough words.

    This intentionally uses set overlap rather than an embedding API: the boundary
    decision is visible, deterministic, and easy to replace with cosine similarity.
    """
    if not 0 <= similarity_threshold <= 1:
        raise ValueError("threshold must be between zero and one")
    sentences = [(m.group(), m.start(), m.end()) for m in re.finditer(r"[^.!?]+[.!?]?", text) if m.group().strip()]
    chunks: list[Chunk] = []
    current: list[tuple[str, int, int]] = []
    for sentence in sentences:
        if current:
            previous_words = set(re.findall(r"\w+", current[-1][0].lower()))
            words = set(re.findall(r"\w+", sentence[0].lower()))
            overlap = len(previous_words & words) / max(1, len(previous_words | words))
            if overlap < similarity_threshold:
                chunks.append(Chunk(" ".join(item[0].strip() for item in current), current[0][1], current[-1][2]))
                current = []
        current.append(sentence)
    if current:
        chunks.append(Chunk(" ".join(item[0].strip() for item in current), current[0][1], current[-1][2]))
    return chunks


def main() -> None:
    text = "Agents retrieve context. Retrieval needs good chunks.\n\nTools extend an agent."
    print([chunk.text for chunk in recursive_chunks(text, 45)])


if __name__ == "__main__":
    main()
