---
name: ceo-agents
description: Logical DOMANGCHA role catalog backed by the canonical agent manifest.
---

# DOMANGCHA Agent Roles

`manifests/agents.json` is authoritative for IDs, groups, and ModelPolicy intent. `agents/dc-*.md` contains provider adapter prompts.

- PLANNER: DC-ANA, DC-BIZ, DC-RES, DC-OSS, DC-KNW
- GENERATOR: DC-DEV-BE, DC-DEV-DB, DC-DEV-FE, DC-DEV-INT, DC-DEV-MOB, DC-DEV-OPS, DC-DOC, DC-WRT, DC-SEO
- EVALUATOR: DC-QA, DC-SEC, DC-REV
- SUPPORT: DC-TOK

Agent roles are optional graph/loop nodes selected by task need. Do not fan out in DIRECT. A writer cannot be the sole reviewer of meaningful implementation. Runtime adapters map roles to native capabilities; never assume Claude `Agent(...)` syntax exists elsewhere.
