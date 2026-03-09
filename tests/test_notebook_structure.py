"""
Auto-grading tests for Lab 4 — Notebook Structure
"""

import pytest
import json
import os

NOTEBOOK = os.path.join(os.path.dirname(__file__), "..", "lab4_technique_toolbox.ipynb")


def load_nb():
    if not os.path.exists(NOTEBOOK):
        pytest.skip("Notebook not found")
    with open(NOTEBOOK, "r", encoding="utf-8") as f:
        return json.load(f)


class TestNotebookExists:
    def test_exists(self):
        assert os.path.exists(NOTEBOOK)

    def test_valid(self):
        nb = load_nb()
        assert "cells" in nb
        assert len(nb["cells"]) >= 20


class TestNotebookContent:
    def test_executed(self):
        nb = load_nb()
        executed = sum(1 for c in nb["cells"]
                       if c.get("cell_type") == "code" and c.get("outputs"))
        assert executed >= 5, f"Only {executed} code cells executed"

    def test_has_phases(self):
        nb = load_nb()
        src = "\n".join("".join(c.get("source", [])) for c in nb["cells"])
        lower = src.lower()
        assert "phase 1" in lower or "free-form" in lower
        assert "phase 2" in lower or "format" in lower
        assert "phase 3" in lower or "few-shot" in lower

    def test_has_self_consistency(self):
        nb = load_nb()
        src = "\n".join("".join(c.get("source", [])) for c in nb["cells"])
        lower = src.lower()
        assert "self-consistency" in lower or "majority_vote" in lower
