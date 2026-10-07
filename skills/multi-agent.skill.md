---
name: multi-agent
description: Compose explicit message-passing agents with bounded orchestration.
---

# Multi-agent skill

Use this skill only when separate roles or parallel work improve a measurable outcome.

## Protocol

- Give every message a sender, recipient, payload, and correlation ID.
- Keep a supervisor responsible for task ownership, timeouts, retries, and cancellation.
- Prefer a small dependency graph to open-ended agent chatter.
- Preserve proposals and voting evidence before selecting a consensus result.
- Add traces and cost limits before increasing the number of agents.

The reference path is `src/phase5/13_message_passing.py` through `15_consensus.py`.

Powered by Aspiro · part of agents-from-scratch
