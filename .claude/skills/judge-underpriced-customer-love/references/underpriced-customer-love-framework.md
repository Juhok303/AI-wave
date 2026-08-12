# Underpriced Customer Love — Investment Decision Tree

> 소비자가 실제로 사랑하지만 아직 재무성과·Valuation에 반영되지 않은 기업을 발굴하기 위한 판단 구조·정량지표·점수화·의사결정 규칙.
> `judgment-rules.md`의 기준③ "Underpriced Customer Love (ULRS)"의 상세 방법론. 원본 출처: 카카오톡 공유 파일 `underpriced_customer_love_framework.html`.

## A. Thesis 구조 평가

**Strengths**
- "고객 애착 → 재무 전환"이라는 인과 사슬이 명확해 검증 가능한 가설이다.
- Leading/Lagging 지표 분리 의도 자체가 뒤늦은 추종매수를 방지하는 구조다.
- Gap(괴리) 중심 접근 — Love의 절대수준이 아니라 Love와 Price 사이의 상대적 격차가 alpha의 원천이라는 인식이 정확하다.

**Weaknesses / 수정 필요**
- 원안 Layer B(Quality of Love)와 E(Competitive Durability)가 상당 부분 중복 → 통합.
- Layer C(Monetization Gap)와 F(Valuation Gap) 이름이 모호 → "Operating" vs "Market Recognition"으로 명확화.
- 경영진 자본배분(Capital Allocation) Layer가 원안에 없음 → 추가.
- Peer Group 정의 방법론 부재 → 없으면 전체 Scorecard가 자의적.

**최종 채택 Layer 구조 (8개 → 7개로 재편)**

| # | Layer명 | 원안 대비 변경 |
| --- | --- | --- |
| 1 | Customer Love (Existence & Strength) | 유지 |
| 2 | Love Durability & Defensibility | B + E 통합 |
| 3 | Operating Monetization Gap | C, 이름 명확화 |
| 4 | Financial Conversion Capacity | D + 자본배분 Sub-layer 추가 |
| 5 | Market Recognition Gap | F, 이름 명확화 |
| 6 | Catalyst & Timing | G 유지 |
| 7 | Risk / Thesis-Break | H 유지, False Positive 필터 통합 |

## B. 전체 Investment Decision Tree

```
UNDERPRICED CUSTOMER LOVE THESIS
├─ 1. CUSTOMER LOVE (존재·강도)
│   ├─ 1.1 Behavioral Love: Repeat Purchase Rate(12M), Purchase Frequency Trend, Cohort Retention Curve, Organic/Branded Search Share, Direct Traffic Share
│   ├─ 1.2 Expressed Love: Review Score(Level & Trend), Review Volume Growth, NPS/CSAT(공시 시), SNS Sentiment Net Score
│   ├─ 1.3 Engagement Depth: App DAU/MAU, Session Frequency, UGC 증가율
│   └─ 1.4 Willingness to Pay(WTP): 가격 인상 후 판매량 유지율, Full-price Sell-through Rate, 할인 의존도(Promo % of Revenue)
├─ 2. LOVE DURABILITY & DEFENSIBILITY
│   ├─ 2.1 Temporal Durability: Cohort Retention 감쇠율, Search Trend 변동성(유행성 여부), 신규 vs 기존 고객 매출 비중 안정성
│   └─ 2.2 Competitive Moat: Switching Cost Proxy, Community/Network Effect, IP/제형/기술 특허, 신규 진입자 카테고리 침투 속도
├─ 3. OPERATING MONETIZATION GAP
│   ├─ 3.1 Revenue Monetization: ARPU/ARPU Growth, Revenue per Loyal Customer
│   ├─ 3.2 Margin Monetization: Gross Margin, Contribution Margin, CAC Payback
│   └─ 3.3 Capital Allocation Signal: Marketing Spend %/Rev, 확장 vs 수익화 우선순위
├─ 4. FINANCIAL CONVERSION CAPACITY
│   ├─ 4.1 Unit Economics: LTV/CAC, Contribution Margin Trajectory
│   ├─ 4.2 Operating Leverage: Fixed Cost Ratio, GM→EBIT 전환 속도
│   └─ 4.3 Capital Discipline: FCF Conversion, Reinvestment vs ROIC
├─ 5. MARKET RECOGNITION GAP
│   ├─ 5.1 Sell-side Expectation Gap: Consensus vs 우리 추정, Estimate Revision
│   └─ 5.2 Valuation Gap: EV/Sales Percentile, Implied Growth Reversal
├─ 6. CATALYST & ENTRY TIMING: Stage 1~5 KPI Trigger (F절)
└─ 7. RISK / THESIS-BREAK / FALSE POSITIVE FILTER: Red Flag 10종(H절), Thesis-break 조건(I절)
```

