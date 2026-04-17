# /ceo-doc — 문서화 오케스트레이터 / Documentation Orchestrator

**EN** — Full documentation pipeline: API docs → usage guides → codemaps → release notes. Combines gstack, ECC, and DC-DOC agent.

**KO** — API 문서 → 사용 가이드 → 코드맵 → 릴리즈 노트 전체 파이프라인. gstack, ECC, DC-DOC 에이전트를 결합합니다.

## 사용법 / Usage

```
/ceo-doc              → 전체 문서화 파이프라인 / Full doc pipeline
/ceo-doc --api        → API 문서 중심 / API docs focus
/ceo-doc --release    → 릴리즈 노트 / Release notes
/ceo-doc --codemaps   → 코드맵 업데이트 / Update codemaps
/ceo-doc --seo        → SEO 최적화 포함 / Include SEO optimization
```

## 실행 파이프라인 / Execution Pipeline

### STEP 1: 코드맵 업데이트 (Codemaps)
- ECC `/update-codemaps` → 코드베이스 구조 자동 업데이트

### STEP 2: API 문서 (API Docs)
- DC-DOC 에이전트 → API 문서 + 사용 가이드 작성
- ECC `/docs` → Context7 기반 문서 조회 및 참조

### STEP 3: 프로젝트 문서 업데이트 (Project Docs)
- ECC `/update-docs` → README, CHANGELOG, 사용 가이드 업데이트
- gstack `/docs` → gstack 문서 워크플로우

### STEP 4: 릴리즈 문서 (Release Docs, 배포 후)
- gstack `/document-release` → 배포 후 문서 업데이트
- ECC `/report` → 프로젝트 상태 보고서 생성

### STEP 5: SEO 최적화 (SEO, 선택)
- DC-SEO 에이전트 → 메타 태그, Schema.org, SEO/AEO/GEO 최적화

## 결과 보고 / Output

```
[CEO-DOC REPORT]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 코드맵 (Codemaps):   ✅ 업데이트 완료
📖 API 문서 (API Docs): ✅ 생성/업데이트 완료
📝 프로젝트 문서 (Docs): ✅ README + CHANGELOG
🚀 릴리즈 노트 (Release): ✅ 작성 완료
🔍 SEO 최적화 (SEO):    ✅ 메타태그 + Schema.org
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[생성/업데이트된 파일 목록]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 연동 도구 / Tools Used

| 도구 | 출처 | 역할 |
|------|------|------|
| `/docs` | gstack | 문서 워크플로우 |
| `/document-release` | gstack | 릴리즈 후 문서 |
| `/update-codemaps` | ECC | 코드맵 업데이트 |
| `/update-docs` | ECC | 프로젝트 문서 |
| `/docs` | ECC | Context7 문서 조회 |
| `/report` | ECC | 상태 보고서 |
| DC-DOC | MACC | 문서 작성 에이전트 |
| DC-SEO | MACC | SEO 최적화 에이전트 |
