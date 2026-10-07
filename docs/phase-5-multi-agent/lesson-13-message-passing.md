# Lesson 13: Message Passing with asyncio

**You are here:** Phase 5 / Lesson 13 of 20 · Multi-Agent

> Agents can communicate through typed messages and `asyncio.Queue` mailboxes without sharing mutable state.

## What

Agents can communicate through typed messages and `asyncio.Queue` mailboxes without sharing mutable state.

## Why

Message passing makes sender, recipient, payload, and shutdown explicit. It also gives you a place to add timeouts and tracing.

## How

Run the analyst-to-writer example, add a timeout, and test that stop messages shut down every actor.

The runnable, offline-first implementation lives at [`src/phase5/13_message_passing.py`](https://github.com/DevAnimecx/agents-from-scratch/blob/main/src/phase5/13_message_passing.py).

```bash
python src/phase5/13_message_passing.py
```

```python
# The lesson keeps the important boundary small enough to test.
# Read the source file for the complete implementation and demo.
```

## What the framework hides

AutoGen abstracts conversations; raw queues teach the backpressure and lifecycle concerns hidden by that abstraction.

## Exercise

Change one policy in the implementation, add a regression test for the new behavior, and write down the trade-off you observed. Then plug the same interface into a model or storage provider as an optional experiment.

## Checkpoint

- [ ] I can explain the input, state, output, and failure mode.
- [ ] I ran the example without a hosted API key.
- [ ] I can name the production concern the abstraction handles for me.

---

[← Lesson 12](../phase-4-planning/lesson-12-self-reflection.md) · [Lesson 14 →](lesson-14-orchestration.md)
