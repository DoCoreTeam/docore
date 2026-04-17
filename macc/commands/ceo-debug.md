# /ceo-debug — 디버그 오케스트레이터 / Debug Orchestrator

**EN** — Full debug pipeline: reproduce → investigate → fix → verify. Combines gstack's investigate with ECC's debug tools and build fixers.

**KO** — 재현 → 조사 → 수정 → 검증 전체 파이프라인. gstack 조사 도구 + ECC 디버그 + 빌드 수정 도구를 결합합니다.

## 사용법 / Usage

```
/ceo-debug "버그 설명"      → 전체 디버그 파이프라인 / Full debug pipeline
/ceo-debug --build          → 빌드 오류 집중 / Build error focus
/ceo-debug --runtime        → 런타임 오류 집중 / Runtime error focus
/ceo-debug --perf           → 성능 문제 집중 / Performance issue focus
/ceo-debug --lang go        → 언어별 빌드 픽스 / Language-specific fix
```

## 실행 파이프라인 / Execution Pipeline

### STEP 1: 조사 (Investigation)
- gstack `/investigate` → 근본 원인 분석, 에러 추적, 증거 수집
- ECC `/debug` → 체계적 버그 진단

### STEP 2: 빌드 오류 수정 (Build Fix, 해당 시)
- ECC `/build-fix` → 빌드 오류 자동 수정
- 언어별 라우팅:
  - `/go-build` → Go 빌드 오류
  - `/rust-build` → Rust 컴파일러 오류
  - `/cpp-build` → C++ / CMake 오류
  - `/flutter-build` → Dart 분석 오류
  - `/kotlin-build` → Kotlin/Gradle 오류
  - `/gradle-build` → Android/KMP Gradle 오류

### STEP 3: 성능 문제 (Performance, 해당 시)
- ECC `/perf-check` → 병목, 번들 크기, 런타임 속도 분석

### STEP 4: 수정 및 검증 (Fix & Verify)
- ECC `/test` → 수정 후 테스트 재실행
- gstack `/qa` → 수정된 기능 브라우저 검증
- ECC `/quality-gate` → 게이트 통과 확인

## 결과 보고 / Output

```
[CEO-DEBUG REPORT]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🐛 버그 (Bug): <설명>
🔍 근본 원인 (Root Cause): <분석>
🔧 수정 방법 (Fix): <적용된 수정>
✅ 검증 결과 (Verification): PASS / FAIL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[수정된 파일 목록]
[남은 이슈]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 연동 도구 / Tools Used

| 도구 | 출처 | 역할 |
|------|------|------|
| `/investigate` | gstack | 근본 원인 조사 |
| `/qa` | gstack | 브라우저 검증 |
| `/debug` | ECC | 버그 진단 |
| `/build-fix` | ECC | 빌드 오류 수정 |
| `/go-build` `/rust-build` etc. | ECC | 언어별 빌드 픽스 |
| `/perf-check` | ECC | 성능 분석 |
| `/test` | ECC | 테스트 재실행 |
| `/quality-gate` | ECC | 게이트 확인 |
