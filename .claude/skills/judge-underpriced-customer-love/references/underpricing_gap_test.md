# Underpricing / Gap Test

이 스킬에서 가장 중요한 단일 분석이다. "Love가 있다"는 것만으로는 충분하지 않다 — Love와 Price
사이의 **상대적 격차(Gap)**가 alpha의 원천이라는 것이 이 철학의 핵심 주장이다. 아래를 순서대로
채운다. 데이터가 없으면 "Insufficient Data"라고 쓰고 임의로 채우지 않는다.

## 0. 정규화 원칙 (Gap 계산 전에 반드시 적용)

1. 모든 Metric은 raw 값이 아니라 **산업 내 Percentile Rank(0~100)**로 변환 후 비교한다. 표본이
   20개 미만인 소규모 Peer Group에서는 z-score를 보조로 병기한다.
2. **Peer Group 정의**: 3중 필터 — ① 동일 업종/카테고리 ② 매출 규모 0.3x~3x ③ 유통채널 유사성.
   이 레포에서 정식 Peer DB가 없을 때의 축소판 절차는 SKILL.md의 "Peer Group 축소판" 절을 따른다.
3. **산업별 보정**: 절대치 비교 금지, 산업 내 percentile만 비교한다(예: Apparel의 GM 40%와
   Software의 GM 40%는 의미가 다르다).

## 1. 핵심 Gap 공식 (5종)

| Gap | 공식 | 경제적 의미 |
| --- | --- | --- |
| Love–Monetization Gap | Layer1 %ile − Layer3 %ile | 애착은 있는데 못 팔고 있음 |
| Love–Margin Gap | Layer1 %ile − Margin %ile | 애착은 있는데 마진화 안 됨 |
| Love–Valuation Gap | Layer1 %ile − EV/Sales %ile | 시장이 애착을 가격에 안 넣음 |
| Durability-adjusted Gap | (Layer1×Layer2 결합) − Layer3 %ile | "가짜 사랑"을 걸러낸 순수 Gap |
| **Conversion-Readiness Gap** | Layer4 %ile − Layer5 %ile | 전환 능력은 있는데 시장 기대는 낮음 — **가장 강력한 Signal, ULRS 공식에 직접 사용** |

## 2. Signal 유효성 판정

Gap ≥ 25%p이고, 동시에 **최근 2개 분기 연속 Gap 축소 방향**일 때만 유효 Signal로 인정한다.
Gap이 크지만 정체·확대 중이면 "구조적 실패" 가능성(False Positive 후보)이므로, 유효 Signal이
아니라고 명시한다.

## 3. 메모에 채울 표

| Gap | 값(%p) | 최근 2개 분기 추세(축소/정체/확대) | 유효 Signal 여부 |
| --- | ---:| --- | --- |
| Love–Monetization | | | |
| Love–Margin | | | |
| Love–Valuation | | | |
| Durability-adjusted | | | |
| Conversion-Readiness | | | |

`Conversion-Readiness Gap`은 `judgment-rules.md` 기준③의 `ULRS = √(Love%ile × Durability%ile) ×
Conversion_Readiness_Gap × (1 − Risk_Penalty%)` 공식에 그대로 대입한다 — 이 문서와 다른 값을
만들어내지 않는다.
