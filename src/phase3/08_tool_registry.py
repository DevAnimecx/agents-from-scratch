"""Lesson 08: a dict of callables with explicit registration and dispatch."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True)
class RegisteredTool:
    name: str
    description: str
    function: Callable[..., Any]


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, RegisteredTool] = {}

    def register(self, name: str, description: str, function: Callable[..., Any]) -> None:
        if not name or name in self._tools:
            raise ValueError(f"tool name is empty or already registered: {name!r}")
        self._tools[name] = RegisteredTool(name, description, function)

    def dispatch(self, tool_name: str, **arguments: Any) -> Any:
        try:
            tool = self._tools[tool_name]
        except KeyError as exc:
            raise KeyError(f"unknown tool {tool_name!r}; choose from {sorted(self._tools)}") from exc
        return tool.function(**arguments)

    def schemas(self) -> list[dict[str, str]]:
        return [{"name": t.name, "description": t.description} for t in self._tools.values()]

    def __contains__(self, name: str) -> bool:
        return name in self._tools


def main() -> None:
    tools = ToolRegistry()
    tools.register("greet", "Say hello", lambda name: f"Hello, {name}!")
    print(tools.dispatch("greet", name="agent"))


if __name__ == "__main__":
    main()
