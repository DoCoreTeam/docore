# /ceo-update — CEO 업데이트 / Update CEO

Canonical installer의 guarded update workflow다. Managed adapter만 교체하고 사용자 registry/checkpoint를 보존한다.

**EN** — Update the shared engine and Claude/Codex adapters. Registries and checkpoints are preserved.

**KO** — shared engine과 Claude/Codex adapter를 업데이트합니다. 레지스트리와 체크포인트는 보존됩니다.

> 💡 업데이트 전에 현재 버전을 확인하려면 `/ceo-version` 을 먼저 실행하세요.

## 실행 / Execution

```bash
curl -fsSL https://raw.githubusercontent.com/DoCoreTeam/domangcha/main/domangcha/install.sh | bash
```

> ⚠️ v3.0.0부터 `npx domangcha` 는 실행한 자리를 보고 판단한다. 프로젝트 안에서 실행하면
> 그 프로젝트에 루프를 설치하고 `~/.claude` 는 건드리지 않는다. 하네스를 갱신하려면 위 명령을
> 쓰거나 프로젝트 밖(예: `cd ~`)에서 `npx domangcha` 를 실행한다.

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
