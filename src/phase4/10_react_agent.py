"""Lesson 10: the ReAct loop in plain Python.

The loop is intentionally model-agnostic. A ``policy`` receives the transcript and
returns either ``Action(tool, input)`` or ``Final(answer)``. The demo policy lets
this file run without an API key.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Action:
    tool: str
    input: str


@dataclass(frozen=True)
class Final:
    answer: str


@dataclass(frozen=True)
class Observation:
    tool: str
    result: str


Decision = Action | Final
Policy = Callable[[str, list[object]], Decision]


class ReActAgent:
    def __init__(self, tools: dict[str, Callable[[str], str]], policy: Policy, max_steps: int = 8) -> None:
        self.tools, self.policy, self.max_steps = tools, policy, max_steps

    def run(self, goal: str) -> str:
        transcript: list[object] = []
        for step in range(self.max_steps):
            decision = self.policy(goal, transcript)
            if isinstance(decision, Final):
                return decision.answer
            if decision.tool not in self.tools:
                transcript.append(Observation(decision.tool, "ERROR: unknown tool"))
                continue
            try:
                result = self.tools[decision.tool](decision.input)
            except Exception as exc:  # observation is fed back to the policy
                result = f"ERROR: {exc}"
            transcript.append(Observation(decision.tool, result))
        raise RuntimeError(f"agent exceeded {self.max_steps} steps")


def demo_policy(goal: str, transcript: list[object]) -> Decision:
    if not transcript:
        return Action("lookup", goal)
    observation = transcript[-1]
    return Final(f"I found: {getattr(observation, 'result', observation)}")


def main() -> None:
    agent = ReActAgent({"lookup": lambda query: f"offline result for {query}"}, demo_policy)
    print(agent.run("the definition of RAG"))


if __name__ == "__main__":
    main()
