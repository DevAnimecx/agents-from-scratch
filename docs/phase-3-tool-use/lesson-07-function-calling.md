# Lesson 07: Function Calling from Scratch

**You are here:** Phase 3 / Lesson 7 of 20 · Tool Use

> Function calling is a typed data pipeline: schema, model output, JSON parsing, validation, execution, and bounded retry.

## What

Function calling is a typed data pipeline: schema, model output, JSON parsing, validation, execution, and bounded retry.

## Why

Treating a tool call as executable text invites malformed arguments and unsafe actions. Treating it as data creates a validation boundary.

## How

Define a `ToolSpec`, validate required properties and types, execute a valid call, and feed errors into a retry loop.

The runnable, offline-first implementation lives at [`src/phase3/07_function_calling.py`](https://github.com/DevAnimecx/agents-from-scratch/blob/main/src/phase3/07_function_calling.py).

```bash
python src/phase3/07_function_calling.py
```

```python
# The lesson keeps the important boundary small enough to test.
# Read the source file for the complete implementation and demo.
```

## What the framework hides

Provider-native function calling moves formatting into the API, but your application still owns authorization, validation, and error handling.

## Exercise

Change one policy in the implementation, add a regression test for the new behavior, and write down the trade-off you observed. Then plug the same interface into a model or storage provider as an optional experiment.

## Checkpoint

- [ ] I can explain the input, state, output, and failure mode.
- [ ] I ran the example without a hosted API key.
- [ ] I can name the production concern the abstraction handles for me.

---

[← Lesson 06](../phase-2-rag/lesson-06-vector-search-reranking.md) · [Lesson 08 →](lesson-08-tool-registry.md)
