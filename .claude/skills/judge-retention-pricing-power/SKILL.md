---
name: judge-retention-pricing-power
description: "Retention-to-Pricing-Power" 기준(가격 인상에도 판매량/유지율이 유지되는가)으로 개별기업을 판단한다. judgment-rules.md의 기준①을 실행하는 스킬.
---

# judge-retention-pricing-power

## 입력
- `data/cache/<기업명>/dart.json`, `data/cache/<기업명>/fnguide.json`
- `judgment-rules.md`의 "1. Retention-to-Pricing-Power" 섹션

## 동작

1. **Secondary 우선 확인**: `fnguide.json`에 ASP·판매량(또는 가입자) 추정치가 있으면 그 YoY를 직접 비교한다. 둘 다 (+)이면 강한 부합 신호(High Confidence)로 우선 채택하고 4번으로 건너뛴다.
2. **Primary 계산 (fnguide 없거나 보조용)**: `dart.json`의 `income_statement`에서 당기/전기 `매출액`, `매출총이익`으로 아래를 계산한다.
   ```
   매출총이익률(당기) = 매출총이익(당기) / 매출액(당기)
   매출총이익률(전기) = 매출총이익(전기) / 매출액(전기)
   매출액 YoY = (매출액(당기) − 매출액(전기)) / 매출액(전기)
   ```
   전전기 데이터도 있으면 동일 계산을 한 번 더 해서 "2개년 연속 유지" 여부를 확인한다.
3. **정성 보강**: `web.json`에 가격 인상 관련 뉴스/리뷰가 있으면 이탈·불매 언급 여부를 함께 기록한다(Low Confidence, 보조 근거로만 사용).
4. `judgment-rules.md` "1. Retention-to-Pricing-Power"의 판단 기준표를 그대로 적용해 부합/부분부합/미부합을 정한다:
   - 매출총이익률 2개년 연속 유지 이상(또는 ASP·판매량 동반 상승) **AND** 매출액 YoY (+) → **부합**
   - 매출총이익률 개선되나 매출액 YoY 정체/감소 → **부분부합**
   - 매출총이익률 하락 + 매출액 YoY 정체/감소 → **미부합**
5. 사용한 실제 수치(매출총이익률 두 기간, 매출액 YoY %, 데이터 출처·신뢰도)를 근거로 남긴다.

## 출력
- 판단 결과(부합/부분부합/미부합) + 사용한 수치와 근거(어떤 데이터·신뢰도로 판단했는지) + 적용한 `judgment-rules.md` 조항(기준① 판단 기준 중 어느 문장에 해당하는지) — investment-desk 에이전트가 최종 보고서에 통합. 이 문서에 없는 별도 기준으로 판단하지 않는다.

## 데이터 부족 시 처리
`dart.json`에 매출총이익률 계산에 필요한 계정이 없거나 연속 2개년 데이터가 없으면, 그 사실을 명시하고 "판단 보류(데이터 부족)"로 표시한다. 임의로 부합/미부합을 추정하지 않는다.
