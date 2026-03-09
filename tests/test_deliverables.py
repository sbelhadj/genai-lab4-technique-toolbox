"""Auto-grading: Lab 4 deliverable structure."""
import pytest, json, os

BASE = os.path.join(os.path.dirname(__file__), "..")
NOTEBOOK = os.path.join(BASE, "lab4_technique_toolbox.ipynb")
REPORT = os.path.join(BASE, "technique_report.md")

class TestFilesExist:
    def test_notebook(self): assert os.path.exists(NOTEBOOK)
    def test_report(self): assert os.path.exists(REPORT)

class TestNotebook:
    def test_valid(self):
        with open(NOTEBOOK) as f: nb = json.load(f)
        assert len(nb["cells"]) >= 20
    def test_executed(self):
        with open(NOTEBOOK) as f: nb = json.load(f)
        n = sum(1 for c in nb["cells"] if c.get("cell_type")=="code" and c.get("outputs"))
        assert n >= 6, f"Only {n} cells executed"

class TestReport:
    def test_not_template(self):
        with open(REPORT) as f: content = f.read()
        assert content.count("TODO") <= 5
    def test_has_mechanistic(self):
        with open(REPORT) as f: content = f.read().lower()
        found = [t for t in ["attention","token","pattern","context","sampling"] if t in content]
        assert len(found) >= 2
