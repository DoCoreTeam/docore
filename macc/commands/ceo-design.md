# /ceo-design — 디자인 오케스트레이터 / Design Orchestrator

**EN** — Full design pipeline: direction → system → components → review. Combines gstack's design tools with ECC's UI generation and DC-DEV-FE agent.

**KO** — 디자인 방향 → 디자인 시스템 → 컴포넌트 → 리뷰 전체 파이프라인. gstack 디자인 도구 + ECC UI 생성 + DC-DEV-FE 에이전트를 결합합니다.

## 사용법 / Usage

```
/ceo-design "원하는 디자인"   → 전체 디자인 파이프라인 / Full design pipeline
/ceo-design --system          → 디자인 시스템 중심 / Design system focus
/ceo-design --component "버튼" → 특정 컴포넌트 / Specific component
/ceo-design --review          → 기존 UI 리뷰만 / Review existing UI only
/ceo-design --liquid-glass    → Liquid Glass 스타일 / Apple-style Liquid Glass
```

## 실행 파이프라인 / Execution Pipeline

### STEP 1: 디자인 방향 설정 (Design Direction)
- gstack `/design-consultation` → 디자인 방향, 레퍼런스, 스타일 가이드 확정
- gstack `/design-shotgun` → 여러 방향 동시 탐색 (빠른 아이데이션)
- gstack `/office-hours` → 디자인 의사결정 조언 (선택)

### STEP 2: 디자인 시스템 (Design System)
- ECC `design-system` 스킬 → 토큰, 컬러, 타이포그래피, 스페이싱 정의
- ECC `liquid-glass-design` 스킬 → Liquid Glass 효과 (선택)
- gstack `/design` → 브랜드 + 컴포넌트 가이드라인

### STEP 3: 구현 (Implementation)
- gstack `/design-html` → HTML/CSS 구현
- ECC `/ui-design` → UI 컴포넌트 생성
- ECC `/design` → 디자인 코드 생성
- DC-DEV-FE 에이전트 → 프론트엔드 컴포넌트 구현

### STEP 4: 리뷰 (Review)
- gstack `/design-review` → 시각적 디자인 리뷰 및 폴리싱
- gstack `/plan-design-review` → 기획 단계 디자인 검토

## 결과 보고 / Output

```
[CEO-DESIGN REPORT]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎨 디자인 방향 (Direction): <스타일>
🎭 디자인 시스템 (System): <컬러/타이포/스페이싱>
🧩 생성 컴포넌트 (Components): <목록>
✅ 디자인 리뷰 (Review): PASS / NEEDS_REVISION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[산출물 파일 목록]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 연동 도구 / Tools Used

| 도구 | 출처 | 역할 |
|------|------|------|
| `/design-consultation` | gstack | 디자인 방향 컨설팅 |
| `/design-shotgun` | gstack | 다방향 디자인 탐색 |
| `/design` | gstack | 브랜드 + 컴포넌트 |
| `/design-html` | gstack | HTML/CSS 구현 |
| `/design-review` | gstack | 비주얼 리뷰 |
| `/plan-design-review` | gstack | 기획 단계 디자인 검토 |
| `/ui-design` | ECC | UI 컴포넌트 생성 |
| `/design` | ECC | 디자인 코드 생성 |
| `design-system` | ECC skill | 디자인 시스템 |
| `liquid-glass-design` | ECC skill | Liquid Glass 효과 |
| DC-DEV-FE | MACC | 프론트엔드 에이전트 |
