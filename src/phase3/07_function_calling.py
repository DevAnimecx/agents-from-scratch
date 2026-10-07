"""Lesson 07: JSON schema -> parse -> validate -> execute -> retry."""
from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True)
class ToolSpec:
    name: str
    description: str
    parameters: dict[str, Any]
    function: Callable[..., Any]

    def public_schema(self) -> dict[str, Any]:
        return {"name": self.name, "description": self.description, "parameters": self.parameters}


class ToolCallError(ValueError):
    pass


def validate_arguments(spec: ToolSpec, arguments: dict[str, Any]) -> None:
    schema = spec.parameters
    required = schema.get("required", [])
    missing = [name for name in required if name not in arguments]
    if missing:
        raise ToolCallError(f"missing required arguments: {', '.join(missing)}")
    for name, value in arguments.items():
        definition = schema.get("properties", {}).get(name)
        if not definition:
            raise ToolCallError(f"unknown argument: {name}")
        expected = definition.get("type")
        valid = {"string": isinstance(value, str), "number": isinstance(value, (int, float)) and not isinstance(value, bool),
                 "integer": isinstance(value, int) and not isinstance(value, bool), "boolean": isinstance(value, bool),
                 "object": isinstance(value, dict), "array": isinstance(value, list)}.get(expected, True)
        if not valid:
            raise ToolCallError(f"{name} must be {expected}")


def parse_tool_call(payload: str | dict[str, Any]) -> tuple[str, dict[str, Any]]:
    try:
        data = json.loads(payload) if isinstance(payload, str) else payload
    except json.JSONDecodeError as exc:
        raise ToolCallError(f"invalid JSON: {exc.msg}") from exc
    if not isinstance(data, dict) or not isinstance(data.get("name"), str) or not isinstance(data.get("arguments", {}), dict):
        raise ToolCallError("tool call must contain a name and object arguments")
    return data["name"], data["arguments"]


def execute_tool_call(payload: str | dict[str, Any], tools: dict[str, ToolSpec]) -> Any:
    name, arguments = parse_tool_call(payload)
    if name not in tools:
        raise ToolCallError(f"unknown tool: {name}")
    spec = tools[name]
    validate_arguments(spec, arguments)
    return spec.function(**arguments)


def execute_with_retry(outputs: list[str | dict[str, Any]], tools: dict[str, ToolSpec], max_attempts: int = 3) -> Any:
    """Try model outputs in order; a real model can use the error as its retry prompt."""
    errors = []
    for output in outputs[:max_attempts]:
        try:
            return execute_tool_call(output, tools)
        except ToolCallError as exc:
            errors.append(str(exc))
    raise ToolCallError("tool call failed after retries: " + " | ".join(errors))


def main() -> None:
    add = ToolSpec("add", "Add two numbers", {"type": "object", "properties": {
        "a": {"type": "number"}, "b": {"type": "number"}}, "required": ["a", "b"]}, lambda a, b: a + b)
    print(execute_with_retry(['{"name":"add","arguments":{"a":2,"b":3}}'], {"add": add}))


if __name__ == "__main__":
    main()
