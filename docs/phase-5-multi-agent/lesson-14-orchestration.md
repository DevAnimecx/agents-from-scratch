# Lesson 14: Role Assignment & Orchestration

**You are here:** Phase 5 / Lesson 14 of 20 · Multi-Agent

> A supervisor executes a dependency-aware task graph and assigns each task to a named worker role.

## What

A supervisor executes a dependency-aware task graph and assigns each task to a named worker role.

## Why

Delegation needs ownership: who schedules work, detects cycles, retries failures, and combines results?

## How

Build a two-task graph, then introduce a missing dependency and a cycle to see the explicit errors.

The runnable, offline-first implementation lives at [`src/phase5/14_orchestration.py`](https://github.com/DevAnimecx/agents-from-scratch/blob/main/src/phase5/14_orchestration.py).

```bash
python src/phase5/14_orchestration.py
```

```python
# The lesson keeps the important boundary small enough to test.
# Read the source file for the complete implementation and demo.
```

## What the framework hides

CrewAI Crew and task graphs provide ergonomic role definitions; this supervisor is the minimal control plane.

## Exercise

Change one policy in the implementation, add a regression test for the new behavior, and write down the trade-off you observed. Then plug the same interface into a model or storage provider as an optional experiment.

## Checkpoint

- [ ] I can explain the input, state, output, and failure mode.
- [ ] I ran the example without a hosted API key.
- [ ] I can name the production concern the abstraction handles for me.

---

[← Lesson 13](lesson-13-message-passing.md) · [Lesson 15 →](lesson-15-consensus.md)
