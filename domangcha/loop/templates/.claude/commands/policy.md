---
description: 누적 정책 조회와 자체감사 승격 (LOOP.md 6절)
---
node scripts/loop.mjs policy check 를 실행해 활성 정책을 출력하고 현재 변경분에 전 줄을 대조

$ARGUMENTS 가 비어 있으면 대조 결과만 보고
$ARGUMENTS 가 반복 실수 설명이면 LOOP.md 6절 승격 기준으로 판단해
일반 규칙일 때만 node scripts/loop.mjs policy add --title "짧은 제목" --rule "무엇을 하지 말고 무엇을 할 것" --origin 근거 를 실행하고
항목 한정 실수면 승격하지 않는 이유를 설명

규칙은 관측 가능한 행동으로 쓰고 diff 나 명령 출력으로 위반 여부를 판정할 수 있어야 함
