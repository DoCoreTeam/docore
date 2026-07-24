#!/bin/bash
set -euo pipefail

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
WHITE='\033[1;37m'
BOLD='\033[1m'
DIM='\033[2m'
NC='\033[0m'

CLAUDE_DIR="${HOME}/.claude"
AGENTS_DIR="${CLAUDE_DIR}/agents"
COMMANDS_DIR="${CLAUDE_DIR}/commands"
SKILLS_DIR="${CLAUDE_DIR}/skills"

DOMANGCHA_REPO="https://github.com/DoCoreTeam/domangcha.git"
GSTACK_REPO="https://github.com/garrytan/gstack.git"
ECC_REPO="https://github.com/affaan-m/everything-claude-code.git"

TMP_DIR=$(mktemp -d)
trap "rm -rf $TMP_DIR" EXIT

TOTAL_STEPS=13
CURRENT_STEP=0

# ── progress bar ─────────────────────────────────
step() {
    CURRENT_STEP=$((CURRENT_STEP + 1))
    local label_ko="$1"
    local label_en="$2"
    local filled=$((CURRENT_STEP * 20 / TOTAL_STEPS))
    local empty=$((20 - filled))
    local bar="${GREEN}${BOLD}"
    for i in $(seq 1 $filled); do bar="${bar}█"; done
    bar="${bar}${DIM}"
    for i in $(seq 1 $empty); do bar="${bar}░"; done
    bar="${bar}${NC}"
    echo ""
    printf "  ${CYAN}[%d/%d]${NC} ${WHITE}${BOLD}%-28s${NC}${DIM} / %s${NC}\n" \
        "$CURRENT_STEP" "$TOTAL_STEPS" "$label_ko" "$label_en"
    printf "  %b  ${DIM}%d%%${NC}\n" "$bar" "$((CURRENT_STEP * 100 / TOTAL_STEPS))"
}

# ── spinner ───────────────────────────────────────
spin() {
    local pid=$! frames='⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏' i=0
    while kill -0 $pid 2>/dev/null; do
        printf "\r  ${CYAN}${frames:$((i % ${#frames})):1}${NC}  ${DIM}%s${NC}" "$1"
        sleep 0.1
        i=$((i + 1))
    done
    printf "\r  ${GREEN}✔${NC}  %-40s\n" "$1"
}

# ── helper: git update-or-clone ──────────────────
git_update_or_clone() {
    local repo="$1" dest="$2" label="$3"
    if [ -d "${dest}/.git" ]; then
        echo -e "${YELLOW}  ⟳ ${label} — 최신 버전으로 업데이트 / pulling latest${NC}"
        git -C "$dest" fetch --depth 1 origin --quiet
        git -C "$dest" reset --hard origin/HEAD --quiet
    elif [ -d "$dest" ]; then
        echo -e "${YELLOW}  ⟳ ${label} — 재클론 중 / re-cloning${NC}"
        rm -rf "$dest"
        git clone --depth 1 "$repo" "$dest" --quiet
    else
        echo -e "${GREEN}  ✅ ${label} — 신규 설치 / fresh install${NC}"
        git clone --depth 1 "$repo" "$dest" --quiet
    fi
}

# ── 1. DOMANGCHA download ─────────────────────────
clear
echo ""
echo -e "${CYAN}${BOLD}"
echo "  ██████╗  ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗ ██████╗  ██████╗ ██╗  ██╗ █████╗ "
echo "  ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗████╗  ██║██╔════╝ ██╔════╝ ██║  ██║██╔══██╗"
echo "  ██║  ██║██║   ██║██╔████╔██║███████║██╔██╗ ██║██║  ███╗██║      ███████║███████║"
echo "  ██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██║      ██╔══██║██╔══██║"
echo "  ██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝╚██████╗ ██║  ██║██║  ██║"
echo "  ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝"
echo -e "${NC}"
echo -e "${WHITE}${BOLD}  돔황차 — 개발 지옥에서 도망쳐  🚗💨${NC}"
echo -e "${DIM}  Your AI getaway car from development hell.${NC}"
echo ""
echo -e "  ${MAGENTA}${BOLD}AI 개발 자동화 도구${NC}  ${DIM}·${NC}  ${MAGENTA}AI Development Automation Tool${NC}"
echo -e "  ${DIM}손코딩에서 도망쳐 — 18명 AI 크루가 대신 짭니다${NC}"
echo -e "  ${DIM}Escape hand-coding — a 18-agent AI crew builds for you${NC}"
echo ""
echo -e "${DIM}  ──────────────────────────────────────────────────────${NC}"
echo -e "  ${DIM}재설치 / Reinstall:${NC}  ${CYAN}npx domangcha${NC}"
echo -e "  ${DIM}또는 / or:${NC}  ${DIM}curl -sSL https://raw.githubusercontent.com/DoCoreTeam/domangcha/main/domangcha/install.sh | bash${NC}"
echo -e "${DIM}  ──────────────────────────────────────────────────────${NC}"
echo -e "  ${DIM}설치를 시작합니다 / Starting installation...${NC}"
echo ""
( git clone --depth 1 "$DOMANGCHA_REPO" "$TMP_DIR/domangcha-repo" --quiet ) & spin "DOMANGCHA 다운로드 중 / Downloading..."
SRC="${TMP_DIR}/domangcha-repo/domangcha"
DOMANGCHA_VERSION=$(cat "${SRC}/VERSION" 2>/dev/null || echo "unknown")

