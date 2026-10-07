---
name: rag-pipeline
description: Design a measurable retrieval-augmented generation pipeline.
---

# RAG pipeline skill

Use this skill to build RAG from the document boundary outward.

## Checklist

- Preserve source IDs and original text.
- Choose and test chunk size, overlap, and metadata.
- Make embedding dimensions and normalization explicit.
- Compare dense, lexical, and hybrid retrieval on a fixed dataset.
- Rerank for relevance and diversity, then evaluate answer faithfulness and citation recall.

Start with `src/phase2/04_embeddings.py`, `05_chunking.py`, and `06_vector_search.py`. A vector database is an optimization and persistence layer, not a substitute for retrieval evaluation.

Powered by Aspiro · part of agents-from-scratch