## C. Layer별 상세 설계

표기: L/C/G = Leading/Confirming/Lagging.

### C-1. Customer Love

| Sub-layer | Metric | Formula | Data Source | L/C/G | Benchmark | Weight |
| --- | --- | --- | --- | --- | --- | --- |
| Behavioral | 12M Repeat Purchase Rate | 재구매 고객수 / 총 구매고객수(12M) | 공시·IR·카드데이터 Proxy | Leading | Peer Percentile | 20% |
| Behavioral | Cohort Retention (M1→M12) | 코호트별 잔존율 곡선 | 공시(제한적) | Leading | 곡선 기울기 Peer비교 | 15% |
| Behavioral | Branded Search Share | Brand 검색량 / (Brand+Category 검색량) | Google Trends Proxy | Leading | YoY %p 변화 | 15% |
| Expressed | Review Score Trend | 최근 6M 평균 − 이전 6M 평균 | App/이커머스 리뷰 | Leading | Peer 대비 방향성 | 15% |
| Expressed | Review Volume Growth | YoY 리뷰수 증가율 | 동일 | Leading | 매출성장률과 디커플링 여부 | 10% |
| Engagement | DAU/MAU (Stickiness) | DAU / MAU | App Analytics Proxy | Leading | Peer Percentile | 15% |
| WTP | 가격 인상 후 판매량 유지율 | 인상 후 3M 판매량 / 인상 전 3M 판매량 | 회사 발표·채널데이터 | Confirming | >90% = 강한 WTP | 10% |

경제적 논리: Behavioral·Expressed·Engagement는 향후 매출 성장의 선행 신호, WTP는 향후 마진 확장(가격결정력)의 선행 신호. 두 축을 분리해야 "성장만 있고 마진은 없는" 기업을 구분할 수 있다.

### C-2. Love Durability & Defensibility

| Sub-layer | Metric | Formula | DA | L/C/G | Weight |
| --- | --- | --- | --- | --- | --- |
| Temporal | Retention Decay Rate | (M1 Retention − M12 Retention)/M1 | 공시(제한적)/Proxy | Confirming | 20% |
| Temporal | Search Trend 변동성(CV) | 표준편차/평균 (24M) | Proxy(Medium) | Leading | 15% |
| Temporal | 신규 vs 기존고객 매출 비중 안정성 | 분기별 비중의 표준편차 | 공시 | Confirming | 15% |
| Moat | Switching Cost Proxy | 구독/락인 계약 비중, 데이터 락인 | 정성 → 0/1/2 | Confirming | 20% |
| Moat | 신규 진입자 침투 속도 | 최근 2년 신규 브랜드 출시 수 | 산업 리포트 | Leading | 15% |
| Moat | IP/기술 보유 | 특허수, 독점 원료/제형 계약 | 공시 | Confirming | 15% |

경제적 논리: Layer1이 "지금 사랑받는가"라면 Layer2는 "그 사랑이 복제·모방·유행 소멸에 얼마나 강한가". 두 Layer를 AND 조건(곱)으로 결합해야 "반짝 유행"을 걸러낸다.

### C-3. Operating Monetization Gap

| Sub-layer | Metric | Formula | DA | L/C/G | Weight |
| --- | --- | --- | --- | --- | --- |
| Revenue | ARPU Growth | (ARPUₜ−ARPUₜ₋₁)/ARPUₜ₋₁ | 공시 | Confirming | 25% |
| Revenue | Revenue per Loyal Customer | 반복구매 매출/반복구매 고객수 | 공시(드묾)→Proxy | Confirming | 20% |
| Margin | Gross Margin Trend | 3Y Trend, YoY %p | 공시 | Confirming | 20% |
| Margin | CAC Payback Period | CAC / (ARPU×GM%/월) | 공시/역산 | Confirming | 20% |
| Capital | Marketing Spend %/Rev Trend | 마케팅비/매출, 방향성 | 공시 | Confirming | 15% |