# ── 2. Agents ────────────────────────────────────
step "에이전트 18명 설치" "Installing 18 agents"
mkdir -p "$AGENTS_DIR"
agent_new=0; agent_up=0
for f in "${SRC}/agents/"*.md; do
    name=$(basename "$f")
    if [ -f "${AGENTS_DIR}/${name}" ]; then
        agent_up=$((agent_up + 1))
    else
        agent_new=$((agent_new + 1))
    fi
    cp "$f" "${AGENTS_DIR}/${name}"
done
echo -e "  ${GREEN}✔${NC}  ${GREEN}${agent_new}개 신규(new)${NC}  ${YELLOW}${agent_up}개 업데이트(updated)${NC}  ${DIM}→ ~/.claude/agents/${NC}"

# ── 3. Commands ───────────────────────────────────
step "명령어 설치" "Installing commands"
mkdir -p "$COMMANDS_DIR"
cmd_new=0; cmd_up=0
for f in "${SRC}/commands/"*.md; do
    name=$(basename "$f")
    if [ -f "${COMMANDS_DIR}/${name}" ]; then
        cmd_up=$((cmd_up + 1))
    else
        cmd_new=$((cmd_new + 1))
    fi
    cp "$f" "${COMMANDS_DIR}/${name}"
done
echo -e "  ${GREEN}✔${NC}  ${GREEN}${cmd_new}개 신규(new)${NC}  ${YELLOW}${cmd_up}개 업데이트(updated)${NC}  ${DIM}→ ~/.claude/commands/${NC}"

# ── 4. CEO skill ──────────────────────────────────
step "CEO 스킬 설치" "Installing CEO skill"
mkdir -p "${SKILLS_DIR}/ceo-system"
cp "${SRC}/skills/ceo-system/SKILL.md" "${SKILLS_DIR}/ceo-system/SKILL.md"
echo -e "  ${GREEN}✔${NC}  ceo-system/SKILL.md  ${DIM}→ ~/.claude/skills/ceo-system/${NC}"

# insane-search (vendored, MIT — fivetaku/insane-search): 차단 사이트 우회 리더
if [ -d "${SRC}/skills/insane-search" ]; then
    rm -rf "${SKILLS_DIR}/insane-search"
    mkdir -p "${SKILLS_DIR}/insane-search"
    cp -r "${SRC}/skills/insane-search/"* "${SKILLS_DIR}/insane-search/"
    echo -e "  ${GREEN}✔${NC}  insane-search/  ${DIM}→ ~/.claude/skills/insane-search/ (DC-RES·DC-OSS 차단 우회)${NC}"
fi

# ── 5. CLAUDE.md ──────────────────────────────────
step "CLAUDE.md 업데이트" "Updating CLAUDE.md"
if [ -f "${CLAUDE_DIR}/CLAUDE.md" ]; then
    if grep -qE "^# (docrew|DOCORE|DOMANGCHA|CEO) v" "${CLAUDE_DIR}/CLAUDE.md" 2>/dev/null; then
        echo -e "${YELLOW}  ⟳ CLAUDE.md — DOMANGCHA 섹션 갱신 / updating DOMANGCHA section${NC}"
        python3 - "${CLAUDE_DIR}/CLAUDE.md" "${SRC}/CLAUDE.md" <<'PYEOF'
