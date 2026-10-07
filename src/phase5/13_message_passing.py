"""Lesson 13: actors communicating through asyncio queues."""
from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Any, Awaitable, Callable


@dataclass(frozen=True)
class Message:
    sender: str
    recipient: str
    payload: Any
    stop: bool = False


Handler = Callable[[Message], Awaitable[Message | None]]


class Actor:
    def __init__(self, name: str, handler: Handler) -> None:
        self.name, self.handler = name, handler
        self.inbox: asyncio.Queue[Message] = asyncio.Queue()

    async def run(self, actors: dict[str, "Actor"]) -> None:
        while True:
            message = await self.inbox.get()
            if message.stop:
                return
            reply = await self.handler(message)
            if reply is not None:
                await actors[reply.recipient].inbox.put(reply)


async def conversation() -> list[str]:
    transcript: list[str] = []
    async def analyst(message: Message) -> Message:
        transcript.append(f"analyst: {message.payload}")
        return Message("analyst", "writer", f"Analysis of {message.payload}")
    async def writer(message: Message) -> None:
        transcript.append(f"writer: {message.payload}")
    actors = {"analyst": Actor("analyst", analyst), "writer": Actor("writer", writer)}
    tasks = [asyncio.create_task(actor.run(actors)) for actor in actors.values()]
    await actors["analyst"].inbox.put(Message("user", "analyst", "RAG"))
    await asyncio.sleep(0)
    await asyncio.sleep(0)
    for actor in actors.values():
        await actor.inbox.put(Message("system", actor.name, None, stop=True))
    await asyncio.gather(*tasks)
    return transcript


def main() -> None:
    print(asyncio.run(conversation()))


if __name__ == "__main__":
    main()
