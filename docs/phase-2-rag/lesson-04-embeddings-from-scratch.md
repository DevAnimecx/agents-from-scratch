# Lesson 04: Embeddings from Scratch

**You are here:** Phase 2 / Lesson 4 of 20 · RAG

> A hashing embedder maps words into a fixed-size vector and cosine similarity measures directional closeness.

## What

A hashing embedder maps words into a fixed-size vector and cosine similarity measures directional closeness.

## Why

Embeddings turn text retrieval into arithmetic. A deterministic baseline makes vector shape, normalization, and collisions observable.

## How

Embed a small corpus, calculate cosine scores, then swap the embedder for Sentence-Transformers without changing the retriever contract.

The runnable, offline-first implementation lives at [`src/phase2/04_embeddings.py`](https://github.com/DevAnimecx/agents-from-scratch/blob/main/src/phase2/04_embeddings.py).

```bash
python src/phase2/04_embeddings.py
```

```python
# The lesson keeps the important boundary small enough to test.
# Read the source file for the complete implementation and demo.
```

## What the framework hides

Sentence-Transformers supplies learned multilingual representations; it does not remove the need to inspect similarity and evaluation data.

## Exercise

Change one policy in the implementation, add a regression test for the new behavior, and write down the trade-off you observed. Then plug the same interface into a model or storage provider as an optional experiment.

## Checkpoint

- [ ] I can explain the input, state, output, and failure mode.
- [ ] I ran the example without a hosted API key.
- [ ] I can name the production concern the abstraction handles for me.

---

[← Lesson 03](../phase-1-context-memory/lesson-03-long-term-memory.md) · [Lesson 05 →](lesson-05-chunking.md)
