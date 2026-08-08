# /ceo-knowledge — Knowledge Registry Commands

Canonical TaskRouter의 read-only/curation intent adapter다. Knowledge Registry는 advisory input이며 control edge 권한이 없다.

DC-KNW (18번째 DOMANGCHA 직원) 관리 2-layer 지식 레지스트리 명령어 모음.

## 명령어 목록

### /ceo-knowledge [query]
- 별칭: `/ceo-k`
- 동작: DC-KNW QUERY 모드 실행
- 인자:
  - ID `KNW-YYYY-MM-DD-NNN` — 특정 엔트리 조회
  - 키워드 — semantic 검색
  - 생략 — 전체 INDEX 출력
- 예시:
  ```
  /ceo-knowledge KNW-2026-05-01-001
  /ceo-knowledge 파일 크기
  /ceo-knowledge
  ```
- 출력 포맷: `[DC-KNW QUERY]` 블록

### /ceo-learn "내용"
- 동작: DC-KNW RECORD 모드 실행
- 인자: 기록할 패턴/지식 설명 (자유 형식)
- 예시:
  ```
  /ceo-learn "DC-DEV-BE가 async 없이 await 사용 시 빌드 실패"
  /ceo-learn "GATE 5 파괴적 변경 시 사용자 승인 필수"
  ```
- CEO가 자동으로 `type/severity/domain` 분류
- 직접 registry 쓰지 않음 — `/ceo-promote`로 승인 필요
- `.knw-queue/KNW-PENDING-NNN.md` 생성
- 출력 포맷: `[DC-KNW RECORD]` 블록 + 큐 파일 경로

### /ceo-promote [ID]
- 동작: DC-KNW CURATE 모드 실행
- 인자:
  - 생략 — 큐 전체 처리
  - `KNW-PENDING-NNN` — 특정 엔트리만 처리
- GATE 완료 후 CEO가 자동 호출
- 중복 체크 → registry 이동 또는 삭제
- INDEX.md 카운트 자동 업데이트
- 출력 포맷: `[DC-KNW CURATE]` 블록

### /ceo-forget KNW-ID
- 동작: registry 엔트리 삭제 (CEO 확인 후)
- 인자: `KNW-YYYY-MM-DD-NNN` (필수)
- 파일 삭제 전 확인 절차 실행
- INDEX.md 카운트 자동 업데이트
- 출력 포맷: `[DC-KNW FORGET]` 블록

## 레지스트리 구조

```
domangcha/knowledge-registry/
├── INDEX.md                  ← 전체 목록 + 통계
├── .knw-queue/               ← 승인 대기 (임시)
│   └── KNW-PENDING-NNN.md
├── error/                    ← 반복 에러 패턴
├── pattern/                  ← 베스트 프랙티스
├── decision/                 ← 아키텍처 결정 (ADR)
├── workflow/                 ← 프로세스 절차
└── skill/                    ← 기술 지식
```

## KNW 엔트리 ID 체계

- 형식: `KNW-YYYY-MM-DD-NNN`
- NNN: 당일 순번 (001부터)
- 타입별 폴더에 저장
- 예: `KNW-2026-05-01-001` → `error/KNW-2026-05-01-001.md`

## 자동 통합 (CEO 파이프라인)

| 단계 | 모드 | 동작 |
|------|------|------|
| PHASE 1 시작 | GUARD | 관련 엔트리 advisory 출력 (non-blocking) |
| GATE 완료 후 | CURATE | `.knw-queue/` 자동 처리 |

- GUARD 결과는 CEO 파이프라인 중단 없음
- 사용자는 `/ceo-learn` + `/ceo-promote`로 수동 관리도 가능
