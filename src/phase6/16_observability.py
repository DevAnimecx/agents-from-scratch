"""Lesson 16: streaming events, spans, and a simple cost ledger."""
from __future__ import annotations

import asyncio
import time
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import AsyncIterator, Iterator


@dataclass
class Span:
    name: str
    started_at: float = field(default_factory=time.perf_counter)
    ended_at: float | None = None
    attributes: dict[str, str | float | int] = field(default_factory=dict)

    def finish(self) -> None:
        self.ended_at = time.perf_counter()

    @property
    def duration_ms(self) -> float:
        return ((self.ended_at or time.perf_counter()) - self.started_at) * 1000


@contextmanager
def trace(name: str, attributes: dict[str, str | float | int] | None = None) -> Iterator[Span]:
    span = Span(name, attributes=attributes or {})
    try:
        yield span
    finally:
        span.finish()


@dataclass
class CostLedger:
    input_rate: float = 0.0
    output_rate: float = 0.0
    total: float = 0.0

    def record(self, input_tokens: int, output_tokens: int) -> float:
        charge = input_tokens * self.input_rate + output_tokens * self.output_rate
        self.total += charge
        return charge


async def stream_text(text: str, chunk_size: int = 8) -> AsyncIterator[str]:
    if chunk_size < 1:
        raise ValueError("chunk_size must be positive")
    for position in range(0, len(text), chunk_size):
        await asyncio.sleep(0)
        yield text[position:position + chunk_size]


async def collect_stream(text: str) -> str:
    return "".join([chunk async for chunk in stream_text(text)])


def main() -> None:
    with trace("demo", {"lesson": 16}) as span:
        print(asyncio.run(collect_stream("streamed agent answer")))
    print(f"{span.duration_ms:.2f} ms")


if __name__ == "__main__":
    main()
