#!/bin/bash
set -euo pipefail

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}  🏢 DOCORE ADK Installer v1.0.0${NC}"
echo -e "${GREEN}  16 AI Agents Orchestration for Claude Code${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

CLAUDE_DIR="${HOME}/.claude"
AGENTS_DIR="${CLAUDE_DIR}/agents"
COMMANDS_DIR="${CLAUDE_DIR}/commands"
SKILLS_DIR="${CLAUDE_DIR}/skills"

DOCORE_REPO="https://github.com/DoCoreTeam/docore.git"
GSTACK_REPO="https://github.com/garrytan/gstack.git"

# ── 1. Clone docore to temp ─────────────────────
echo -e "${BLUE}[1/4] Downloading DOCORE...${NC}"
TMP_DIR=$(mktemp -d)
trap "rm -rf $TMP_DIR" EXIT

git clone --depth 1 "$DOCORE_REPO" "$TMP_DIR/docore-repo" --quiet
SRC="${TMP_DIR}/docore-repo/docore"
echo -e "${GREEN}  ✅ Downloaded${NC}"

# ── 2. Install agents → ~/.claude/agents/ ───────
echo ""
echo -e "${BLUE}[2/4] Installing agents → ${AGENTS_DIR}/${NC}"
mkdir -p "$AGENTS_DIR"

for f in "${SRC}/agents/"*.md; do
    name=$(basename "$f")
    if [ -f "${AGENTS_DIR}/${name}" ]; then
        echo -e "${YELLOW}  ⟳ ${name} (update)${NC}"
    else
        echo -e "${GREEN}  ✅ ${name}${NC}"
    fi
    cp "$f" "${AGENTS_DIR}/${name}"
done

# ── 3. Install commands → ~/.claude/commands/ ───
echo ""
echo -e "${BLUE}[3/4] Installing commands → ${COMMANDS_DIR}/${NC}"
mkdir -p "$COMMANDS_DIR"

for f in "${SRC}/commands/"*.md; do
    name=$(basename "$f")
    if [ -f "${COMMANDS_DIR}/${name}" ]; then
        echo -e "${YELLOW}  ⟳ ${name} (update)${NC}"
    else
        echo -e "${GREEN}  ✅ ${name}${NC}"
    fi
    cp "$f" "${COMMANDS_DIR}/${name}"
done

# ── 4. Install skill → ~/.claude/skills/ceo-system/ ─
echo ""
echo -e "${BLUE}[4/4] Installing skills + registries...${NC}"
mkdir -p "${SKILLS_DIR}/ceo-system"
cp "${SRC}/skills/ceo-system/SKILL.md" "${SKILLS_DIR}/ceo-system/SKILL.md"
echo -e "${GREEN}  ✅ skills/ceo-system/SKILL.md${NC}"

# ── 5. CLAUDE.md → ~/.claude/CLAUDE.md ──────────
if [ -f "${CLAUDE_DIR}/CLAUDE.md" ]; then
    # Check if already installed
    if grep -q "DOCORE v" "${CLAUDE_DIR}/CLAUDE.md" 2>/dev/null; then
        echo -e "${YELLOW}  ⟳ CLAUDE.md — updating DOCORE section${NC}"
        # Remove old DOCORE block and re-append
        python3 - "${CLAUDE_DIR}/CLAUDE.md" "${SRC}/CLAUDE.md" <<'PYEOF'
import sys

existing = open(sys.argv[1]).read()
docore_new = open(sys.argv[2]).read()

# Remove old DOCORE block if present
start_marker = "# DOCORE"
if start_marker in existing:
    idx = existing.index(start_marker)
    existing = existing[:idx].rstrip() + "\n"

with open(sys.argv[1], 'w') as out:
    out.write(existing.rstrip() + "\n\n" + docore_new)
PYEOF
    else
        echo -e "${YELLOW}  ⟳ Appending to existing CLAUDE.md${NC}"
        echo "" >> "${CLAUDE_DIR}/CLAUDE.md"
        cat "${SRC}/CLAUDE.md" >> "${CLAUDE_DIR}/CLAUDE.md"
    fi
else
    cp "${SRC}/CLAUDE.md" "${CLAUDE_DIR}/CLAUDE.md"
    echo -e "${GREEN}  ✅ CLAUDE.md created${NC}"
fi

# ── 6. Registries → ~/.claude/ ──────────────────
mkdir -p "${CLAUDE_DIR}/reports"

for file in error-registry skill-registry project-registry decision-log; do
    if [ ! -f "${CLAUDE_DIR}/${file}.md" ]; then
        cp "${SRC}/templates/${file}.md" "${CLAUDE_DIR}/${file}.md"
        echo -e "${GREEN}  ✅ ${file}.md${NC}"
    else
        echo -e "${YELLOW}  ⏭️  ${file}.md already exists, skipping${NC}"
    fi
done

# ── 7. gstack (skip if already installed) ───────
GSTACK_DIR="${SKILLS_DIR}/gstack"
if [ -d "$GSTACK_DIR" ]; then
    echo -e "${YELLOW}  ⏭️  gstack already installed, skipping${NC}"
else
    echo -e "${GREEN}  Installing gstack...${NC}"
    git clone --depth 1 "$GSTACK_REPO" "$GSTACK_DIR" --quiet
    echo -e "${GREEN}  ✅ gstack installed${NC}"
fi

# ── Done ───────────────────────────────────────
echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}  ✅ DOCORE ADK installed successfully!${NC}"
echo ""
echo -e "  Installed to:"
echo -e "    ${YELLOW}~/.claude/agents/dc-*.md${NC}          ← 16 agents"
echo -e "    ${YELLOW}~/.claude/commands/ceo*.md${NC}        ← slash commands"
echo -e "    ${YELLOW}~/.claude/skills/ceo-system/${NC}      ← CEO orchestration"
echo -e "    ${YELLOW}~/.claude/CLAUDE.md${NC}               ← auto-loaded by Claude Code"
echo ""
echo -e "  🚀 ${YELLOW}Getting started:${NC}"
echo -e "     1. Open Claude Code in your project"
echo -e "     2. ${YELLOW}/ceo-init${NC}               Initialize project"
echo -e "     3. ${YELLOW}/ceo \"build a todo app\"${NC}   Start development"
echo ""
echo -e "  📋 Commands:"
echo -e "     ${YELLOW}/ceo \"task\"${NC}      Full pipeline (all 16 agents)"
echo -e "     ${YELLOW}/ceo-init${NC}        Project setup + harness"
echo -e "     ${YELLOW}/ceo-status${NC}      Show current status"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