import sys, re
existing = open(sys.argv[1]).read()
docore_new = open(sys.argv[2]).read()
# Match any of the possible section headers
match = re.search(r'^# (docrew|DOCORE|DOMANGCHA|CEO) v', existing, re.MULTILINE)
if match:
    existing = existing[:match.start()].rstrip() + "\n"
with open(sys.argv[1], 'w') as out:
    out.write(existing.rstrip() + "\n\n" + docore_new)
PYEOF
    else
        echo -e "  ${YELLOW}⟳${NC}  기존 CLAUDE.md 갱신 / updating existing CLAUDE.md"
        echo "" >> "${CLAUDE_DIR}/CLAUDE.md"
        cat "${SRC}/CLAUDE.md" >> "${CLAUDE_DIR}/CLAUDE.md"
    fi
else
    cp "${SRC}/CLAUDE.md" "${CLAUDE_DIR}/CLAUDE.md"
    echo -e "  ${GREEN}✔${NC}  CLAUDE.md 생성 완료 / created"
fi

# ── 5. Memory sync (rule refresh) ────────────────
# Runs early — before ECC/gstack/Playwright — so it is never skipped by set -e
step "메모리 동기화 (규칙 최신화)" "Memory sync (rule refresh)"
if [ -d "${SRC}/memory-templates" ]; then
    MEMORY_SYNCED=0
    for memory_dir in "${CLAUDE_DIR}/projects"/*/memory/; do
        [ -d "$memory_dir" ] || continue
        for template in "${SRC}/memory-templates/rule_"*.md; do
            [ -f "$template" ] || continue
            fname=$(basename "$template")
            cp "$template" "${memory_dir}/${fname}"
            MEMORY_SYNCED=$((MEMORY_SYNCED + 1))
        done
        # Update MEMORY.md index entries for overwritten rule files
        if [ -f "${memory_dir}/MEMORY.md" ]; then
            python3 - "${memory_dir}" "${SRC}/memory-templates/" <<'PYEOF'
import sys, os, re
memory_dir, templates_dir = sys.argv[1], sys.argv[2]
memory_md = os.path.join(memory_dir, "MEMORY.md")
content = open(memory_md).read()
for fname in sorted(os.listdir(templates_dir)):
    if not fname.startswith("rule_") or not fname.endswith(".md"):
        continue
    tmpl = open(os.path.join(templates_dir, fname)).read()
    name_m = re.search(r'^name:\s*(.+)$', tmpl, re.MULTILINE)
    desc_m = re.search(r'^description:\s*(.+)$', tmpl, re.MULTILINE)
    if not name_m or not desc_m:
        continue
    new_name = name_m.group(1).strip()
    new_desc = desc_m.group(1).strip()
    replacement = f'- [{new_name}]({fname}) — {new_desc}'
    pattern = r'- \[[^\]]+\]\(' + re.escape(fname) + r'\) — .+'
    if re.search(pattern, content):
        content = re.sub(pattern, lambda m: replacement, content)
    else:
        if not content.endswith('\n'):
            content += '\n'
        content += replacement + '\n'
open(memory_md, 'w').write(content)
PYEOF
        fi
    done
    echo -e "  ${GREEN}✔${NC}  ${MEMORY_SYNCED}개 규칙 메모리 최신화 / ${MEMORY_SYNCED} rule memories refreshed"
else
    echo -e "  ${YELLOW}⚠${NC}  memory-templates 없음 / skipping"
fi

# ── 6. Registries ─────────────────────────────────
step "레지스트리 초기화" "Initializing registries"
mkdir -p "${CLAUDE_DIR}/reports"
# Init knowledge-registry if not exists
KNW_REGISTRY="${SRC}/knowledge-registry"
if [ ! -d "${KNW_REGISTRY}" ]; then
    mkdir -p "${KNW_REGISTRY}"/{error,pattern,decision,workflow,skill,.knw-queue}
    echo -e "  ${GREEN}✔${NC}  knowledge-registry 초기화 / knowledge-registry initialized"
else
    echo -e "  ${DIM}·${NC}  knowledge-registry 이미 존재 / already exists"
fi
for file in error-registry skill-registry project-registry decision-log; do
    if [ ! -f "${CLAUDE_DIR}/${file}.md" ]; then
        cp "${SRC}/templates/${file}.md" "${CLAUDE_DIR}/${file}.md"
        echo -e "  ${GREEN}✔${NC}  ${file}.md  ${DIM}신규(new)${NC}"
    else
        echo -e "  ${YELLOW}⏭${NC}  ${file}.md  ${DIM}보존(preserved — user data)${NC}"
    fi
done

# Auto-add docs/*/ to user's project .gitignore (opt-out: DOMANGCHA_SKIP_GITIGNORE=1)
if [ "${DOMANGCHA_SKIP_GITIGNORE:-0}" = "1" ]; then
    echo -e "  ${DIM}·${NC}  .gitignore 자동 추가 비활성화됨 / auto-gitignore disabled"
