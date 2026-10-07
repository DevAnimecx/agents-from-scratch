# Contributing to agents-from-scratch

Thanks for helping make the agent pipeline easier to understand. This repository values small, runnable explanations over clever abstractions.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
ruff check .
pytest
```

Python 3.11 or newer is required. Core lessons should run without credentials or network access.

## Add a lesson or improvement

1. Open an issue or choose an existing issue with a clear scope.
2. Add the source implementation, a focused test, and a docs page with **What**, **Why**, and **How** sections.
3. Keep optional provider dependencies out of module import paths; document them in `pyproject.toml` and the lesson.
4. Run `ruff check . && pytest` and include the result in the pull request.
5. Explain the invariant your code teaches and the failure mode it makes visible.

## Content standards

- Prefer deterministic examples and tiny corpora.
- Never commit API keys, personal data, generated site output, or large datasets.
- Show the raw mechanism before the framework comparison.
- Treat model output as untrusted data: validate tool names and arguments.
- Use inclusive, respectful examples; translations should be reviewed by a fluent speaker.

## Commit and pull request guide

Use a focused commit such as `lesson 10: add bounded react loop`. Pull requests should state what changed, how it was tested, and whether an optional dependency is involved. A maintainer may ask for a regression test or a simpler explanation.

## Code of conduct

Be kind, specific, and curious. Critique code and explanations, not people. Harassment, discrimination, doxxing, and unwanted contact are not welcome.
