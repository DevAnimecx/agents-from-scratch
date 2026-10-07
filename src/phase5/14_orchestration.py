"""Lesson 14: a small supervisor that owns a task graph and role assignment."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Task:
    name: str
    role: str
    depends_on: tuple[str, ...] = ()


class Supervisor:
    def __init__(self, workers: dict[str, Callable[[Task, dict[str, str]], str]]) -> None:
        self.workers = workers

    def run(self, tasks: list[Task]) -> dict[str, str]:
        pending = list(tasks)
        completed: dict[str, str] = {}
        while pending:
            ready = [task for task in pending if all(dep in completed for dep in task.depends_on)]
            if not ready:
                raise ValueError("task graph has a missing dependency or cycle")
            for task in ready:
                if task.role not in self.workers:
                    raise KeyError(f"no worker for role {task.role!r}")
                completed[task.name] = self.workers[task.role](task, completed)
                pending.remove(task)
        return completed


def main() -> None:
    supervisor = Supervisor({"researcher": lambda task, _: "facts", "writer": lambda task, result: f"draft from {result['research']}"})
    print(supervisor.run([Task("research", "researcher"), Task("draft", "writer", ("research",))]))


if __name__ == "__main__":
    main()
