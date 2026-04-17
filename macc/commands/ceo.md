# /ceo — 전체 파이프라인 자동 실행

사용자가 입력한 업무를 받아 **모든 에이전트가 개발 순서대로 자동 실행**함
중간 생략 없음 — 항상 전체 파이프라인이 돌아감

## 사용법

```
/ceo "원하는 업무 설명"
```

## 에이전트 Tier

**CORE (항상 실행 — 생략 불가):**
DC-BIZ, DC-RES, DC-OSS, DC-DEV-DB, DC-DEV-BE, DC-DEV-FE, DC-DEV-OPS, DC-QA, DC-SEC, DC-REV, DC-DOC, DC-TOK

**EXTENDED (업무 분석 후 CEO가 판단하여 추가):**
DC-DEV-MOB (모바일 포함 시), DC-DEV-INT (외부 API 연동 시), DC-WRT (마케팅/카피 필요 시), DC-SEO (웹 공개 서비스 시)

---

## 실행 순서 (이 순서 반드시 전부 실행)

### PHASE 0.5: CLARIFICATION Q&A (필수 — 생략 불가)

CEO는 PHASE 1 진입 전에 반드시 사용자에게 핵심 질문을 한다.
질문 없이 바로 실행하는 것은 **절대 금지**됨.

**Q&A 실행 규칙:**
- 질문을 **한 번에 하나씩** 묻는다 — 답변을 받으면 다음 질문으로 넘어간다
- 앞 답변을 반영해 다음 질문을 조정한다 (예: "웹"이라고 하면 모바일 질문 생략)
- 최소 7개, 최대 12개 질문 후 충분히 파악되면 Q&A 종료
- 모든 질문이 끝나면 `[Q&A COMPLETE]`를 출력하고 PHASE 1으로 진행

**Q&A 진행 방식 (스텝바이스텝):**

```
[CEO Q&A — PHASE 0.5]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
업무: $ARGUMENTS

Q1. [기술스택] 사용할 언어/프레임워크/DB가 정해져 있나요?
    (예: Next.js + Supabase, FastAPI + PostgreSQL, 아직 미정)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

→ 사용자 답변 대기
→ 답변 받으면 다음 질문:

```
Q2. [타겟 플랫폼] 어느 플랫폼이 대상인가요?
    (예: 웹, iOS/Android, API only, 데스크톱, 복합)
```

→ 이런 식으로 한 번에 하나씩 계속 진행

**질문 풀 (앞 답변에 따라 불필요한 항목은 건너뜀):**

1. [기술스택] 언어/프레임워크/DB
2. [타겟 플랫폼] 웹/모바일/API/데스크톱
3. [기존 코드베이스] 있음(경로) / 없음(새로 시작)
4. [완료 기준] 이 업무가 "완료"라고 판단하는 기준
5. [사용자/규모] 예상 사용자 규모와 트래픽
6. [인증/보안] 로그인, 소셜, 역할별 권한 필요 여부
7. [데이터] 주요 데이터 모델
8. [외부 연동] Stripe, OpenAI, Slack 등 외부 API
9. [우선순위/제약] 하면 안 되는 것 또는 반드시 해야 할 것
10. [디자인] UI 방향, Figma 링크, 참고 서비스
11. [배포/인프라] Vercel, AWS, Railway, 로컬
12. [추가 맥락] 위에 없지만 알아야 할 중요한 정보

**모든 질문이 끝나면:**
- CEO가 답변을 요약하여 `[Q&A COMPLETE]` 블록 출력
- EXTENDED 에이전트 필요 여부 결정 (MOB/INT/WRT/SEO)
- 답변을 INTAKE REPORT에 반영
- PHASE 1 진입

```
[Q&A COMPLETE]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ 확인된 사항:
• 기술스택: <답변>
• 플랫폼: <답변>
• 완료 기준: <답변>
• 주요 제약: <답변>
• EXTENDED 에이전트: <추가 여부 + 이유>
→ PHASE 1 진입합니다
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

---

## DC Agent 실행 규칙 (CRITICAL)

DC-* 에이전트를 실행할 때는 반드시 **`Agent` 도구**를 사용하여 서브에이전트로 스폰합니다.
에이전트 파일을 읽고 인라인으로 시뮬레이션하는 것은 **절대 금지**입니다.
이렇게 해야만 Claude Code UI에서 서브에이전트가 실행 중으로 표시됩니다.

```
Agent(subagent_type="dc-biz", description="DC-BIZ: Business Judge", prompt="...")
Agent(subagent_type="dc-res", description="DC-RES: Researcher", prompt="...")
# 병렬 실행: 한 메시지에서 여러 Agent 호출을 동시에 선언
```

---

### PHASE 0.7: RIPPLE ANALYSIS (확장적 영향도 분석 — 필수)

Q&A 완료 후, 구현 시작 전에 CEO는 반드시 아래를 수행합니다:

