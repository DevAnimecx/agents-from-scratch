# Lesson 19: Code-Mixed RAG (Hinglish & Tanglish)

**You are here:** Phase 7 / Lesson 19 of 20 · Indic Language Agents

> Code-mixed retrieval benefits from script detection and chunking that does not erase the original text.

## What

Code-mixed retrieval benefits from script detection and chunking that does not erase the original text.

## Why

Latin, Devanagari, and Tamil can appear in one query. A pipeline should preserve source text while allowing language-aware normalization.

## How

Inspect script spans, try a small transliteration map, and keep original text as the citation source.

The runnable, offline-first implementation lives at [`src/phase7/19_code_mixed_rag.py`](https://github.com/DevAnimecx/agents-from-scratch/blob/main/src/phase7/19_code_mixed_rag.py).

```bash
python src/phase7/19_code_mixed_rag.py
```

```python
# The lesson keeps the important boundary small enough to test.
# Read the source file for the complete implementation and demo.
```

## What the framework hides

Multilingual encoders and regional models improve recall; language detection remains useful for routing and diagnostics.

## Exercise

Change one policy in the implementation, add a regression test for the new behavior, and write down the trade-off you observed. Then plug the same interface into a model or storage provider as an optional experiment.

## Checkpoint

- [ ] I can explain the input, state, output, and failure mode.
- [ ] I ran the example without a hosted API key.
- [ ] I can name the production concern the abstraction handles for me.

---

[← Lesson 18](../phase-6-production/lesson-18-deployment.md) · [Lesson 20 →](lesson-20-regional-tool-use.md)
