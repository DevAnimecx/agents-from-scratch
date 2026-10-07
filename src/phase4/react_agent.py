"""Packaging-safe entry point for the numbered ReAct lesson."""
from importlib import import_module


def main() -> None:
    import_module("phase4.10_react_agent").main()
