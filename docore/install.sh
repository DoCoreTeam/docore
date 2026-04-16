#!/bin/bash
set -euo pipefail

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
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
ECC_REPO="https://github.com/affaan-m/everything-claude-code.git"

TMP_DIR=$(mktemp -d)
trap "rm -rf $TMP_DIR" EXIT

# ── 1. DOCORE ──────────────────────────────────
echo -e "${BLUE}[1/5] Downloading DOCORE...${NC}"
git clone --depth 1 "$DOCORE_REPO" "$TMP_DIR/docore-repo" --quiet
SRC="${TMP_DIR}/docore-repo/docore"
echo -e "${GREEN}  ✅ Downloaded${NC}"

# ── 2. Install agents → ~/.claude/agents/ ───────
echo ""
echo -e "${BLUE}[2/5] Installing agents → ~/.claude/agents/${NC}"
mkdir -p "$AGENTS_DIR"
for f in "${SRC}/agents/"*.md; do
    name=$(basename "$f")
    [ -f "${AGENTS_DIR}/${name}" ] && echo -e "${YELLOW}  ⟳ ${name}${NC}" || echo -e "${GREEN}  ✅ ${name}${NC}"
    cp "$f" "${AGENTS_DIR}/${name}"
done

# ── 3. Install commands → ~/.claude/commands/ ───
echo ""
echo -e "${BLUE}[3/5] Installing commands → ~/.claude/commands/${NC}"
mkdir -p "$COMMANDS_DIR"
for f in "${SRC}/commands/"*.md; do
    name=$(basename "$f")
    [ -f "${COMMANDS_DIR}/${name}" ] && echo -e "${YELLOW}  ⟳ ${name}${NC}" || echo -e "${GREEN}  ✅ ${name}${NC}"
    cp "$f" "${COMMANDS_DIR}/${name}"
done

# ── 4. Install CEO skill ─────────────────────────
echo ""
echo -e "${BLUE}[4/5] Installing CEO skill → ~/.claude/skills/ceo-system/${NC}"
mkdir -p "${SKILLS_DIR}/ceo-system"
cp "${SRC}/skills/ceo-system/SKILL.md" "${SKILLS_DIR}/ceo-system/SKILL.md"
echo -e "${GREEN}  ✅ ceo-system/SKILL.md${NC}"

# ── 5. CLAUDE.md → ~/.claude/CLAUDE.md ──────────
if [ -f "${CLAUDE_DIR}/CLAUDE.md" ]; then
    if grep -q "DOCORE v" "${CLAUDE_DIR}/CLAUDE.md" 2>/dev/null; then
        echo -e "${YELLOW}  ⟳ CLAUDE.md — updating DOCORE section${NC}"
        python3 - "${CLAUDE_DIR}/CLAUDE.md" "${SRC}/CLAUDE.md" <<'PYEOF'
import sys
existing = open(sys.argv[1]).read()
docore_new = open(sys.argv[2]).read()
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

# ── 6. Registries ───────────────────────────────
mkdir -p "${CLAUDE_DIR}/reports"
for file in error-registry skill-registry project-registry decision-log; do
    if [ ! -f "${CLAUDE_DIR}/${file}.md" ]; then
        cp "${SRC}/templates/${file}.md" "${CLAUDE_DIR}/${file}.md"
        echo -e "${GREEN}  ✅ ${file}.md${NC}"
    else
        echo -e "${YELLOW}  ⏭️  ${file}.md already exists, skipping${NC}"
    fi
done

# ── 7. ECC (Everything Claude Code) ─────────────
echo ""
echo -e "${BLUE}[5/5] Installing ECC (Everything Claude Code)...${NC}"
echo -e "      183 skills + 79 commands that agents rely on"

ECC_TMP="${TMP_DIR}/ecc"
git clone --depth 1 "$ECC_REPO" "$ECC_TMP" --quiet

