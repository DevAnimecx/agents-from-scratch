# Lesson 15: Consensus & Voting

**You are here:** Phase 5 / Lesson 15 of 20 · Multi-Agent

> Majority vote selects the most common proposal; Borda count lets ranked preferences contribute points across a debate.

## What

Majority vote selects the most common proposal; Borda count lets ranked preferences contribute points across a debate.

## Why

Agreement can be a useful stop signal, but the winner is not automatically correct. Preserve counts and rankings for review.

## How

Compare majority and Borda outcomes on tied proposals and make tie-breaking deterministic.

The runnable, offline-first implementation lives at [`src/phase5/15_consensus.py`](https://github.com/DevAnimecx/agents-from-scratch/blob/main/src/phase5/15_consensus.py).

```bash
python src/phase5/15_consensus.py
```

```python
# The lesson keeps the important boundary small enough to test.
# Read the source file for the complete implementation and demo.
```

## What the framework hides

LangGraph can model voting as graph state; the aggregation rule is application-specific.

## Exercise

Change one policy in the implementation, add a regression test for the new behavior, and write down the trade-off you observed. Then plug the same interface into a model or storage provider as an optional experiment.

## Checkpoint

- [ ] I can explain the input, state, output, and failure mode.
- [ ] I ran the example without a hosted API key.
- [ ] I can name the production concern the abstraction handles for me.

---

[← Lesson 14](lesson-14-orchestration.md) · [Lesson 16 →](../phase-6-production/lesson-16-observability.md)