else
    USER_GIT_ROOT=$(git rev-parse --show-toplevel 2>/dev/null || true)
    if [ -z "$USER_GIT_ROOT" ]; then
        echo -e "  ${DIM}·${NC}  git 레포 없음 — .gitignore 건너뜀 / no git repo"
    elif [ "$USER_GIT_ROOT" = "$HOME" ]; then
        echo -e "  ${YELLOW}⏭${NC}  cwd가 \$HOME — .gitignore 건너뜀 / skipping (\$HOME)"
    elif [ -f "${USER_GIT_ROOT}/domangcha/VERSION" ]; then
        echo -e "  ${YELLOW}⏭${NC}  DOMANGCHA 레포 자체 — 건너뜀 / skipping (DOMANGCHA repo)"
    else
        GITIGNORE_PATH="${USER_GIT_ROOT}/.gitignore"
        if [ -f "$GITIGNORE_PATH" ] && grep -qE "^/?docs/(\*|\*\*)/?$" "$GITIGNORE_PATH"; then
            echo -e "  ${YELLOW}⏭${NC}  .gitignore — docs 패턴 존재 / docs pattern present (${GITIGNORE_PATH})"
        else
            printf '\n# DOMANGCHA: user planning docs (local only)\ndocs/*/\n' >> "$GITIGNORE_PATH"
            echo -e "  ${GREEN}✔${NC}  .gitignore — docs/*/ 추가 / added (${GITIGNORE_PATH})"
        fi
        # Untrack already-tracked docs/ subdirs (safe on both fresh install and update)
        TRACKED_SUBDIRS=$(git -C "$USER_GIT_ROOT" -c core.quotepath=false ls-files "docs/" 2>/dev/null \
            | grep -E "^docs/[^/]+/" \
            | sed 's|docs/\([^/]*\)/.*|docs/\1|' \
            | sort -u || true)
        if [ -n "$TRACKED_SUBDIRS" ]; then
            echo "$TRACKED_SUBDIRS" | while IFS= read -r subdir; do
                git -C "$USER_GIT_ROOT" rm -r --cached "$subdir" 2>/dev/null || true
            done
            echo -e "  ${GREEN}✔${NC}  docs/ 하위 폴더 언트래킹 완료 / untracked existing docs/ subdirs"
        fi
    fi
fi

# ── 7. ECC ────────────────────────────────────────
step "ECC 183개 스킬 설치" "Installing 183 ECC skills"
echo -e "  ${DIM}명령어 제외 — /ceo-* 오케스트레이터로 접근 / commands excluded — use /ceo-* orchestrators${NC}"

ECC_TMP="${TMP_DIR}/ecc"
git clone --depth 1 "$ECC_REPO" "$ECC_TMP" --quiet

