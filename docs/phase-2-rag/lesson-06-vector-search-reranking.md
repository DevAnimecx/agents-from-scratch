# Lesson 06: Vector Search & Re-ranking

**You are here:** Phase 2 / Lesson 6 of 20 · RAG

> A useful retriever can combine dense similarity, BM25-style lexical scores, and MMR diversity before returning top-k context.

## What

A useful retriever can combine dense similarity, BM25-style lexical scores, and MMR diversity before returning top-k context.

## Why

Dense search catches meaning; lexical search catches exact names and identifiers. MMR reduces redundant citations.

## How

Compare `vector_search`, `bm25`, `hybrid_search`, and `mmr` on a fixed corpus. Record misses, not just wins.

The runnable, offline-first implementation lives at [`src/phase2/06_vector_search.py`](https://github.com/DevAnimecx/agents-from-scratch/blob/main/src/phase2/06_vector_search.py).

```bash
python src/phase2/06_vector_search.py
```

```python
# The lesson keeps the important boundary small enough to test.
# Read the source file for the complete implementation and demo.
```

## What the framework hides

pgvector and ChromaDB provide indexes and persistence; reranking is still a product decision.

## Exercise

Change one policy in the implementation, add a regression test for the new behavior, and write down the trade-off you observed. Then plug the same interface into a model or storage provider as an optional experiment.

## Checkpoint

- [ ] I can explain the input, state, output, and failure mode.
- [ ] I ran the example without a hosted API key.
- [ ] I can name the production concern the abstraction handles for me.

---

[← Lesson 05](lesson-05-chunking.md) · [Lesson 07 →](../phase-3-tool-use/lesson-07-function-calling.md)
