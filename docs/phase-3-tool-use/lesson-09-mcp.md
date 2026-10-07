# Lesson 09: MCP Protocol (Model Context Protocol)

**You are here:** Phase 3 / Lesson 9 of 20 · Tool Use

> MCP standardizes how a client discovers and calls tools. The lesson implements a minimal JSON-RPC-over-stdio server.

## What

MCP standardizes how a client discovers and calls tools. The lesson implements a minimal JSON-RPC-over-stdio server.

## Why

A protocol boundary lets tools live in a separate process and be reused by different agent clients.

## How

Send `initialize`, `tools/list`, and `tools/call` requests to the offline server, then compare the response envelope with the SDK artifact.

The runnable, offline-first implementation lives at [`src/phase3/09_mcp_server.py`](https://github.com/DevAnimecx/agents-from-scratch/blob/main/src/phase3/09_mcp_server.py).

```bash
python src/phase3/09_mcp_server.py
```

```python
# The lesson keeps the important boundary small enough to test.
# Read the source file for the complete implementation and demo.
```

## What the framework hides

The official MCP SDK handles protocol details and transports; writing the tiny transport once explains what the SDK is protecting you from.

## Exercise

Change one policy in the implementation, add a regression test for the new behavior, and write down the trade-off you observed. Then plug the same interface into a model or storage provider as an optional experiment.

## Checkpoint

- [ ] I can explain the input, state, output, and failure mode.
- [ ] I ran the example without a hosted API key.
- [ ] I can name the production concern the abstraction handles for me.

---

[← Lesson 08](lesson-08-tool-registry.md) · [Lesson 10 →](../phase-4-planning/lesson-10-react-agent.md)
