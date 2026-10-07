"""Lesson 19: script-aware chunking for Hinglish and other code-mixed text."""
from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class LanguageSpan:
    text: str
    script: str


def detect_script(text: str) -> str:
    counts = {"latin": 0, "devanagari": 0, "tamil": 0, "other": 0}
    for character in text:
        codepoint = ord(character)
        if "A" <= character <= "z":
            counts["latin"] += 1
        elif 0x0900 <= codepoint <= 0x097F:
            counts["devanagari"] += 1
        elif 0x0B80 <= codepoint <= 0x0BFF:
            counts["tamil"] += 1
        elif character.isalpha():
            counts["other"] += 1
    return max(counts, key=counts.get) if any(counts.values()) else "other"


def script_spans(text: str) -> list[LanguageSpan]:
    spans: list[LanguageSpan] = []
    for piece in re.findall(r"\S+", text):
        span = LanguageSpan(piece, detect_script(piece))
        if spans and spans[-1].script == span.script:
            spans[-1] = LanguageSpan(spans[-1].text + " " + span.text, span.script)
        else:
            spans.append(span)
    return spans


def transliterate_devanagari(text: str) -> str:
    """Small teaching map, not a replacement for a linguistic transliterator."""
    table = {"नमस्ते": "namaste", "मौसम": "mausam", "आज": "aaj", "है": "hai", "कैसा": "kaisa"}
    for source, target in table.items():
        text = text.replace(source, target)
    return text


def mixed_language_chunks(text: str, max_words: int = 40) -> list[str]:
    if max_words < 1:
        raise ValueError("max_words must be positive")
    words = text.split()
    return [" ".join(words[index:index + max_words]) for index in range(0, len(words), max_words)]


def main() -> None:
    text = "Mausam आज अच्छा है, so the agent can answer in Hinglish."
    print(script_spans(text))
    print(transliterate_devanagari(text))


if __name__ == "__main__":
    main()
