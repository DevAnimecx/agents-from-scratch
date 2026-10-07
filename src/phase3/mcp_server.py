"""Packaging-safe entry point for the numbered MCP lesson."""
from importlib import import_module


def main() -> None:
    import_module("phase3.09_mcp_server").main()
