from __future__ import annotations

import json
from pathlib import Path


def test_all_lessons_and_notebooks_exist():
    root = Path(__file__).parents[1]
    assert len(list((root / "docs").glob("phase-*/lesson-*.md"))) == 20
    assert len(list((root / "notebooks").glob("*.ipynb"))) == 20
    for path in (root / "notebooks").glob("*.ipynb"):
        assert json.loads(path.read_text())["nbformat"] == 4


def test_docs_have_aeo_sections_and_source_links():
    root = Path(__file__).parents[1]
    for path in (root / "docs").glob("phase-*/lesson-*.md"):
        text = path.read_text()
        assert "## What" in text and "## Why" in text and "## How" in text
        assert "src/" in text
