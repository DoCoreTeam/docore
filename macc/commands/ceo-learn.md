# /ceo-learn — 학습 오케스트레이터 / Learning Orchestrator

**EN** — Full learning pipeline: extract patterns → evaluate → save instincts → promote to global. Combines ECC's learning system with gstack's retro and MACC's session tools.

**KO** — 패턴 추출 → 평가 → 인스팅트 저장 → 글로벌 승격 전체 학습 파이프라인. ECC 학습 시스템 + gstack 회고 + MACC 세션 도구를 결합합니다.

## 사용법 / Usage

```
/ceo-learn              → 전체 학습 파이프라인 / Full learning pipeline
/ceo-learn --retro      → 주간 회고 포함 / Include weekly retro
/ceo-learn --promote    → 글로벌 승격 포함 / Include global promotion
/ceo-learn --session    → 세션 저장 중심 / Session save focus
```

## 실행 파이프라인 / Execution Pipeline

### STEP 1: 세션 저장 (Session Save)
- ECC `/save-session` → 현재 세션 상태 저장

### STEP 2: 패턴 추출 (Pattern Extraction)
- ECC `/learn` → 현재 세션에서 재사용 가능한 패턴 추출
- ECC `/learn-eval` → 패턴 품질 자체 평가 후 저장 위치 결정

### STEP 3: 인스팅트 관리 (Instinct Management)
- ECC `/instinct-status` → 현재 인스팅트 목록 + 신뢰도 확인
- ECC `/evolve` → 기존 인스팅트 개선안 제안
- ECC `/prune` → 30일 이상 된 미사용 인스팅트 정리

### STEP 4: 회고 (Retro, 선택)
- gstack `/retro` → 주간 회고 — 잘된 것, 개선할 것, 다음 목표
- gstack `/learn` → gstack 세션 학습 저장

### STEP 5: 글로벌 승격 (Global Promote, 선택)
- ECC `/promote` → 프로젝트 인스팅트를 글로벌로 승격
- ECC `/rules-distill` → 코드베이스 패턴 → 규칙 정제

## 결과 보고 / Output

```
[CEO-LEARN REPORT]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💾 세션 저장 (Session):   ~/.claude/session-data/<날짜>.md
🧠 추출된 패턴 (Patterns): <N>개
📈 인스팅트 (Instincts):  <N>개 (신뢰도 <X>%)
🗑️  정리된 항목 (Pruned):  <N>개
🌐 글로벌 승격 (Promoted): <N>개
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[저장된 패턴 목록]
[회고 요약]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 연동 도구 / Tools Used

| 도구 | 출처 | 역할 |
|------|------|------|
| `/retro` | gstack | 주간 회고 |
| `/learn` | gstack | gstack 학습 저장 |
| `/learn` | ECC | 패턴 추출 |
| `/learn-eval` | ECC | 패턴 품질 평가 |
| `/save-session` | ECC | 세션 저장 |
| `/instinct-status` | ECC | 인스팅트 현황 |
| `/evolve` | ECC | 인스팅트 개선 |
| `/prune` | ECC | 오래된 항목 정리 |
| `/promote` | ECC | 글로벌 승격 |
| `/rules-distill` | ECC | 규칙 정제 |
