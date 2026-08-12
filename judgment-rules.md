# 판단 규칙서 — B2C 개별기업 투자 판단 기준

> 우리 데스크는 이 기준으로 판단한다.

## Input / Scope

- **Input**: 개별기업 (기업명 또는 종목코드 1개)
- **Scope**: B2C

## 판단 기준 3가지

기업이 아래 3가지 기준에 얼마나 부합하는지 각각 판단한다. 각 기준은 "정의", "왜 가치가 있다고 보는가", "대체지표(proxy)"로 구성된다.

### 1. Retention-to-Pricing-Power

- **정의**: 가격(P)을 올려도 판매량/고객 유지율(Q)이 유지되는 구조인가 — 즉 가격 인상이 이탈로 이어지지 않는가.
- **왜 가치가 있다고 보는가**: TODO — 이 구조가 왜 장기 투자 가치로 이어지는지 근거를 채운다.
- **대체지표(proxy)**: TODO — 예) ASP(평균판매단가) YoY 증가율 vs 판매량/구독자 유지율 YoY, 데이터 출처(DART 공시 매출·원가, FnGuide 컨센서스 ASP 추정치) 명시.

### 2. Structural vs Cyclical Misclassification

- **정의**: 시장이 이 기업의 성장을 구조적(secular) 성장인데 경기순환적(cyclical)으로 오분류하고 있는지 (혹은 반대의 경우).
- **왜 가치가 있다고 보는가**: TODO — 오분류가 왜 초과수익 기회로 이어지는지 근거를 채운다.
- **대체지표(proxy)**: TODO — 예) 실적 변동성 vs 업종 평균 변동성, 매크로 지표(FRED)와의 상관관계, 컨센서스(FnGuide) 추정치의 방향성 오차.

### 3. Underpriced Customer Love (ULRS)

- **정의**: 소비자가 실제로 사랑하지만(행동·표현·인게이지먼트 지표로 확인됨) 그 애착이 아직 재무성과나 시장 밸류에이션에 반영되지 않은 상태인가 — "진짜 애착(Love×Durability)" + "그걸 돈으로 바꿀 능력(Conversion)" + "그런데 시장은 아직 모름(Gap)" 3조건이 동시에 성립하는지 판단한다.
- **왜 가치가 있다고 보는가**: Love의 절대 수준이 아니라 Love와 Price 사이의 상대적 Gap이 alpha의 원천이다. Durability를 곱(AND) 구조로 결합해 "반짝 유행"을 구조적으로 걸러내고, 전환 능력은 있는데 시장이 아직 인식 못한 기업만 남긴다.
- **대체지표(proxy)**:
  - 종합 스코어: `ULRS = √(Love%ile × Durability%ile) × Conversion_Readiness_Gap × (1 − Risk_Penalty%)`
  - `Love%ile`: 12M 재구매율, 리뷰 볼륨 증가율(YoY), DAU/MAU, 브랜드 검색점유율 변화(YoY)
  - `Durability%ile`: Retention Decay Rate, Switching Cost Proxy, 신규 진입자 침투 속도
  - `Conversion_Readiness_Gap = (Financial Conversion Capacity%ile − Market Recognition%ile) / 100` — 값이 클수록 강한 매수 신호, 음수면 자동 배제
  - `Risk_Penalty% = Red Flag 개수 × 10%p (최대 50%)`, Red Flag 2개 이상이면 점수와 무관하게 강제 Avoid
  - 데이터 출처: DART 공시(매출·마진), FnGuide 컨센서스(Estimate Revision, EV/Sales) + 리뷰/검색량/앱 데이터(Proxy, 데이터 신뢰도에 따라 0.6~1.0x 할인, 데이터 없음은 중립(50점) 처리 금지 — weight 배제 후 재정규화)
  - 상세 방법론(Layer 정의, Gap 공식, Entry Timing, Red Flag 10종, 섹터 적합도): [`docs/underpriced-customer-love-framework.md`](docs/underpriced-customer-love-framework.md)

## Output

- **투심보고서** (`reports/<기업명>-<yyyymmdd>.md`): 위 3개 기준에 대한 판단 결과 + 근거 데이터 + 종합 의견.

## 재현성 원칙

이 문서는 판단 도구(`.claude/agents/investment-desk.md` 및 관련 스킬)가 그대로 참조하는 단일 기준이다. 도구의 판단 로직이 이 문서와 다르면 안 된다 — 다른 팀이 이 문서와 도구만으로 새로운 기업을 판단할 수 있어야 완성으로 본다.