Gap 정의(핵심): "Love가 높음에도 위 지표들의 Peer Percentile이 낮다"는 사실 자체가 투자 시그널이다 (E절 공식화).

### C-4. Financial Conversion Capacity

| Sub-layer | Metric | Formula | DA | L/C/G | Weight |
| --- | --- | --- | --- | --- | --- |
| Unit Econ | LTV/CAC | (ARPU×GM%×평균 Retention기간)/CAC | 역산(Medium) | Confirming | 25% |
| Op Leverage | Incremental Margin | ΔEBIT/ΔRevenue | 공시 | Confirming | 25% |
| Op Leverage | Fixed Cost Ratio | 고정비/매출 Trend | 공시 | Lagging | 15% |
| Capital | FCF Conversion | FCF/EBITDA | 공시 | Lagging | 20% |
| Capital | Reinvestment vs ROIC | 재투자율, ROIC Trend | 공시 | Lagging | 15% |

자본배분 정성 Overlay: 실적발표 콜에서 "재구매/코호트/마진" 언급 빈도 변화를 텍스트 마이닝해 "성장 우선→수익화 우선" 전환 신호로 사용 (Confidence: Low, Proxy 표시 필수).

### C-5. Market Recognition Gap

| Sub-layer | Metric | Formula | DA | L/C/G | Weight |
| --- | --- | --- | --- | --- | --- |
| Sell-side | Estimate Revision Momentum | 최근 3M 컨센서스 변화율 | FnGuide 컨센서스 | Confirming | 30% |
| Sell-side | Coverage Breadth | 애널리스트 수, Buy 비중 | 데이터 벤더 | Confirming | 10% |
| Valuation | EV/Sales Peer Percentile | 산업 내 백분위 | 시장 데이터 | Lagging | 30% |
| Valuation | Implied Growth Reversal | Multiple 역산 CAGR vs 우리 추정 | DCF 역산 | Confirming | 30% |

## D. 100점 Scorecard

가중치는 "이 Layer가 얼마나 직접적으로/빠르게 주가 re-rating에 연결되는가"를 기준으로 배분.

| Layer | 가중치 | 배분 논리 |
| --- | --- | --- |
| 1. Customer Love | 15 | 필요조건이지만 그 자체로는 주가와 직결 안 됨(가장 흔한 착시 원인) |
| 2. Love Durability & Defensibility | 15 | Love가 진짜인지 검증하는 게이트. 낮으면 이후 Layer 전체에 페널티 |
| 3. Operating Monetization Gap | 20 | 이 Thesis의 핵심 — Gap이 클수록 잠재 alpha 큼 |
| 4. Financial Conversion Capacity | 20 | Gap이 실제 재무성과로 "전환될 능력"이 있는지가 성패를 가름 |
| 5. Market Recognition Gap | 15 | 아무리 좋아도 시장이 이미 안다면 alpha 없음 (핵심 절제 조건) |
| 6. Catalyst 근접성 | 10 | 전환 시점의 가시성 — Holding Period와 IRR에 직결 |
| Risk Penalty | −0~15 | False Positive Red Flag 개수·강도에 비례 차감 |

```
Layer Score = Σ(Metric Peer Percentile × Metric Weight)      [0~100]
Total Score = Σ(Layer Score × Layer Weight%) − Risk Penalty
```

각 Metric 행은 `Raw Metric | YoY 변화 | 3Y Trend | Peer Median 대비 차이 | Peer Percentile | Weight | Score`를 모두 채운다.

게이트 규칙: Layer2(Durability)가 40점 미만이면 총점이 아무리 높아도 Total Score에 상한(cap) 60점을 적용한다 — 일시적 유행을 "저평가된 사랑"으로 오판하는 것을 구조적으로 차단.

## E. Underpricing / Gap Formula

Section E는 `references/underpricing_gap_test.md`로 승격됐다 — 정규화 원칙, Peer Group 3중 필터,
Gap 공식 5종, Signal 유효성 판정 전부 그 문서를 따른다(여기서 중복 서술하지 않는다).

## F. Entry Timing Framework

