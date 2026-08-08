# /ceo-init — Adaptive Runtime Setup

Canonical engine과 runtime adapter를 초기화하는 guarded workflow다. 기존 사용자 설정, registry, checkpoint를 보존한다.

## Setup

1. `~/.domangcha/domangcha/` shared engine과 policies/manifests/graphs를 확인한다.
2. Claude Code가 있으면 managed agents, commands, hooks, CLAUDE adapter를 확인한다.
3. Codex가 있으면 `CODEX_HOME` 또는 `~/.codex`의 managed AGENTS block을 확인한다.
4. 현재 runtime을 `RuntimeDetector`로 탐지하고 capability snapshot을 출력한다.
5. 프로젝트에 `.domangcha/checkpoints/`와 structured event 저장 경로를 준비한다. 이 runtime artifact는 기본적으로 Git에 커밋하지 않는다.
6. `python3 domangcha/engine.py validate` 또는 설치본의 동일 명령을 실행한다.

## Safety

- 기존 AGENTS.md/CLAUDE.md 전체를 덮어쓰지 않는다.
- user registry, decisions, checkpoint, unrelated hooks를 삭제하지 않는다.
- pre-commit, CI, CODEOWNERS는 프로젝트 정책을 검사한 뒤 필요한 경우에만 제안/설치한다.
- project initialization 자체가 commit, push, publish, deploy 권한을 의미하지 않는다.

## Result

```text
[DOMANGCHA INITIALIZED]
version: <VERSION>
runtime: <CLAUDE_CODE|CODEX_LOCAL|CODEX_IDE|CODEX_CLOUD|UNKNOWN>
route engine: ready
checkpointing: ready
manifest validation: pass|fail
```
