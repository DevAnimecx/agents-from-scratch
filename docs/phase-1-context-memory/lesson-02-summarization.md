# Lesson 02: Summarization Chains

**You are here:** Phase 1 / Lesson 2 of 20 · Context & Memory

> A summarization chain compresses old turns into durable context while retaining a small recent window.

## What

A summarization chain compresses old turns into durable context while retaining a small recent window.

## Why

FIFO deletion loses facts permanently. Summaries trade exact wording for a longer-lived representation of the conversation.

## How

Implement a callable summarizer, trigger it after a token threshold, and keep the summarizer interface independent from Ollama or another model provider.

The runnable, offline-first implementation lives at [`src/phase1/02_summarization.py`](https://github.com/DevAnimecx/agents-from-scratch/blob/main/src/phase1/02_summarization.py).

```bash
python src/phase1/02_summarization.py
```

```python
# The lesson keeps the important boundary small enough to test.
# Read the source file for the complete implementation and demo.
```

## What the framework hides

LangChain's summary memory packages this state machine; the model prompt and compression policy still deserve tests.

## Exercise

Change one policy in the implementation, add a regression test for the new behavior, and write down the trade-off you observed. Then plug the same interface into a model or storage provider as an optional experiment.

## Checkpoint

- [ ] I can explain the input, state, output, and failure mode.
- [ ] I ran the example without a hosted API key.
- [ ] I can name the production concern the abstraction handles for me.

---

[← Lesson 01](lesson-01-token-budgeting.md) · [Lesson 03 →](lesson-03-long-term-memory.md)
