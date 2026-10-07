"""Lesson 09: a minimal MCP-shaped JSON-RPC server over stdio.

This teaching server intentionally implements the small message contract needed to
understand MCP. The production artifact in ``mcp-servers/`` adds packaging and a
more explicit tool surface; the optional official SDK is not required here.
"""
from __future__ import annotations

import json
import sys
from typing import Any, Callable


class MiniMCPServer:
    def __init__(self, name: str = "agents-from-scratch") -> None:
        self.name = name
        self.tools: dict[str, Callable[..., Any]] = {}

    def tool(self, name: str, function: Callable[..., Any]) -> None:
        self.tools[name] = function

    def handle(self, request: dict[str, Any]) -> dict[str, Any] | None:
        method, request_id = request.get("method"), request.get("id")
        if method == "initialize":
            result = {"protocolVersion": "2024-11-05", "serverInfo": {"name": self.name, "version": "0.1.0"},
                      "capabilities": {"tools": {}}}
        elif method == "tools/list":
            result = {"tools": [{"name": name, "description": function.__doc__ or ""} for name, function in self.tools.items()]}
        elif method == "tools/call":
            params = request.get("params", {})
            name, arguments = params.get("name"), params.get("arguments", {})
            if name not in self.tools:
                return {"jsonrpc": "2.0", "id": request_id, "error": {"code": -32602, "message": f"unknown tool: {name}"}}
            try:
                value = self.tools[name](**arguments)
                result = {"content": [{"type": "text", "text": str(value)}], "isError": False}
            except Exception as exc:  # return an RPC error, never crash the transport
                result = {"content": [{"type": "text", "text": str(exc)}], "isError": True}
        elif method == "notifications/initialized":
            return None
        else:
            return {"jsonrpc": "2.0", "id": request_id, "error": {"code": -32601, "message": "method not found"}}
        return {"jsonrpc": "2.0", "id": request_id, "result": result}

    def serve(self, input_stream: Any = sys.stdin, output_stream: Any = sys.stdout) -> None:
        for line in input_stream:
            if not line.strip():
                continue
            response = self.handle(json.loads(line))
            if response is not None:
                output_stream.write(json.dumps(response) + "\n")
                output_stream.flush()


def build_server() -> MiniMCPServer:
    server = MiniMCPServer()
    def word_count(text: str) -> int:
        """Count whitespace-separated words."""
        return len(text.split())
    server.tool("word_count", word_count)
    return server


def main() -> None:
    build_server().serve()


if __name__ == "__main__":
    main()
