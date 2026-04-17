# /ceo-update — CEO 업데이트 / Update CEO

**EN** — Update CEO and all dependencies (ECC, gstack, Superpowers) to the latest version. Registries are preserved.

**KO** — CEO와 모든 의존성 (ECC, gstack, Superpowers)을 최신 버전으로 업데이트합니다. 레지스트리는 보존됩니다.

> 💡 업데이트 전에 현재 버전을 확인하려면 `/ceo-version` 을 먼저 실행하세요.

## 실행 / Execution

```bash
curl -sSL https://raw.githubusercontent.com/DoCoreTeam/macc/main/macc/install.sh | bash
```

## 업데이트 항목 / What Gets Updated

| 항목 | 동작 |
|------|------|
| CEO agents (dc-*.md) | ✅ 항상 최신으로 덮어씀 |
| CEO commands (/ceo-*.md) | ✅ 항상 최신으로 덮어씀 |
| CEO SKILL.md | ✅ 항상 최신으로 덮어씀 |
| CLAUDE.md | ✅ CEO 섹션만 교체 |
| ECC (183 skills + 79 commands) | ✅ 전체 교체 |
| gstack | ✅ git pull (또는 재클론) |
| Superpowers | ✅ plugin update (또는 재클론) |
| Registries (error-registry 등) | ⏭️ 보존 (사용자 데이터) |
