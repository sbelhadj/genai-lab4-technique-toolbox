# Lab 4 — Technique Toolbox

**Generative AI & Prompt Engineering — A Mechanistic Approach**

Module 4: Mechanism-Based Prompting Techniques | Duration: 90 minutes

---

## Overview

In this lab you build two mini-projects that demonstrate advanced prompting techniques:

1. **Structured Output Sprint** (55 min) — Extract structured metadata from TaskFlow user stories in three phases: free-form → format-constrained → few-shot. Measure compliance rates at each step and validate with `jsonschema`.

2. **Self-Consistency Mini-Bench** (20 min) — Run 20 logic/arithmetic problems at multiple sample counts (`n = 1, 3, 5`), apply majority voting, and chart the accuracy-vs-cost trade-off.

**Core principle:** *Every advanced technique exploits a specific mechanism. Few-shot = attention over patterns. CoT = intermediate tokens as new context. Self-consistency = sampling diversity + voting. Format constraints = structural token attention.*

---

## Quick Start

```bash
# Codespaces (recommended): click Code → Codespaces → Create codespace on main
# Local:
pip install requests pytest jsonschema jupyter matplotlib numpy nbformat
ollama serve & ollama pull llama3.2:3b
jupyter notebook
```

---

## Repository Structure

```
genai-lab4-technique-toolbox/
├── lab4_technique_toolbox.ipynb        # ← YOUR MAIN WORKSPACE (both parts)
├── utils/
│   ├── generation_utils.py             # generate(), generate_n()
│   ├── schema_validators.py            # jsonschema validation helpers
│   └── consistency_utils.py            # extract_final_answer(), majority_vote()
├── data/
│   ├── user_stories.json               # 15 TaskFlow user stories for extraction
│   ├── logic_problems.json             # 20 logic/arithmetic problems
│   └── precomputed_outputs.json        # Fallback outputs
├── tests/
│   ├── test_deliverables.py            # Auto-graded: notebook + analysis
│   └── test_schema_validators.py       # Auto-graded: validator functions
└── technique_report.md                 # ← YOUR DELIVERABLE: technique analysis
```

---

## Deliverables

| # | What | Where |
|---|------|-------|
| 1 | Completed notebook (both parts) | `lab4_technique_toolbox.ipynb` |
| 2 | Technique selection guide + analysis | `technique_report.md` |
| 3 | Gain-vs-cost chart | In notebook |
| 4 | Compliance rate comparison table | In notebook |

---

*Lab 4 of 8 — DevAssist / TaskFlow Lab Series*
