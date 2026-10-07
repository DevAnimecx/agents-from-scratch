# Lesson 10: ReAct Loop (80 lines)

**You are here:** Phase 4 / Lesson 10 of 20 · Planning

> A ReAct agent alternates between a policy decision, a tool action, an observation, and a new decision until it returns a final answer.

## What

A ReAct agent alternates between a policy decision, a tool action, an observation, and a new decision until it returns a final answer.

## Why

The loop is the smallest useful agent architecture. A step limit and explicit unknown-tool observation turn failure into state instead of a hang.

## How

Run the offline demo, replace `demo_policy` with an LLM adapter, and log every observation. Never let an unbounded model loop reach production.

The runnable, offline-first implementation lives at [`src/phase4/10_react_agent.py`](https://github.com/DevAnimecx/agents-from-scratch/blob/main/src/phase4/10_react_agent.py).

```bash
python src/phase4/10_react_agent.py
```

```python
# The lesson keeps the important boundary small enough to test.
# Read the source file for the complete implementation and demo.
```

## What the framework hides

LangGraph ReAct agents add graph state and durable execution; the same plan-act-observe invariant is still underneath.

## Exercise

Change one policy in the implementation, add a regression test for the new behavior, and write down the trade-off you observed. Then plug the same interface into a model or storage provider as an optional experiment.

## Checkpoint

- [ ] I can explain the input, state, output, and failure mode.
- [ ] I ran the example without a hosted API key.
- [ ] I can name the production concern the abstraction handles for me.

---

[← Lesson 09](../phase-3-tool-use/lesson-09-mcp.md) · [Lesson 11 →](lesson-11-tree-of-thought.md)
