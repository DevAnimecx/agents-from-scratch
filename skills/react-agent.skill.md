---
name: react-agent
description: Build and review a bounded ReAct agent from first principles.
---

# ReAct agent skill

Use this skill when a task needs a tool-using agent and the control loop should remain inspectable.

## Contract

1. Write the goal and the available tools as data.
2. Ask the model for either a validated action or a final answer.
3. Execute only a registered tool; append its result as an observation.
4. Stop on a final answer, an error policy, or a hard step budget.
5. Log the transcript without secrets.

Prefer the reference implementation in `src/phase4/10_react_agent.py`. Do not invent an unbounded `while True` loop, execute arbitrary code from model text, or hide tool errors.

Powered by Aspiro · part of agents-from-scratch
