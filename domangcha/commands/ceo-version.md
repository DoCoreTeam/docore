# /ceo-version — Version Status

`manifests/versions.json` 기반 deterministic release-surface workflow다. `domangcha/VERSION`이 authoritative하다.

1. source checkout이면 `domangcha/VERSION`, installed runtime이면 `~/.domangcha/domangcha/VERSION`을 읽는다.
2. source checkout은 `python3 domangcha/engine.py validate`로 package, CLI, CLAUDE headers, README badge를 검증한다.
3. 최신 버전 조회가 요청되면 npm registry/GitHub VERSION을 read-only로 확인한다.
4. 업데이트는 사용자 승인 후 `/ceo-update`로 위임한다.

Unknown/network failure는 설치를 손상시키지 않으며 현재 버전과 오류만 보고한다.
