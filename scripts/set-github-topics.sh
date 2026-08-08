#!/usr/bin/env bash
# set-github-topics.sh
# Sets GitHub repository topics for DoCoreTeam/domangcha
# Requires: GitHub CLI (gh) authenticated with repo write access

set -euo pipefail

REPO="DoCoreTeam/domangcha"

echo "Setting GitHub topics for ${REPO}..."

gh repo edit "${REPO}" \
  --add-topic claude-code \
  --add-topic openai-codex \
  --add-topic graph-engineering \
  --add-topic workflow-engine \
  --add-topic ai-agents \
  --add-topic anthropic \
  --add-topic llm \
  --add-topic automation \
  --add-topic developer-tools \
  --add-topic cli \
  --add-topic ai \
  --add-topic multi-agent \
  --add-topic bash \
  --add-topic claude \
  --add-topic mcp \
  --add-topic productivity \
  --add-topic devtools \
  --add-topic agentic-ai \
  --add-topic code-generation \
  --add-topic workflow-automation \
  --add-topic open-source \
  --add-topic ai-automation \
  --add-topic shell

echo "GitHub topics set successfully for ${REPO}"
