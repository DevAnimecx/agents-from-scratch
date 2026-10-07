# Lesson 05: Chunking Strategies

**You are here:** Phase 2 / Lesson 5 of 20 · RAG

> Chunk boundaries are a retrieval decision. Fixed, recursive, and semantic chunkers expose different trade-offs between context and precision.

## What

Chunk boundaries are a retrieval decision. Fixed, recursive, and semantic chunkers expose different trade-offs between context and precision.

## Why

A perfect embedding cannot recover a fact that was split across unrelated chunks or buried in an oversized chunk.

## How

Run all three chunkers over the same document, inspect offsets, and vary size and overlap before choosing a default.

The runnable, offline-first implementation lives at [`src/phase2/05_chunking.py`](https://github.com/DevAnimecx/agents-from-scratch/blob/main/src/phase2/05_chunking.py).

```bash
python src/phase2/05_chunking.py
```

```python
# The lesson keeps the important boundary small enough to test.
# Read the source file for the complete implementation and demo.
```

## What the framework hides

LlamaIndex NodeParser offers production integrations; the hand-built functions clarify what a chunk actually contains.

## Exercise

Change one policy in the implementation, add a regression test for the new behavior, and write down the trade-off you observed. Then plug the same interface into a model or storage provider as an optional experiment.

## Checkpoint

- [ ] I can explain the input, state, output, and failure mode.
- [ ] I ran the example without a hosted API key.
- [ ] I can name the production concern the abstraction handles for me.

---

[← Lesson 04](lesson-04-embeddings-from-scratch.md) · [Lesson 06 →](lesson-06-vector-search-reranking.md)
