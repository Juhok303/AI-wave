# Red Flag / False Positive Filter

Love × Durability × Gap이 모두 그럴듯해 보여도, 아래 10종 중 2개 이상이 동시에 발동하면
**점수와 무관하게 즉시 AVOID로 강제 분류**한다(Risk Gate). 10종 전부를 빠짐없이 점검하고, 각 항목에
대해 데이터가 없으면 "확인 불가"로 명시한다(임의로 미해당 처리하지 않는다).

| # | Red Flag | 정량 기준 | 판정 |
| --- | --- | --- | --- |
| 1 | SNS 반짝 유행 | Search Trend CV > 0.8 (24M) + Branded Search 급락(3M MoM −30%↑) | 즉시 Watchlist 강등 |
| 2 | 높은 NPS·낮은 구매빈도 | Review %ile ≥ 80, Repeat Purchase %ile < 30 | Love–Behavior Divergence 경고 |
| 3 | TAM 과소 | TAM/현재 Market Cap < 3x | 투자 배제 |
| 4 | 할인 의존 성장 | Promo %/Rev YoY↑ + Revenue Growth↑ 동반 | Full-price Sell-through 확인 필수 |
| 5 | 높은 Retention·높은 CAC | LTV/CAC < 3.0 | Financial Conversion 감점 |
| 6 | Engagement–Revenue 미연결 | Engagement %ile − ARPU %ile > 40%p, 2분기↑ | 구조적 Monetization 실패 가능성 |
| 7 | 낮은 진입장벽 | 2년 내 신규 경쟁 브랜드 5개↑ + 카테고리 성장 둔화 | Moat 점수 대폭 감점 |
| 8 | 가격탄력성 취약 | 가격 인상 후 판매량 유지율 < 85% | WTP 미달, Margin 전환 가능성 낮음 |
| 9 | 이미 고평가 | EV/Sales %ile ≥ 80 | Market Recognition Gap 음수 → 배제 |
| 10 | 인위적 성장 | 마케팅비 %매출 YoY > Revenue YoY | 구매된 성장(Organic 아님) |

## 강제 규칙

**Red Flag 2개 이상 동시 발생 → Total Score·ULRS 부호와 무관하게 즉시 AVOID.** 1개만 발동한 경우는
`Risk_Penalty% = 발동 개수 × 10%p (최대 50%)`로 ULRS 공식의 `(1 − Risk_Penalty%)` 항에 반영한다.

## 메모에 채울 표

| # | Red Flag | 발동 여부 | 근거 |
| --- | --- | --- | --- |
| 1~10 | (위 10종 각각) | 발동 / 미발동 / 확인 불가 | 값 + 기간 + 출처 |