| Stage | 조건(정량 Trigger) | 판단 | 주요 관찰 KPI |
| --- | --- | --- | --- |
| 1. Watchlist | Layer1 %ile ≥ 70, Layer3 %ile < 40, 재무개선 신호 없음 | 관찰만 | Review/Search Trend |
| 2. Early Entry | 최근 2개 분기 연속 GM 또는 ARPU YoY 개선 시작 | 분할매수(30~40%) | CAC Payback 단축, Retention 개선 |
| 3. Main Entry | 첫 분기 Consensus 상회 + Margin Beat, Revision 방향전환 | 핵심 매수(60~70%) | Estimate Revision 양전환 |
| 4. Late Entry | 2개 분기 연속 Beat, 커버리지 증가, Multiple 이미 상승 | 추가매수 제한적 | Coverage Breadth 증가율 |
| 5. Fully Priced | EV/Sales %ile ≥ 75, Implied Growth ≈ 우리 추정 | 신규매수 금지, Exit 검토 | Gap ≈ 0 |

## G. Catalyst Framework

| Catalyst 유형 | 확인 KPI | 예상 시차(Love→재무 반영) |
| --- | --- | --- |
| 재구매율 최초 공개 | 공시/IR 자료 | 즉시(가격 반영은 1~2주) |
| Cohort 데이터 공개 | 실적발표 슬라이드 | 즉시~1개월 |
| 가격 인상 성공 | 다음 분기 판매량 유지 확인 | 1개 분기 |
| 마진 개선 첫 분기 | 실적발표 | 즉시~1개월 |
| 신규 채널 성숙(Cohort 3) | 매장별 실적 공시(제한적) | 2~4개 분기 |
| 애널리스트 커버리지 개시/상향 | 리서치 발간 | 발간 즉시 |

Catalyst는 Layer1(Leading) → Layer3(Confirming) → Layer5(시장 반응)의 시간 순서를 따르며, 이 순서가 Entry Stage와 1:1 대응된다.

## H. Risk & False Positive Filter

Section H는 `references/red_flag_test.md`로 승격됐다 — Red Flag 10종 정량 기준과 강제 AVOID
규칙(2개 이상 동시 발동 시)은 그 문서를 따른다(여기서 중복 서술하지 않는다).

## I. Holding Period & Exit Rule

```
예상 Holding Period = Stage 도달까지 예상 분기수(Stage2→4) + Re-rating 반영 지연(1~2분기)
```

Catalyst 예상 시차(G절)의 합으로 기업별 개별 산정하며, 고정 1~2년 가정은 초기값(prior)으로만 사용한다.

| Exit 유형 | 정량 조건 |
| --- | --- |
| Successful Exit | Market Recognition Gap이 5%p 이내로 수렴 & EV/Sales %ile ≥ 65 |
| Thesis-break Exit | Layer1 또는 Layer2 %ile이 2개 분기 연속 20%p↑ 하락 |
| Time-stop Exit | Entry 후 6개 분기 경과해도 Operating Monetization Gap 미축소(오히려 확대) |

## J. Sector Fit Matrix

| 산업 | Fit | 핵심 Love Metric | 핵심 Monetization Metric | 핵심 Catalyst | 최대 False Positive |
| --- | --- | --- | --- | --- | --- |
| Apparel/Fashion | 중 | Full-price Sell-through | Gross Margin | 가격인상 성공 | 유행성 |
| Beauty | 높음 | Repeat Purchase, Review Growth | ARPU, Repeat Revenue | Cohort 공개 | 인플루언서發 반짝 성장 |
| Restaurants/F&B | 낮음~중 | Traffic, Repeat Visit | Same-store Sales | 매장 성숙 Cohort | 프로모션 의존 |
| Consumer Subscription | 높음 | Retention Curve, Churn | ARPU, LTV/CAC | Cohort 공개, 가격인상 | 초기 무료체험 왜곡 |
| Consumer Software/Apps | 높음 | DAU/MAU, Retention | ARPU, Conversion Rate | 유료전환율 개선 | Engagement–Revenue 미연결 |
| Gaming | 중 | DAU, Session | ARPPU | 신규 콘텐츠 흥행 | 콘텐츠 사이클 의존 |
| E-commerce | 중 | Repeat Purchase, Direct Traffic | AOV, CAC Payback | 물류/마진 레버리지 | 할인 의존 |
| Marketplace | 중 | Take Rate 여력, GMV Repeat | Take Rate Trend | Take Rate 인상 | Supply-Demand 불균형 |
| Travel/Leisure | 낮음 | Repeat Booking | ARPU/Booking | 계절 성수기 확인 | 경기민감 왜곡 |
| Luxury | 낮음 | Full-price Sell-through | Gross Margin | 가격결정력 확인 | 이미 고평가 상시 |
| Consumer Electronics | 낮음 | Repeat Upgrade | ASP Trend | 신제품 사이클 | 제품 사이클 의존 |
| Fitness | 중 | Retention, Engagement | ARPU | 가격인상 유지율 | 시즌성(1월 효과) |
| Entertainment/Media | 낮음~중 | Engagement, Watch Time | ARPU, Ad Load | 구독 가격인상 | Content Cliff |

