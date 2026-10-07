# Translation guide

Translations make the course useful to more builders, but technical accuracy matters more than speed. English is the source of truth; do not translate code identifiers, shell commands, file paths, or API names.

## Where translations live

- `i18n/<language>/README.md` contains a translated project overview.
- Future lesson translations should mirror `docs/phase-*/` under `i18n/<language>/docs/`.
- Keep the lesson number and slug recognizable so links remain easy to maintain.

## Workflow

1. Copy the English section and translate prose, headings, alt text, and explanations.
2. Preserve fenced code blocks, inline code, links to source, and warning/admonition structure.
3. Add the translator's language and review notes in the pull request.
4. Ask a fluent reviewer to check terminology, especially words for token, embedding, retrieval, tool, and guardrail.
5. Run the docs build and update the language switcher only when a landing page is available.

AI-assisted drafts are welcome, but they must receive human review. Do not invent claims about model quality or regional language coverage.
