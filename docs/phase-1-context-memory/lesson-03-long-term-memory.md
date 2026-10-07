# Lesson 03: Long-Term Memory (Vector)

**You are here:** Phase 1 / Lesson 3 of 20 · Context & Memory

> Long-term memory stores vectors beside text and ranks memories with cosine similarity. It persists as ordinary JSON.

## What

Long-term memory stores vectors beside text and ranks memories with cosine similarity. It persists as ordinary JSON.

## Why

A conversation window is short-lived. Retrieval lets an agent recall relevant facts without replaying every previous turn.

## How

Add records, search with a query vector, save to JSON, reload, and test that the most similar memory is first.

The runnable, offline-first implementation lives at [`src/phase1/03_memory.py`](https://github.com/DevAnimecx/agents-from-scratch/blob/main/src/phase1/03_memory.py).

```bash
python src/phase1/03_memory.py
```

```python
# The lesson keeps the important boundary small enough to test.
# Read the source file for the complete implementation and demo.
```

## What the framework hides

Mem0 and ChromaDB add production storage, filtering, and indexing; this lesson isolates the ranking primitive.

## Exercise

Change one policy in the implementation, add a regression test for the new behavior, and write down the trade-off you observed. Then plug the same interface into a model or storage provider as an optional experiment.

## Checkpoint

- [ ] I can explain the input, state, output, and failure mode.
- [ ] I ran the example without a hosted API key.
- [ ] I can name the production concern the abstraction handles for me.

---

[← Lesson 02](lesson-02-summarization.md) · [Lesson 04 →](../phase-2-rag/lesson-04-embeddings-from-scratch.md)
