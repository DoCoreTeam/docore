#!/usr/bin/env bash
# Replace repository topics with the canonical 20-topic public metadata set.
set -euo pipefail

REPO="DoCoreTeam/domangcha"

gh api --method PUT "repos/${REPO}/topics" --input - <<'JSON'
{"names":["domangcha","claude-code","openai-codex","graph-engineering","loop-engineering","ai-agents","agent-orchestration","workflow-engine","developer-tools","cli","python","automation","multi-agent","checkpointing","human-in-the-loop","llm","code-generation","devtools","open-source","productivity"]}
JSON

echo "GitHub topics synchronized for ${REPO}"