```
[RIPPLE ANALYSIS]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 직접 변경 대상: <수정할 파일/컴포넌트>
🌊 파급 영향: <이 변경이 영향주는 연관 파일>
🔧 함께 개선할 항목: <사용자 미언급 but 필요한 것>
⚠️ 사이드이펙트 위험: <깨질 수 있는 기존 동작>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

- 수정 1개 → 연관 파일 2-3개 추가 점검 필수
- "이것만 해줘" = "이것 + 연관된 모든 것을 일관되게"
- 개선 기회 발견 시 → 즉시 처리 (보고는 [CEO 자체 추가]로)

---

### PHASE 1: PLANNER (기획)

CEO가 아래를 순서대로 수행:

1. **CEO 자가점검** 실행
   - 사용자가 명시하지 않았지만 포함해야 할 항목 확인
   - error-registry 관련 패턴 확인
   - skill-registry 사용 가능 패턴 확인
   - project-registry 제약 충돌 확인

2. **Intake Report** 생성
   ```
   [CEO INTAKE REPORT]
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   📋 업무명: $ARGUMENTS
   🎯 목표: <달성해야 할 결과>
   ⚠️ 위험도: LOW / MEDIUM / HIGH / CRITICAL
   🔀 병렬 가능: YES / NO
   🚦 우선순위: P0 / P1 / P2 / P3
   💰 규모 판정: SMALL / MEDIUM / LARGE / HEAVY
   🤖 모델 배정: <Opus/Sonnet/Haiku 조합>
   🧩 EXTENDED 에이전트: <MOB/INT/WRT/SEO 중 필요한 것>
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ```

3. **DC-BIZ** 호출 → 사업 타당성 판단 (agents/dc-biz.md 참조)
4. **DC-RES** 호출 → 기술 리서치 (agents/dc-res.md 참조)
5. **DC-OSS** 호출 → 외부 라이브러리/도구 Top 3 탐색 (agents/dc-oss.md 참조)
6. CEO가 **docs/PLAN.md** 작성

### PHASE 2: CONTRACT (계약)

7. CEO + **DC-QA** 스프린트 계약 협상
8. **docs/CONTRACT-SPRINT-1.md** 작성 (구현 범위 + 검증 기준 합의)

### PHASE 3: GENERATOR (개발 — 병렬 실행)

**CORE 에이전트 (항상 실행 — 동시):**

9.  **DC-DEV-DB** → 스키마 설계 + 마이그레이션 (agents/dc-dev-db.md 참조)
10. **DC-DEV-BE** → API 엔드포인트 + 비즈니스 로직 (agents/dc-dev-be.md 참조)
11. **DC-DEV-FE** → UI 컴포넌트 + 페이지 (agents/dc-dev-fe.md 참조)
12. **DC-DEV-OPS** → CI/CD + 하네스 장치 구축 (agents/dc-dev-ops.md 참조)
13. **DC-DOC** → API 문서 + 사용 가이드 (agents/dc-doc.md 참조)

**EXTENDED 에이전트 (Q&A 분석 결과에 따라 추가 실행):**

14. **DC-DEV-MOB** → 모바일 대응 — 모바일 플랫폼 포함 시 (agents/dc-dev-mob.md 참조)
15. **DC-DEV-INT** → 외부 API 연동 — 외부 서비스 연동 시 (agents/dc-dev-int.md 참조)
16. **DC-WRT** → 마케팅 카피/콘텐츠 — 마케팅 페이지/카피 필요 시 (agents/dc-wrt.md 참조)
17. **DC-SEO** → SEO/AEO/GEO 최적화 — 웹 공개 서비스 시 (agents/dc-seo.md 참조)

18. 완료 후 **docs/SPRINT-1-HANDOFF.md** 작성 (사실만 기록 — 평가 없이)

### PHASE 4: EVALUATOR (검증 — 3-way 동시)

19. **DC-QA** → 기능/품질 테스트 → docs/QA-SPRINT-1.md (agents/dc-qa.md 참조)
20. **DC-SEC** → OWASP 기반 보안 검토 → docs/SEC-SPRINT-1.md (agents/dc-sec.md 참조)
21. **DC-REV** → 코드 리뷰 + 품질 채점 → docs/REV-SPRINT-1.md (agents/dc-rev.md 참조)

### PHASE 5: 판정

22. **전체 PASS** → PHASE 6으로 진행
23. **ANY FAIL** → GENERATOR로 돌아가서 재작업 (최대 3회)
24. **3회 초과** → 에스컬레이션:
    ```
    [ESCALATION]
    🔴 실패 업무: <업무명>
    📊 시도 횟수: 3/3
    🔍 근본 원인: <CEO 분석>
    💡 대안:
      1. 접근 방식 변경
      2. 범위 축소
      3. 수동 처리 권고
    ```

### PHASE 6: GATE + 최종 보고

25. **GATE 1**: error-registry 금지 패턴 스캔 + **파일 300줄 초과 감지 → 즉시 차단** (모듈 분리 지시)
26. **GATE 2**: 완료 조건 충족 검증
27. **GATE 3**: 버전 태그 포함 확인 — `macc/VERSION` 파일의 현재 버전과 일치 여부
28. **GATE 4**: Builder ≠ Reviewer 역할 분리 확인
29. **GATE 5**: 파괴적 변경 감지 → 있으면 사용자 승인 필요
30. **DC-TOK** → 컨텍스트 사용량 보고 (agents/dc-tok.md 참조)
31. **CEO 자가점검** 최종 실행
32. **git commit** -m "v$(cat macc/VERSION 2>/dev/null || cat VERSION 2>/dev/null || echo "??"): $ARGUMENTS"
33. **CEO REPORT** 출력:

```
[CEO REPORT]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ 업무 완료: $ARGUMENTS
🏷️ 버전: v{VERSION} (macc/VERSION 파일 기준)
👥 투입: CORE 12명 + EXTENDED <n>명
⏱️ 실행: PLANNER→GENERATOR(병렬)→EVALUATOR(3-way)→GATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[산출물]
(실제 결과물 — 코드, 파일, 문서 등)

[품질 보증]
□ GATE 1-5 모두 통과
□ DC-QA 검증 완료
□ DC-SEC 보안 검토 완료
□ DC-REV 코드 리뷰 완료
□ 버전 태그 적용
□ 하네스 장치 구현 완료
□ CEO 자가점검 완료

[CEO 자체 추가 항목]
• (사용자가 명시하지 않았지만 CEO가 추가한 것)

[다음 권장 액션]
• (CEO가 권장하는 다음 단계)

[Rollback 가이드]
• (문제 발견 시 되돌리는 방법)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
