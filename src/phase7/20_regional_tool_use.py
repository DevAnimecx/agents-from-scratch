"""Lesson 20: normalize regional-language tool requests before validation."""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True)
class RegionalToolCall:
    name: str
    arguments: dict[str, Any]
    language: str


_TOOL_ALIASES = {"मौसम": "weather", "weather": "weather", "வானிலை": "weather", "खोजो": "search", "search": "search"}


def normalize_tool_call(text: str, language: str = "auto") -> RegionalToolCall:
    lowered = text.lower()
    name = next((canonical for alias, canonical in _TOOL_ALIASES.items() if alias in lowered), None)
    if name is None:
        raise ValueError("could not identify a supported tool")
    city_match = re.search(r"(?:in|में|में|இல்)\s+([\w\u0900-\u0bff-]+)", text, re.IGNORECASE)
    arguments = {"city": city_match.group(1)} if city_match else {}
    return RegionalToolCall(name, arguments, language if language != "auto" else "mixed")


def dispatch_regional(call: RegionalToolCall, tools: dict[str, Callable[..., Any]]) -> Any:
    if call.name not in tools:
        raise KeyError(call.name)
    return tools[call.name](**call.arguments)


def main() -> None:
    call = normalize_tool_call("मौसम in Delhi", "hi")
    print(call, dispatch_regional(call, {"weather": lambda city: f"Weather for {city}"}))


if __name__ == "__main__":
    main()
