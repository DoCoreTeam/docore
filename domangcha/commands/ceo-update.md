# /ceo-update — CEO 업데이트 / Update CEO

Canonical installer의 guarded update workflow다. Managed adapter만 교체하고 사용자 registry/checkpoint를 보존한다.

**EN** — Update the shared engine and Claude/Codex adapters. Registries and checkpoints are preserved.

**KO** — shared engine과 Claude/Codex adapter를 업데이트합니다. 레지스트리와 체크포인트는 보존됩니다.

> 💡 업데이트 전에 현재 버전을 확인하려면 `/ceo-version` 을 먼저 실행하세요.

## 실행 / Execution

```bash
# 1순위: npm 레지스트리 경유 (권장)
npx domangcha --full

# 위 실패 시 fallback: GitHub raw 직접
# curl -fsSL https://raw.githubusercontent.com/DoCoreTeam/domangcha/main/domangcha/install.sh | bash
```

> ⚠️ v3.0.0부터 `--full` 이 전체 하네스 설치·업데이트 플래그다. 인자 없는 `npx domangcha` 는
> 현재 프로젝트에 경량 루프를 설치하며 `~/.claude` 를 갱신하지 않는다.
> `npx domangcha --full` 실패 시 fallback 명령어의 `#`을 제거하여 수동 실행하세요.

## 업데이트 항목 / What Gets Updated

| 항목 | 동작 |
|------|------|
| CEO agents (dc-*.md) | ✅ 항상 최신으로 덮어씀 |
| CEO commands (/ceo-*.md) | ✅ 항상 최신으로 덮어씀 |
| CEO SKILL.md | ✅ 항상 최신으로 덮어씀 |
| CLAUDE.md | ✅ CEO 섹션만 교체 |
| Codex AGENTS managed block | ✅ DOMANGCHA block만 교체 |
| Shared engine (`~/.domangcha`) | ✅ 항상 최신으로 교체 |
| ECC (183 skills + 79 commands) | ✅ 전체 교체 |
| gstack | ✅ git pull (또는 재클론) |
| Superpowers | ✅ plugin update (또는 재클론) |
| Memory templates (rule_*.md) | ✅ 규칙 메모리 최신화 |
| Registries (error-registry 등) | ⏭️ 보존 (사용자 데이터) |
