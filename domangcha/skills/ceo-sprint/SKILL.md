---
name: ceo-sprint
description: Compatibility facade for graph execution and validation profiles.
---

# CEO Sprint Compatibility Facade

Former sprint phases map to the versioned `graphs/full_pipeline.json` definition. Nodes, edges, retries, joins, and terminal states are enforced by `orchestration/graph.py`.

Planner/generator/evaluator roles remain reusable logical AgentRoles. Writer/reviewer identity separation is validated from execution records.
