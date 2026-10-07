# Lesson 01: Token Budgeting & Sliding Windows

**You are here:** Phase 1 / Lesson 1 of 20 · Context & Memory

> A token window keeps the newest conversation turns under a hard budget. The hand-built version makes counting, pinning, and FIFO eviction visible.

## What

A token window keeps the newest conversation turns under a hard budget. The hand-built version makes counting, pinning, and FIFO eviction visible.

## Why

A model cannot see an unlimited transcript. An explicit budget prevents context overflow and lets you reason about what the model forgot.

## How

Use `TokenWindow(max_tokens=...)`, add messages, inspect `token_count`, and compare `as_prompt()` with the original transcript.

The runnable, offline-first implementation lives at [`src/phase1/01_token_budget.py`](https://github.com/DevAnimecx/agents-from-scratch/blob/main/src/phase1/01_token_budget.py).

```bash
python src/phase1/01_token_budget.py
```

```python
# The lesson keeps the important boundary small enough to test.
# Read the source file for the complete implementation and demo.
```

## What the framework hides

LangChain's window memory provides the same policy behind a higher-level API; the important choice is which messages to evict.

## Exercise

Change one policy in the implementation, add a regression test for the new behavior, and write down the trade-off you observed. Then plug the same interface into a model or storage provider as an optional experiment.

## Checkpoint

- [ ] I can explain the input, state, output, and failure mode.
- [ ] I ran the example without a hosted API key.
- [ ] I can name the production concern the abstraction handles for me.

---

[← Course home](../index.md) · [Lesson 02 →](lesson-02-summarization.md)
