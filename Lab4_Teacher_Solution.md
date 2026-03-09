# Lab 4 — Teacher Solution

**CONFIDENTIAL**

## Expected Compliance Rates

| Phase | Rate | Why |
|-------|------|-----|
| Free-form | 0–5% | No format spec → mixed formats, none valid JSON |
| Format-constrained | 50–70% | Format tokens bias generation but fences/extra text break validation |
| Few-shot | 85–95% | Examples create strong attention anchors for structure + mapping |

## Mechanistic Justifications

| Transition | Mechanism |
|-----------|-----------|
| P1→P2 | Format tokens create attention patterns biasing toward matching structural tokens (M2) |
| P2→P3 | Few-shot examples place complete demos in context; attention replicates pattern (M2) |
| CoT | Intermediate tokens enter context window, helping disambiguate before extraction (M2) |
| Self-consistency | Temperature>0 creates diverse paths; majority vote favors correct answers (M1) |

## Self-Consistency Expected Results

- n=1: ~55%, n=3: ~65%, n=5: ~75%, n=7: ~75% (plateau)
- Sweet spot: n=3 or n=5
- Fails when model consistently wrong (all samples produce same wrong answer)

## Timing Risks

- Self-consistency takes longest (50+ generations for 10 problems × n=5)
- If behind: skip CoT bonus, reduce to n=1 and n=5 only

---

*CONFIDENTIAL — Teacher Solution Lab 4 of 8*
