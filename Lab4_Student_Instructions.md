# Lab 4 — Technique Toolbox

## Generative AI & Prompt Engineering — Practical Lab Series

**Module:** 4 — Mechanism-Based Prompting Techniques | **Duration:** 90 min | **Pair programming**

---

## Context

DevAssist needs to extract structured metadata from TaskFlow user stories and solve multi-step reasoning problems. Today you expand the Lab 3 contract framework with four techniques, each grounded in a mechanism you already understand.

## Learning Objectives

| ID | Objective |
|----|-----------|
| L4.1 | Design few-shot prompts with deliberate example selection |
| L4.2 | Apply CoT and explain its mechanism (intermediate tokens as context) |
| L4.3 | Implement self-consistency and quantify accuracy-vs-cost |
| L4.4 | Enforce structured output with format constraints + jsonschema |
| L4.5 | Select appropriate technique for a given task with mechanistic reasoning |

## Lab Structure (90 min)

| Phase | Time | Activity |
|-------|------|----------|
| Setup | 5 min | Load data, verify Ollama |
| Phase 1 | 15 min | Free-form extraction (zero-shot) |
| Phase 2 | 15 min | Format-constrained + jsonschema |
| Phase 3 | 15 min | Few-shot + format |
| Bonus | 10 min | CoT for ambiguous stories |
| Self-consistency | 20 min | n=1,3,5 + majority vote + chart |
| Wrap-up | 10 min | Technique selection guide |

## Deliverables

1. Completed notebook with all phases + self-consistency bench
2. Compliance comparison chart (3 phases)
3. Gain-vs-cost chart (self-consistency)
4. Technique selection guide (1 paragraph)

## Evaluation

| Criterion | Weight |
|-----------|--------|
| Prompt progression (3 phases) | 25% |
| Validation + compliance metrics | 20% |
| Self-consistency experiment + chart | 20% |
| Mechanistic analysis (M1–M4) | 25% |
| Technique selection reasoning | 10% |

---

*Lab 4 of 8 — DevAssist / TaskFlow Lab Series*