추천 초기 Universe: ① Beauty ② Consumer Subscription ③ Consumer Software/Apps — 리뷰·앱데이터로 Behavioral Love가 자동 수집 가능하고, Cohort/Retention 공시 관행 또는 신뢰도 높은 Proxy가 있으며, Monetization Gap이 마진/ARPU로 명확히 관측되는 산업.

## K. Core Version (실전 탑재용 축소판)

7개 Layer 전체를 매 종목마다 풀 계산하는 것은 데이터 가용성상 비현실적. 최소 탑재 Core Metric 12개:

1. 12M Repeat Purchase Rate (또는 Proxy)
2. Review Volume Growth (YoY)
3. Branded Search Share 변화(YoY)
4. DAU/MAU (해당 시)
5. 가격 인상 후 판매량 유지율
6. Retention Decay Rate (Durability 게이트)
7. Gross/Contribution Margin Trend
8. CAC Payback Period
9. LTV/CAC
10. Estimate Revision Momentum(3M)
11. EV/Sales Peer Percentile
12. Red Flag Count (0~10)

**데이터 신뢰도 처리 원칙**

| Confidence | 데이터 유형 | 처리 |
| --- | --- | --- |
| High | Direct 공시/회사 발표 | 그대로 반영 |
| Medium | Third-party(앱분석, 검색량) | Score 0.8x 할인 |
| Low | Proxy(역산 추정) | Score 0.6x 할인 |
| N/A | 데이터 없음 | 중립(50점) 처리 금지 — Weight의 50%만 인정, 나머지 50%는 재정규화(re-normalize)로 제외 |

왜 "정보 없음=중립"이 아닌가: 정보 없음을 중립(50점)으로 처리하면 데이터가 없는 기업이 오히려 페널티를 피해가는 역설이 발생하기 때문이다.

## 최종 Composite Metric — ULRS (Underpriced Love Recognition Score)

```
ULRS = [ (Love × Durability)^0.5 ] × Conversion_Readiness_Gap × (1 − Risk_Penalty%)
```

- `Love` = Layer1 Percentile (0~100), Customer Love 강도
- `Durability` = Layer2 Percentile (0~100), 애착의 지속가능성/방어력. 기하평균을 쓰는 이유 — 산술평균은 "Love=100, Durability=0"인 반짝 유행주도 50점을 줘버려 False Positive를 못 거른다. 하나라도 낮으면 전체가 크게 깎이는 AND 조건 구조가 필요.
- `Conversion_Readiness_Gap` = (Layer4 %ile − Layer5 %ile)/100 — "전환 능력은 있는데 시장은 아직 모른다"의 크기. 음수(시장이 이미 앞서감)면 ULRS 자체가 음수가 되어 자동 배제 신호가 됨.
- `Risk_Penalty%` = H절 Red Flag 개수 × 10%p (최대 50%)

**해석**
- ULRS > 0 (값 클수록): Love가 진짜(Durability 확인)이며, 회사는 재무 전환 능력이 있는데 시장은 아직 반영 안 함 — 최적 매수 구간
- ULRS ≈ 0: Gap이 이미 닫혔거나 전환 능력 자체가 미증명 — Watchlist
- ULRS < 0: 시장이 이미 더 낙관적이거나 Love/Durability 자체가 약함 — Avoid

이 Thesis의 본질은 "좋은 기업 찾기"가 아니라 **① 진짜 애착(Love×Durability) ② 그것을 돈으로 바꿀 능력(Conversion) ③ 그런데 시장은 아직 모름(Gap)**이라는 세 조건의 동시 성립이다. ULRS는 이 세 조건을 곱셈 구조로 강제하여, 어느 한 조건이라도 무너지면 전체 점수가 급격히 낮아지도록 설계했다.
