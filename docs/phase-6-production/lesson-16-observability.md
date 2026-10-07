# Lesson 16: Streaming & Observability

**You are here:** Phase 6 / Lesson 16 of 20 · Production

> Streaming yields partial output while spans and a cost ledger record latency, attributes, and token charges.

## What

Streaming yields partial output while spans and a cost ledger record latency, attributes, and token charges.

## Why

Users perceive latency differently when output streams, while operators need structured traces to debug slow or expensive runs.

## How

Collect a stream, wrap a step in `trace`, and record input/output token usage in `CostLedger`.

The runnable, offline-first implementation lives at [`src/phase6/16_observability.py`](https://github.com/DevAnimecx/agents-from-scratch/blob/main/src/phase6/16_observability.py).

```bash
python src/phase6/16_observability.py
```

```python
# The lesson keeps the important boundary small enough to test.
# Read the source file for the complete implementation and demo.
```

## What the framework hides

LangSmith, Langfuse, and OpenTelemetry exporters add storage and dashboards; instrumentation should remain provider-agnostic.

## Exercise

Change one policy in the implementation, add a regression test for the new behavior, and write down the trade-off you observed. Then plug the same interface into a model or storage provider as an optional experiment.

## Checkpoint

- [ ] I can explain the input, state, output, and failure mode.
- [ ] I ran the example without a hosted API key.
- [ ] I can name the production concern the abstraction handles for me.

---

[← Lesson 15](../phase-5-multi-agent/lesson-15-consensus.md) · [Lesson 17 →](lesson-17-evals-guardrails.md)
