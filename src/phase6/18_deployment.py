"""Lesson 18: turn a lesson agent into a reproducible MCP/skill artifact."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def build_manifest(name: str, command: list[str], description: str) -> dict[str, Any]:
    if not name or not command:
        raise ValueError("name and command are required")
    return {"name": name, "version": "0.1.0", "description": description, "command": command,
            "healthcheck": {"type": "stdio", "timeout_seconds": 5}}


def write_manifest(path: str | Path, **kwargs: Any) -> Path:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(build_manifest(**kwargs), indent=2) + "\n", encoding="utf-8")
    return destination


def main() -> None:
    print(json.dumps(build_manifest("aspiro-agent", ["python", "-m", "agent"], "A lesson agent"), indent=2))


if __name__ == "__main__":
    main()