UPDATED_SKILLS=0
NEW_SKILLS=0
for skill_dir in "${ECC_TMP}/skills"/*/; do
    skill_name=$(basename "$skill_dir")
    dest="${SKILLS_DIR}/${skill_name}"
    if [ -d "$dest" ]; then
        rm -rf "$dest"
        UPDATED_SKILLS=$((UPDATED_SKILLS + 1))
    else
        NEW_SKILLS=$((NEW_SKILLS + 1))
    fi
    mkdir -p "$dest"
    cp -r "${skill_dir}"* "$dest/" 2>/dev/null || true
done
echo -e "  ${GREEN}✔${NC}  ECC 스킬 완료 / Skills done: ${GREEN}${NEW_SKILLS} 신규(new)${NC}  ${YELLOW}${UPDATED_SKILLS} 업데이트(updated)${NC}"

# ── 8. gstack ─────────────────────────────────────
step "gstack 업데이트" "Updating gstack"
( git_update_or_clone "$GSTACK_REPO" "${SKILLS_DIR}/gstack" "gstack" 2>&1 ) & spin "gstack 동기화 중 / Syncing gstack..."

# ── 9. Superpowers ────────────────────────────────
step "Superpowers 설치 (필수)" "Installing Superpowers (required)"
SUPERPOWERS_INSTALLED=false

# Method 1: Claude Code plugin CLI
if command -v claude &>/dev/null; then
    if claude plugin marketplace list 2>/dev/null | grep -q "obra/superpowers-marketplace"; then
        echo -e "  ${YELLOW}⟳${NC}  superpowers-marketplace 이미 등록됨 / already registered"
    else
        claude plugin marketplace add obra/superpowers-marketplace 2>/dev/null && \
            echo -e "${GREEN}  ✅ Marketplace registered: obra/superpowers-marketplace${NC}" || true
    fi

    if claude plugin list 2>/dev/null | grep -q "superpowers"; then
        claude plugin update superpowers 2>/dev/null && \
            echo -e "${GREEN}  ✅ superpowers updated via plugin${NC}" || \
            echo -e "${YELLOW}  ⟳ superpowers already up to date${NC}"
        SUPERPOWERS_INSTALLED=true
    else
        claude plugin install superpowers@superpowers-marketplace 2>/dev/null && \
            SUPERPOWERS_INSTALLED=true && \
            echo -e "${GREEN}  ✅ superpowers installed via plugin${NC}" || true
    fi
fi

# Method 2: GitHub fallback
if [ "$SUPERPOWERS_INSTALLED" = false ]; then
    SUPERPOWERS_REPO="https://github.com/obra/superpowers.git"
    git_update_or_clone "$SUPERPOWERS_REPO" "${SKILLS_DIR}/superpowers" "superpowers" 2>/dev/null && \
        SUPERPOWERS_INSTALLED=true || true
fi

# REQUIRED — fail loudly if not installed
if [ "$SUPERPOWERS_INSTALLED" = false ]; then
    echo ""
    echo -e "${RED}  ╔══════════════════════════════════════════╗${NC}"
    echo -e "${RED}  ║  ❌  SUPERPOWERS 설치 실패 / FAILED     ║${NC}"
    echo -e "${RED}  ║  CEO 작동에 필수 / Required for CEO     ║${NC}"
    echo -e "${RED}  ╚══════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "  Claude Code 내에서 수동 설치 / Install manually inside Claude Code:"
    echo -e "    \033[1;33m/plugin marketplace add obra/superpowers-marketplace\033[0m"
    echo -e "    \033[1;33m/plugin install superpowers@superpowers-marketplace\033[0m"
    exit 1
fi

# ── 10. Hooks ─────────────────────────────────────
step "훅 설치 (자동 테스트 + CEO 검토)" "Installing hooks (auto-test + CEO review)"
mkdir -p "${CLAUDE_DIR}/hooks"
cp "${SRC}/hooks/domangcha-post-edit.sh" "${CLAUDE_DIR}/hooks/domangcha-post-edit.sh"
cp "${SRC}/hooks/domangcha-stop.sh"      "${CLAUDE_DIR}/hooks/domangcha-stop.sh"
cp "${SRC}/hooks/domangcha-ceo-enforcer.py" "${CLAUDE_DIR}/hooks/domangcha-ceo-enforcer.py"
cp "${SRC}/hooks/domangcha-ralph-loop.py" "${CLAUDE_DIR}/hooks/domangcha-ralph-loop.py"
chmod +x "${CLAUDE_DIR}/hooks/domangcha-post-edit.sh"
chmod +x "${CLAUDE_DIR}/hooks/domangcha-stop.sh"
chmod +x "${CLAUDE_DIR}/hooks/domangcha-ceo-enforcer.py"
chmod +x "${CLAUDE_DIR}/hooks/domangcha-ralph-loop.py"
echo -e "  ${GREEN}✔${NC}  domangcha-post-edit.sh  ${DIM}자동 테스트+수정 / auto-test + auto-fix${NC}"
echo -e "  ${GREEN}✔${NC}  domangcha-stop.sh        ${DIM}CEO 품질 검토 / CEO quality review${NC}"
echo -e "  ${GREEN}✔${NC}  domangcha-ceo-enforcer.py  ${DIM}CEO 파이프라인 강제 / pipeline enforcer${NC}"
echo -e "  ${GREEN}✔${NC}  domangcha-ralph-loop.py  ${DIM}ralph 자율 루프 엔진 / ralph loop engine${NC}"

# ── 11. settings.json ─────────────────────────────
step "settings.json 훅 주입" "Injecting hooks into settings.json"
python3 - "${CLAUDE_DIR}" <<'PYEOF'
import sys, json, os

claude_dir = sys.argv[1]
hooks_dir  = os.path.join(claude_dir, "hooks")
settings_path = os.path.join(claude_dir, "settings.json")

DOMANGCHA_POST = {
    "matcher": "Write|Edit|MultiEdit",
    "hooks": [{"type": "command", "command": f'bash "{hooks_dir}/domangcha-post-edit.sh"'}]
}
# async: true — CEO quality review runs in background so session ends immediately
DOMANGCHA_STOP = {
    "hooks": [{"type": "command", "command": f'bash "{hooks_dir}/domangcha-stop.sh"', "timeout": 120, "async": True}]
}
# ralph loop engine — BLOCKING (no async) so exit 2 can force loop continuation
DOMANGCHA_RALPH_LOOP = {
    "hooks": [{"type": "command", "command": f'python3 "{hooks_dir}/domangcha-ralph-loop.py"', "timeout": 30}]
}
DOMANGCHA_ENFORCER = {
    "matcher": "",
    "hooks": [{"type": "command", "command": f'python3 "{hooks_dir}/domangcha-ceo-enforcer.py"'}]
}
# domangcha-stop-checks.js: TypeScript check + Playwright smoke test (ECC plugin)
# Runs FIRST so it can read the edited-files accumulator before format-typecheck clears it
DOMANGCHA_STOP_CHECKS_PATH = os.path.join(claude_dir, "scripts", "hooks", "domangcha-stop-checks.js")
DOMANGCHA_STOP_CHECKS = {
    "matcher": "*",
    "hooks": [{"type": "command", "command": f'node "{DOMANGCHA_STOP_CHECKS_PATH}"', "timeout": 120}],
    "description": "DOMANGCHA Stop Guard: TypeScript BLOCKING check + Playwright smoke test"
} if os.path.exists(DOMANGCHA_STOP_CHECKS_PATH) else None

settings = {}
if os.path.exists(settings_path):
    try:
        with open(settings_path) as f:
            settings = json.load(f)
    except Exception:
        settings = {}

hooks = settings.get("hooks", {})

# UserPromptSubmit — CEO pipeline enforcer (idempotent)
upr = hooks.get("UserPromptSubmit", [])
upr = [h for h in upr if not any("domangcha-ceo-enforcer" in sub.get("command","") for sub in h.get("hooks",[]))]
upr.insert(0, DOMANGCHA_ENFORCER)
hooks["UserPromptSubmit"] = upr

# PostToolUse — remove old DOMANGCHA hook, append fresh
post = hooks.get("PostToolUse", [])
post = [h for h in post if not any("domangcha-post-edit" in sub.get("command","") for sub in h.get("hooks",[]))]
post.append(DOMANGCHA_POST)
hooks["PostToolUse"] = post

# Stop — remove old DOMANGCHA hooks, re-inject in correct order
stop = hooks.get("Stop", [])
stop = [h for h in stop if not any(
    ("domangcha-stop" in sub.get("command","") or "domangcha-ralph-loop" in sub.get("command",""))
    for sub in h.get("hooks",[])
)]
if DOMANGCHA_STOP_CHECKS:
    stop.insert(0, DOMANGCHA_STOP_CHECKS)
stop.append(DOMANGCHA_RALPH_LOOP)  # ralph engine (blocking) — must run to force loop
stop.append(DOMANGCHA_STOP)
hooks["Stop"] = stop

settings["hooks"] = hooks
with open(settings_path, "w") as f:
    json.dump(settings, f, indent=2)
print("  ✔  settings.json 훅 주입 완료 / hooks injected (merged safely)")
PYEOF

# ── 12. Playwright (폴백 — 기본은 Claude-in-Chrome 확장) ──
step "Playwright MCP 설정 (브라우저 검증 폴백)" "Setting up Playwright MCP (browser-verify fallback)"
bash "${SRC}/hooks/domangcha-playwright-setup.sh"

# ── 13. Git hooks ─────────────────────────────────
step "git 훅 설치 (자동 재설치)" "Installing git hooks (auto-reinstall)"
# Find the git repo root that contains domangcha/ (works from any working dir)
GIT_REPO=$(git -C "$(dirname "${SRC}")" rev-parse --show-toplevel 2>/dev/null || true)
if [ -n "$GIT_REPO" ]; then
    GIT_HOOKS_DIR="${GIT_REPO}/.git/hooks"
    mkdir -p "$GIT_HOOKS_DIR"

    # post-merge: fires after `git pull` merges changes
    cat > "${GIT_HOOKS_DIR}/post-merge" << 'HOOK_EOF'
#!/bin/bash
# Auto-reinstall DOMANGCHA when repo is updated via git pull
INSTALL_SH="$(git rev-parse --show-toplevel)/domangcha/install.sh"
if [ -f "$INSTALL_SH" ]; then
    echo "[DOMANGCHA] 업데이트 감지 — 재설치 중..."
    bash "$INSTALL_SH"
fi
HOOK_EOF

    # post-checkout: fires after `git clone` (initial checkout)
    cat > "${GIT_HOOKS_DIR}/post-checkout" << 'HOOK_EOF'
#!/bin/bash
# Auto-install DOMANGCHA on first checkout (git clone)
PREV_HEAD=$1
NEW_HEAD=$2
IS_BRANCH_CHECKOUT=$3
# Only fire on branch checkout (IS_BRANCH_CHECKOUT=1), not file checkout
[ "$IS_BRANCH_CHECKOUT" != "1" ] && exit 0
INSTALL_SH="$(git rev-parse --show-toplevel)/domangcha/install.sh"
if [ -f "$INSTALL_SH" ]; then
    echo "[DOMANGCHA] 체크아웃 감지 — 설치 중..."
    bash "$INSTALL_SH"
fi
HOOK_EOF

    chmod +x "${GIT_HOOKS_DIR}/post-merge"
    chmod +x "${GIT_HOOKS_DIR}/post-checkout"
    echo -e "  ${GREEN}✔${NC}  post-merge  ${DIM}git pull 시 자동 재설치 / auto-reinstall on git pull${NC}"
    echo -e "  ${GREEN}✔${NC}  post-checkout  ${DIM}git clone 시 자동 설치 / auto-install on git clone${NC}"
else
    echo -e "  ${YELLOW}⚠${NC}  git 레포 루트 없음 — git 훅 건너뜀 / git repo root not found — skipping git hooks"
fi

# ── 14. Mark installed version ────────────────────
echo "${DOMANGCHA_VERSION}" > "${CLAUDE_DIR}/domangcha-installed-version"
rm -f "${CLAUDE_DIR}/.domangcha-version-cache"

# ── Done — clear + full screen ───────────────────
clear
python3 - "${DOMANGCHA_VERSION}" <<'PYEOF'
import sys, unicodedata, shutil

v = sys.argv[1]
cols = shutil.get_terminal_size((80, 24)).columns

def dw(s):
    return sum(2 if unicodedata.east_asian_width(c) in ('W','F') else 1 for c in s)

CY="\033[0;36m"; CB="\033[0;36m\033[1m"; GR="\033[0;32m"
MG="\033[0;35m"; WH="\033[1;37m"; DM="\033[2m"; NC="\033[0m"; BD="\033[1m"

# ── ASCII banner (wide: full art / narrow: text) ──
wide = cols >= 86
if wide:
    print(f"\n{CB}")
    for line in [
        "  ██████╗  ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗ ██████╗  ██████╗ ██╗  ██╗ █████╗ ",
        "  ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗████╗  ██║██╔════╝ ██╔════╝ ██║  ██║██╔══██╗",
        "  ██║  ██║██║   ██║██╔████╔██║███████║██╔██╗ ██║██║  ███╗██║      ███████║███████║",
        "  ██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██║      ██╔══██║██╔══██║",
        "  ██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝╚██████╗ ██║  ██║██║  ██║",
        "  ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝",
    ]: print(line)
    print(NC)
else:
    print(f"\n{CB}  🚗💨 DOMANGCHA{NC}")

print(f"{WH}{BD}  돔황차 — 개발 지옥에서 도망쳐  🚗💨{NC}")
print(f"{DM}  Escape development hell. DOMANGCHA is your getaway car.{NC}")
print(f"  {MG}{BD}AI 개발 자동화 도구{NC}  {DM}·{NC}  {MG}AI Development Automation Tool{NC}")
print()

# ── Version block (wide: big digits / narrow: inline) ──
if wide:
    digits = {
        '0':["┌─┐","│ │","└─┘"],'1':[" ┐ "," │ "," ┴ "],'2':["┌─┐","┌─┘","└─┘"],
        '3':["┌─┐"," ─┤","└─┘"],'4':["┬ ┬","└─┤","  ┴"],'5':["┌─ ","└─┐","└─┘"],
        '6':["┌─ ","├─┐","└─┘"],'7':["┌─┐","  │","  ╵"],'8':["┌─┐","├─┤","└─┘"],
        '9':["┌─┐","└─┤","  ┘"],'.':["   ","   "," · "],'-':["   ","───","   "],
        'v':["   ","\\/ ","   "],
    }
    print(f"{GR}{BD}")
    lines = ["  ","  ","  "]
    for c in "v" + v:
        d = digits.get(c, ["   ","   ","   "])
        for i in range(3): lines[i] += d[i] + " "
    for l in lines: print(l)
    print(NC)
else:
    print(f"  {GR}{BD}v{v}{NC}\n")

# ── Info box (width-adaptive) ──
rows = [
    (CY, "18 에이전트(Agents)  ·  16 명령어(Commands)  ·  풀 파이프라인(Full Pipeline)"),
    (DM, "기획 → 빌드 → 검증 → GATE → 출시  /  Plan → Build → Eval → GATE → Ship"),
    (WH, "by docore  (Michael Dohyeon Kim · KDC CEO)"),
    (DM, "github.com/DoCoreTeam/domangcha"),
    (GR, "설치/업데이트:  npx domangcha"),
]
max_content = max(dw(t) for _, t in rows)
box_inner = min(max_content + 4, cols - 6)
bar = "─" * (box_inner)
def row(col, text):
    pad = box_inner - dw(text) - 4
    return f"  {MG}│{NC}  {col}{text}{NC}{' ' * max(pad,0)}  {MG}│{NC}"
print(f"  {MG}┌{bar}┐{NC}")
for col, text in rows:
    print(row(col, text))
print(f"  {MG}└{bar}┘{NC}")
print()

# ── Installed items ──
sep = "  " + "─" * min(cols - 6, 56)
print(f"{WH}{BD}  설치된 항목 / What's installed{NC}")
print(f"{DM}{sep}{NC}")
items = [
    ("~/.claude/agents/dc-*.md",   "18명 DC-* 에이전트 / 18 DC-* Worker Agents"),
    ("~/.claude/commands/ceo*.md", "/ceo /ceo-init /ceo-ralph /ceo-status ..."),
    ("~/.claude/skills/",          "CEO 스킬 + 183 ECC + gstack + Superpowers"),
    ("~/.claude/hooks/ + settings.json", "자동 테스트·CEO 검토·파이프라인 강제 / enforcer"),
    ("~/.claude/CLAUDE.md",        "Claude Code 자동 로드 / auto-loaded"),
]
for path, desc in items:
    print(f"  {GR}✔{NC}  \033[1;33m{path}{NC}")
    print(f"     {DM}{desc}{NC}")
print(f"{DM}{sep}{NC}")
print()

# ── Getting started ──
print(f"{WH}{BD}  🚀 시작하기 / Getting Started{NC}")
print(f"  {DM}1.{NC} Claude Code 를 아무 프로젝트에서 열기  {DM}/ Open Claude Code in any project{NC}")
print(f"  {DM}2.{NC} {CY}/ceo-init{NC}  {DM}프로젝트 초기화 / Initialize project{NC}")
print(f"  {DM}3.{NC} {CY}/ceo \"투두앱 만들어줘\"{NC}  {DM}→ 풀 파이프라인 시작 / Start full pipeline{NC}")
print()
print(f"  {WH}{BD}📦 재설치 / Update / Reinstall{NC}")
print(f"  {GR}  npx domangcha{NC}  {DM}← 권장 / recommended{NC}")
print(f"  {DM}  curl -sSL https://raw.githubusercontent.com/DoCoreTeam/domangcha/main/domangcha/install.sh | bash{NC}")
print()
print(f"  {WH}{BD}📋 주요 명령어 / Key Commands{NC}")
cmds = [
    ("/ceo \"업무\"", "Q&A → 17에이전트 → GATE → 완료"),
    ("/ceo-ralph",    "자율 반복 루프 / autonomous loop"),
    ("/ceo-init",     "프로젝트 하네스 셋업 / harness setup"),
    ("/ceo-status",   "현황 조회 / show status"),
]
for cmd, desc in cmds:
    print(f"  {CY}{cmd:<20}{NC}  {DM}{desc}{NC}")
print()
print(f"  {MG}{BD}개발 지옥에서 도망쳐. 🚗💨 돔황차가 데려다 줄게.{NC}")
print(f"  {DM}Escape development hell. DOMANGCHA is your getaway car.{NC}")
print()
PYEOF
