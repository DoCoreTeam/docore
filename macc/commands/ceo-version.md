# /ceo-version — 버전 확인 및 업데이트 안내

현재 설치된 MACC 버전을 확인하고, GitHub 최신 버전과 비교하여 업데이트 여부를 물어봄

## 실행 순서

### STEP 1: 현재 설치 버전 읽기

```bash
# 1순위: CLAUDE.md (가장 신뢰할 수 있는 소스)
INSTALLED=$(grep "^# MACC v" ~/.claude/CLAUDE.md 2>/dev/null | head -1 | sed 's/# MACC v//' | cut -d' ' -f1)
# 2순위: SKILL.md (헤더 패턴이 다를 수 있음)
if [ -z "$INSTALLED" ]; then
  INSTALLED=$(grep "^# CEO AGENT SYSTEM v\|^# MACC v" ~/.claude/skills/ceo-system/SKILL.md 2>/dev/null | head -1 | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' | head -1)
fi
echo "설치된 버전: ${INSTALLED:-알 수 없음}"
```

### STEP 2: GitHub 최신 버전 가져오기

```bash
LATEST=$(curl -fsSL https://raw.githubusercontent.com/DoCoreTeam/macc/main/macc/VERSION 2>/dev/null | tr -d '[:space:]')
echo "최신 버전: ${LATEST:-가져오기 실패}"
```

### STEP 3: 버전 비교 후 출력

아래 형식으로 출력:

```
[CEO VERSION]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏷️  설치 버전: v{INSTALLED}
🌐  최신 버전: v{LATEST}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### STEP 4: 업데이트 필요 여부 판단

**최신 버전 = 설치 버전인 경우:**
```
✅ 최신 버전입니다. 업데이트가 필요하지 않습니다.
```

**최신 버전 > 설치 버전인 경우:**
```
🆙 업데이트가 있습니다!
   설치: v{INSTALLED} → 최신: v{LATEST}

업데이트 하시겠습니까? (y/n)
```

→ 사용자 답변 대기

- **y / yes / 예 / ㅇ** → 즉시 실행:
  ```bash
  curl -sSL https://raw.githubusercontent.com/DoCoreTeam/macc/main/macc/install.sh | bash
  ```

- **n / no / 아니 / ㄴ** → 종료:
  ```
  ⏭️  업데이트를 건너뜁니다. 나중에 /ceo-update 로 업데이트할 수 있습니다.
  ```

**버전 가져오기 실패인 경우:**
```
⚠️  GitHub에 연결할 수 없습니다. 네트워크를 확인해주세요.
   수동 업데이트: /ceo-update
```
