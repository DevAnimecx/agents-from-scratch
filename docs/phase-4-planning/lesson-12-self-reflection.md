# Lesson 12: Self-Reflection & Critique

**You are here:** Phase 4 / Lesson 12 of 20 · Planning

> Reflection is a bounded generate → critique → revise loop with an auditable history of each revision.

## What

Reflection is a bounded generate → critique → revise loop with an auditable history of each revision.

## Why

A second pass can catch missing constraints, but unlimited self-critique increases cost without guaranteeing truth.

## How

Give the loop a deterministic critique, stop on acceptance, and assert the maximum number of revisions.

The runnable, offline-first implementation lives at [`src/phase4/12_self_reflection.py`](https://github.com/DevAnimecx/agents-from-scratch/blob/main/src/phase4/12_self_reflection.py).

```bash
python src/phase4/12_self_reflection.py
```

```python
# The lesson keeps the important boundary small enough to test.
# Read the source file for the complete implementation and demo.
```

## What the framework hides

CrewAI verifiers package role/task wiring; the quality contract and stopping condition remain yours.

## Exercise

Change one policy in the implementation, add a regression test for the new behavior, and write down the trade-off you observed. Then plug the same interface into a model or storage provider as an optional experiment.

## Checkpoint

- [ ] I can explain the input, state, output, and failure mode.
- [ ] I ran the example without a hosted API key.
- [ ] I can name the production concern the abstraction handles for me.

---

[← Lesson 11](lesson-11-tree-of-thought.md) · [Lesson 13 →](../phase-5-multi-agent/lesson-13-message-passing.md)
