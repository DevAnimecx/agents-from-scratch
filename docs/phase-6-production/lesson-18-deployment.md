# Lesson 18: Deployment: MCP Server + Agent Skill

**You are here:** Phase 6 / Lesson 18 of 20 · Production

> Deployment is a reproducible contract: a name, version, command, description, and health check that another runtime can launch.

## What

Deployment is a reproducible contract: a name, version, command, description, and health check that another runtime can launch.

## Why

Packaging turns a notebook into something discoverable, testable, and installable by an agent runtime.

## How

Generate a manifest, inspect the packaged MCP server, and read the companion skill files before publishing credentials or network access.

The runnable, offline-first implementation lives at [`src/phase6/18_deployment.py`](https://github.com/DevAnimecx/agents-from-scratch/blob/main/src/phase6/18_deployment.py).

```bash
python src/phase6/18_deployment.py
```

```python
# The lesson keeps the important boundary small enough to test.
# Read the source file for the complete implementation and demo.
```

## What the framework hides

Production runtimes and `npx skills add` provide distribution; the manifest makes assumptions reviewable.

## Exercise

Change one policy in the implementation, add a regression test for the new behavior, and write down the trade-off you observed. Then plug the same interface into a model or storage provider as an optional experiment.

## Checkpoint

- [ ] I can explain the input, state, output, and failure mode.
- [ ] I ran the example without a hosted API key.
- [ ] I can name the production concern the abstraction handles for me.

---

[← Lesson 17](lesson-17-evals-guardrails.md) · [Lesson 19 →](../phase-7-indic-languages/lesson-19-code-mixed-rag.md)
