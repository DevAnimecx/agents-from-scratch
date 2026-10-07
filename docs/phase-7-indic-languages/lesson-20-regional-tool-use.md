# Lesson 20: Regional LLM Tool Use

**You are here:** Phase 7 / Lesson 20 of 20 · Indic Language Agents

> Regional tool use normalizes multilingual requests into the same validated canonical tool contract.

## What

Regional tool use normalizes multilingual requests into the same validated canonical tool contract.

## Why

A Hindi or Tamil user should not require a separate business-logic implementation. Normalize language at the boundary, then dispatch safely.

## How

Parse weather requests in mixed scripts, inspect the language label, and reject unsupported tools before execution.

The runnable, offline-first implementation lives at [`src/phase7/20_regional_tool_use.py`](https://github.com/DevAnimecx/agents-from-scratch/blob/main/src/phase7/20_regional_tool_use.py).

```bash
python src/phase7/20_regional_tool_use.py
```

```python
# The lesson keeps the important boundary small enough to test.
# Read the source file for the complete implementation and demo.
```

## What the framework hides

AI4Bharat, Sarvam, Gemma, and other multilingual models can improve parsing; canonical schemas keep execution stable.

## Exercise

Change one policy in the implementation, add a regression test for the new behavior, and write down the trade-off you observed. Then plug the same interface into a model or storage provider as an optional experiment.

## Checkpoint

- [ ] I can explain the input, state, output, and failure mode.
- [ ] I ran the example without a hosted API key.
- [ ] I can name the production concern the abstraction handles for me.

---

[← Lesson 19](lesson-19-code-mixed-rag.md) · [Course home →](../index.md)
