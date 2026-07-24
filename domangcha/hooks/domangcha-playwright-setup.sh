#!/usr/bin/env bash
# DOMANGCHA — Playwright MCP setup (called from install.sh)
# NOTE: 브라우저 검증 기본은 Claude-in-Chrome 확장(mcp__claude-in-chrome__*).
#       Playwright는 폴백(헤드리스 CI / 회귀 스위트 / Chrome 확장 미가용)용으로만 설치.
#       정책: skills/ceo-standards/SKILL.md "브라우저 검증 정책"
GREEN='\033[0;32m'; YELLOW='\033[1;33m'; BLUE='\033[0;34m'; NC='\033[0m'

echo -e "${BLUE}  브라우저 검증 기본 = Claude-in-Chrome 확장. Playwright는 폴백(CI/헤드리스)으로 설치합니다.${NC}"

if ! command -v node &>/dev/null; then
    echo -e "${YELLOW}  ⚠️  Node.js not found — Playwright(폴백) skipped (install: https://nodejs.org)${NC}"
    exit 0
fi
if ! command -v claude &>/dev/null; then
    echo -e "${YELLOW}  ⚠️  claude CLI not found — Playwright MCP skipped${NC}"
    exit 0
fi

LATEST_VER=$(npm show @playwright/mcp version 2>/dev/null | tr -d '[:space:]' || echo "")
CURRENT_ENTRY=$(claude mcp list 2>/dev/null | grep -i "playwright" | head -1 || echo "")

if [ -n "$CURRENT_ENTRY" ]; then
    CURRENT_VER=$(echo "$CURRENT_ENTRY" | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' | head -1 || echo "")
    if [ -n "$LATEST_VER" ] && [ -n "$CURRENT_VER" ] && [ "$LATEST_VER" != "$CURRENT_VER" ]; then
        echo -e "${YELLOW}  ⟳ playwright MCP — updating ${CURRENT_VER} → ${LATEST_VER}${NC}"
        claude mcp remove playwright 2>/dev/null || true
        claude mcp add playwright -s user npx "@playwright/mcp@${LATEST_VER}" 2>/dev/null \
            && echo -e "${GREEN}  ✅ playwright MCP updated to v${LATEST_VER}${NC}" \
            || echo -e "${YELLOW}  ⚠️  Update failed — keeping existing${NC}"
    else
        echo -e "${YELLOW}  ⟳ playwright MCP already up to date (v${CURRENT_VER:-latest})${NC}"
    fi
else
    VER_TAG="${LATEST_VER:-latest}"
    claude mcp add playwright -s user npx "@playwright/mcp@${VER_TAG}" 2>/dev/null \
        && echo -e "${GREEN}  ✅ playwright MCP registered (v${VER_TAG})${NC}" \
        || echo -e "${YELLOW}  ⚠️  Registration failed — run: claude mcp add playwright -s user npx @playwright/mcp@latest${NC}"
fi

echo -e "${BLUE}  Installing Playwright Chromium browser...${NC}"
npx playwright install --with-deps chromium 2>/dev/null \
    && echo -e "${GREEN}  ✅ Chromium installed${NC}" \
    || echo -e "${YELLOW}  ⚠️  Chromium install failed — run: npx playwright install --with-deps chromium${NC}"

echo -e "${GREEN}  ✅ Playwright MCP ready — 폴백(headless CI/회귀)용. 실화면 검증은 Claude-in-Chrome 확장 우선.${NC}"
echo -e "     Headed: claude mcp add playwright -s user npx @playwright/mcp --headed"
