# Lesson 08: Tool Registry & Dispatch

**You are here:** Phase 3 / Lesson 8 of 20 · Tool Use

> A registry is a dictionary of named callables plus a dispatch boundary that turns a validated name and arguments into a result.

## What

A registry is a dictionary of named callables plus a dispatch boundary that turns a validated name and arguments into a result.

## Why

As tools grow, scattered `if` statements become an untestable routing layer. Registration creates one inspectable source of truth.

## How

Register tools, publish their schemas, reject duplicates, and dispatch only known names.

The runnable, offline-first implementation lives at [`src/phase3/08_tool_registry.py`](https://github.com/DevAnimecx/agents-from-scratch/blob/main/src/phase3/08_tool_registry.py).

```bash
python src/phase3/08_tool_registry.py
```

```python
# The lesson keeps the important boundary small enough to test.
# Read the source file for the complete implementation and demo.
```

## What the framework hides

LangChain Tool and Pydantic AI add schemas and lifecycle hooks; the registry pattern remains the core.

## Exercise

Change one policy in the implementation, add a regression test for the new behavior, and write down the trade-off you observed. Then plug the same interface into a model or storage provider as an optional experiment.

## Checkpoint

- [ ] I can explain the input, state, output, and failure mode.
- [ ] I ran the example without a hosted API key.
- [ ] I can name the production concern the abstraction handles for me.

---

[← Lesson 07](lesson-07-function-calling.md) · [Lesson 09 →](lesson-09-mcp.md)
