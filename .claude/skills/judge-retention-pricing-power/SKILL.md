---
name: judge-retention-pricing-power
description: "Retention-to-Pricing-Power" 기준(가격 인상에도 판매량/유지율이 유지되는가)으로 개별기업을 판단한다. judgment-rules.md의 기준①을 실행하는 스킬.
---

# judge-retention-pricing-power

## 입력
- `data/cache/<기업명>/dart.json`, `data/cache/<기업명>/fnguide.json`
- `judgment-rules.md`의 "1. Retention-to-Pricing-Power" 섹션

## 동작
1. 캐시된 원자료에서 ASP(또는 가격) 추이와 판매량/유지율 추이를 추출한다.
2. `judgment-rules.md`에 정의된 대체지표 기준으로 "가격 상승 + 판매량 유지"가 성립하는지 판단한다.
3. 판단 근거(사용한 수치, 기간)를 함께 남긴다.

## 출력
- 판단 결과(부합/부분부합/미부합) + 근거 요약 — investment-desk 에이전트가 최종 보고서에 통합.

## TODO
- [ ] `judgment-rules.md`의 대체지표 정의가 확정되면 그에 맞춰 판단 로직 구체화
