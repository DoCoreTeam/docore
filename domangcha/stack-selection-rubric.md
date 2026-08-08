# Adaptive Routing Rubric

This file documents the deterministic score implemented by `orchestration/router.py`. The code is authoritative.

| Signal | Score |
|---|---:|
| mutation | +2 |
| 2–3 files | +1 |
| 4–7 files | +3 |
| 8+ files | +5 |
| iteration/test correction | +2 |
| external integration | +3 |
| database/schema | +4 |
| auth/security | +5 |
| public breaking risk | +5 |
| independent branches | +4 |
| checkpoint/HITL | +5 |
| read-only deterministic task | −5 |

Default boundaries are DIRECT ≤1, LOOP 2–6, GRAPH ≥7. Hard invariants override scores. gstack, Superpowers, ECC, browser tools, and agent roles are node capabilities—not competing routing stacks.