# Install ECC skills → ~/.claude/skills/
INSTALLED_SKILLS=0
SKIPPED_SKILLS=0
for skill_dir in "${ECC_TMP}/skills"/*/; do
    skill_name=$(basename "$skill_dir")
    dest="${SKILLS_DIR}/${skill_name}"
    if [ -d "$dest" ]; then
        SKIPPED_SKILLS=$((SKIPPED_SKILLS + 1))
    else
        mkdir -p "$dest"
        cp -r "${skill_dir}"* "$dest/" 2>/dev/null || true
        INSTALLED_SKILLS=$((INSTALLED_SKILLS + 1))
    fi
done
echo -e "${GREEN}  ✅ Skills: ${INSTALLED_SKILLS} installed, ${SKIPPED_SKILLS} already present${NC}"

# Install ECC commands → ~/.claude/commands/
INSTALLED_CMDS=0
SKIPPED_CMDS=0
for cmd_file in "${ECC_TMP}/commands/"*.md; do
    cmd_name=$(basename "$cmd_file")
    dest="${COMMANDS_DIR}/${cmd_name}"
    if [ -f "$dest" ]; then
        SKIPPED_CMDS=$((SKIPPED_CMDS + 1))
    else
        cp "$cmd_file" "$dest"
        INSTALLED_CMDS=$((INSTALLED_CMDS + 1))
    fi
done
echo -e "${GREEN}  ✅ Commands: ${INSTALLED_CMDS} installed, ${SKIPPED_CMDS} already present${NC}"

# ── 8. gstack (skip if already installed) ────────
GSTACK_DIR="${SKILLS_DIR}/gstack"
if [ -d "$GSTACK_DIR" ]; then
    echo -e "${YELLOW}  ⏭️  gstack already installed, skipping${NC}"
else
    git clone --depth 1 "$GSTACK_REPO" "$GSTACK_DIR" --quiet
    echo -e "${GREEN}  ✅ gstack installed${NC}"
fi

# ── 9. Superpowers ───────────────────────────────
echo ""
echo -e "${BLUE}[Extra] Installing Superpowers...${NC}"
SUPERPOWERS_INSTALLED=false

# Method 1: Claude Code plugin CLI (claude plugin command)
if command -v claude &>/dev/null; then
    # Add marketplace source if not already added
    if claude plugin marketplace list 2>/dev/null | grep -q "obra/superpowers-marketplace"; then
        echo -e "${YELLOW}  ⏭️  superpowers-marketplace already registered${NC}"
    else
        claude plugin marketplace add obra/superpowers-marketplace 2>/dev/null && \
            echo -e "${GREEN}  ✅ Marketplace registered: obra/superpowers-marketplace${NC}" || \
            echo -e "${YELLOW}  ⚠️  Marketplace registration skipped (check Claude version)${NC}"
    fi

    # Install superpowers plugin
    if claude plugin list 2>/dev/null | grep -q "superpowers"; then
        echo -e "${YELLOW}  ⏭️  superpowers already installed, skipping${NC}"
        SUPERPOWERS_INSTALLED=true
    else
        claude plugin install superpowers@superpowers-marketplace 2>/dev/null && \
            SUPERPOWERS_INSTALLED=true && \
            echo -e "${GREEN}  ✅ superpowers installed via plugin system${NC}" || \
            echo -e "${YELLOW}  ⚠️  Plugin install unavailable, trying fallback...${NC}"
    fi
fi

# Method 2: Direct GitHub fallback
if [ "$SUPERPOWERS_INSTALLED" = false ]; then
    SUPERPOWERS_REPO="https://github.com/obra/superpowers.git"
    SUPERPOWERS_DIR="${SKILLS_DIR}/superpowers"
    if [ -d "$SUPERPOWERS_DIR" ]; then
        echo -e "${YELLOW}  ⏭️  superpowers already present at ${SUPERPOWERS_DIR}${NC}"
    else
        git clone --depth 1 "$SUPERPOWERS_REPO" "$SUPERPOWERS_DIR" --quiet 2>/dev/null && \
            echo -e "${GREEN}  ✅ superpowers cloned to ${SUPERPOWERS_DIR}${NC}" || \
            echo -e "${YELLOW}  ⚠️  superpowers not available — install manually:${NC}"
            echo -e "      ${YELLOW}/plugin marketplace add obra/superpowers-marketplace${NC}"
            echo -e "      ${YELLOW}/plugin install superpowers@superpowers-marketplace${NC}"
    fi
fi

# ── Done ─────────────────────────────────────────
echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}  ✅ DOCORE ADK installed successfully!${NC}"
echo ""
echo -e "  Installed to:"
echo -e "    ${YELLOW}~/.claude/agents/dc-*.md${NC}          ← 16 DOCORE agents"
echo -e "    ${YELLOW}~/.claude/commands/ceo*.md${NC}        ← /ceo /ceo-init /ceo-status"
echo -e "    ${YELLOW}~/.claude/skills/ceo-system/${NC}      ← CEO orchestration brain"
echo -e "    ${YELLOW}~/.claude/skills/ecc:*/  ${NC}         ← 183 ECC skills"
echo -e "    ${YELLOW}~/.claude/commands/ecc:* ${NC}         ← 79 ECC commands"
echo -e "    ${YELLOW}~/.claude/skills/gstack/ ${NC}         ← gstack tools"
echo -e "    ${YELLOW}~/.claude/skills/superpowers/${NC}     ← superpowers (or via plugin)"
echo -e "    ${YELLOW}~/.claude/CLAUDE.md${NC}               ← auto-loaded by Claude Code"
echo ""
echo -e "  🚀 ${YELLOW}Getting started:${NC}"
echo -e "     1. Open Claude Code in any project"
echo -e "     2. ${YELLOW}/ceo-init${NC}               Initialize project"
echo -e "     3. ${YELLOW}/ceo \"build a todo app\"${NC}   Start full pipeline"
echo ""
echo -e "  📋 Commands:"
echo -e "     ${YELLOW}/ceo \"task\"${NC}      Full pipeline (16 agents)"
echo -e "     ${YELLOW}/ceo-init${NC}        Project setup + harness"
echo -e "     ${YELLOW}/ceo-status${NC}      Show current status"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
