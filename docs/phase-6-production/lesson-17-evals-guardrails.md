# Lesson 17: Evals & Guardrails

**You are here:** Phase 6 / Lesson 17 of 20 · Production

> A production agent needs measurable evals and input/output controls such as PII redaction and rate limiting.

## What

A production agent needs measurable evals and input/output controls such as PII redaction and rate limiting.

## Why

A demo can look correct while drifting, leaking personal data, or exceeding a budget. Guardrails make failure modes explicit.

## How

Run exact-match evaluation, redact email and phone patterns, and exercise a token bucket limiter.

The runnable, offline-first implementation lives at [`src/phase6/17_evals_guardrails.py`](https://github.com/DevAnimecx/agents-from-scratch/blob/main/src/phase6/17_evals_guardrails.py).

```bash
python src/phase6/17_evals_guardrails.py
```

```python
# The lesson keeps the important boundary small enough to test.
# Read the source file for the complete implementation and demo.
```

## What the framework hides

DeepEval and Guardrails AI provide larger ecosystems; start with a small regression set you can inspect.

## Exercise

Change one policy in the implementation, add a regression test for the new behavior, and write down the trade-off you observed. Then plug the same interface into a model or storage provider as an optional experiment.

## Checkpoint

- [ ] I can explain the input, state, output, and failure mode.
- [ ] I ran the example without a hosted API key.
- [ ] I can name the production concern the abstraction handles for me.

---

[← Lesson 16](lesson-16-observability.md) · [Lesson 18 →](lesson-18-deployment.md)
