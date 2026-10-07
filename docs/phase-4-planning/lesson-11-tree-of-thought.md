# Lesson 11: Tree of Thought

**You are here:** Phase 4 / Lesson 11 of 20 · Planning

> Tree search keeps several candidate reasoning branches, expands them, scores them, and prunes to a width.

## What

Tree search keeps several candidate reasoning branches, expands them, scores them, and prunes to a width.

## Why

A single greedy chain can commit to a bad assumption. Breadth-first or depth-first search trades latency for alternative plans.

## How

Write an `expand` function, vary width and depth, and test that the best score survives pruning.

The runnable, offline-first implementation lives at [`src/phase4/11_tree_of_thought.py`](https://github.com/DevAnimecx/agents-from-scratch/blob/main/src/phase4/11_tree_of_thought.py).

```bash
python src/phase4/11_tree_of_thought.py
```

```python
# The lesson keeps the important boundary small enough to test.
# Read the source file for the complete implementation and demo.
```

## What the framework hides

Multi-agent group chat frameworks can provide parallel proposals; this lesson isolates the search policy.

## Exercise

Change one policy in the implementation, add a regression test for the new behavior, and write down the trade-off you observed. Then plug the same interface into a model or storage provider as an optional experiment.

## Checkpoint

- [ ] I can explain the input, state, output, and failure mode.
- [ ] I ran the example without a hosted API key.
- [ ] I can name the production concern the abstraction handles for me.

---

[← Lesson 10](lesson-10-react-agent.md) · [Lesson 12 →](lesson-12-self-reflection.md)
