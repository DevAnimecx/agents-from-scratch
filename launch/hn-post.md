# Show HN draft

**Title:** I built an AI agent pipeline from raw Python before using a framework

I kept reaching for an agent framework without being able to explain what happened between a user message and a tool result. agents-from-scratch is a 20-lesson, offline-first course that makes those mechanics explicit.

The first pass uses ordinary Python, NumPy, JSON, and asyncio to build:

- token windows, summaries, and persistent vector memory;
- embeddings, chunking, hybrid retrieval, and MMR;
- schema validation, tool registries, and an MCP-shaped stdio server;
- a bounded ReAct loop, tree search, reflection, and multi-agent protocols;
- streaming, traces, evals, PII redaction, rate limiting, and deployment contracts;
- code-mixed RAG and regional-language tool boundaries.

Then each lesson maps the primitive to a framework abstraction. No API key is required for the examples or tests.

Repo: https://github.com/DevAnimecx/agents-from-scratch
Docs: https://aspiro.dev/

I would especially value feedback on which primitive is still too magical, which lesson is too hard for a mid-level Python developer, and whether the Indic-language examples preserve useful distinctions without overclaiming model quality.
