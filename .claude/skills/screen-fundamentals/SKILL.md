---
name: screen-fundamentals
description: 시장성·경쟁력·수익성·재무 효율성·ESG 부합 여부 5개 항목을 평가해 Pass/Caution/Fail로 flag한다. judgment-rules.md 2단계(스크리닝 체크리스트)를 실행하는 스킬. 1단계 핵심 판단 기준(judge-*)과 무관하게, 1단계에서 하나 이상 기준에 부합한 기업에 대해서만 실행한다.
---

# screen-fundamentals

## 입력
- `data/cache/<기업명>/dart.json`, `data/cache/<기업명>/fnguide.json`
- `judgment-rules.md`의 "2단계 — 스크리닝 체크리스트" 섹션 (5개 항목 정의·대체지표·Flag 기준)

## 동작
1단계 judge-* 스킬에서 하나 이상 기준에 부합한 기업에 대해서만 호출한다. 아래 5개 항목을 각각 독립적으로 평가한다.

1. **시장성** — TAM 추정치, 카테고리 성장률(YoY), TAM/시가총액 배수 계산 → 3x 미만이면 Caution.
2. **경쟁력** — 시장점유율 추이, 최근 2년 신규 경쟁 브랜드 진입 수 → 5개 이상 + 카테고리 성장 둔화면 Caution.
3. **수익성** — Gross/영업이익률 수준·추이 → 영업적자 2개 분기 이상 지속 시 Fail.
4. **재무 효율성** — ROIC, 부채비율, 이자보상배율, 자산회전율 → 이자보상배율 1 미만이 2개 분기 연속이면 Fail.
5. **ESG 부합 여부** — 공시된 ESG 등급(있는 경우), 지배구조 관련 소송/제재 이력 → 최근 1년 내 중대 이력 있으면 Caution/Fail.

ESG와 신규 경쟁사 동향처럼 데이터 키트(DART/FnGuide/FRED) 밖 정보가 필요한 항목은 Proxy로 표시하고, 확인 불가 시 "데이터 없음"으로 명시한다(임의로 Pass 처리하지 않는다).

## 출력
- 5개 항목 각각의 Flag(Pass/Caution/Fail/데이터 없음) + 근거 한 줄 — investment-desk 에이전트가 투심보고서의 "스크리닝 Flag" 섹션에 그대로 반영.

## TODO
- [ ] ESG 등급/제재 이력, 신규 경쟁 브랜드 동향 등 데이터 키트 밖 정보의 실제 소스 확정
