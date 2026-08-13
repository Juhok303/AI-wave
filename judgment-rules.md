# 판단 규칙서 — B2C 개별기업 투자 판단 기준

> 우리 데스크는 이 기준으로 판단한다.

## Input / Scope

- **Input**: 개별기업 (기업명 또는 종목코드 1개)
- **Scope**: B2C

### Scope Gate (판단을 시작하기 전 가장 먼저 확인)

대상 기업이 이 규칙서의 적용 대상(B2C)인지부터 확인한다. 주력 매출·사업 구조가 **기업 대상(B2B)**이거나, B2C로 보기 어려운 경우(금융지주·순수 지주회사·공공기관 등)는 이 판단 규칙서의 적용 대상이 **아니다**. 이런 기업이면 `fetch-*`/`judge-*` 등 데이터 수집·판단 단계를 아예 시작하지 않고, 그 자리에서 "이 도구(AI-wave)는 B2C 기업만 다룬다"는 사실과 판단 근거(왜 B2C가 아니라고 봤는지)를 사용자에게 알린 뒤 종료한다 — 억지로 판단을 진행해 미부합/판단 보류로 채우지 않는다.

이건 각 기준 스킬의 자체 Universe Filter(그 철학이 이 기업에 맞는지, 예: Framework Fit High/Medium/Low)와는 다른 단계다 — Scope Gate는 "B2C 자체가 맞는가"라는 더 앞선 질문이고, Universe Filter는 "B2C인 걸 전제로 이 철학이 이 기업에 맞는가"라는 다음 질문이다.

기업이 아래 3가지 기준에 얼마나 부합하는지 각각 판단한다. 각 기준은 "정의", "왜 가치가 있다고 보는가", "대체지표(proxy)"로 구성된다.

**3개 기준을 모두 만족할 필요는 없다.** 기준별로 부합/부분부합/미부합을 독립적으로 판단하고, 하나 이상 부합하는 기준이 있으면 다음 단계(스크리닝)로 넘어간다. 3개 모두 미부합이면 그 시점에 투자 매력이 없는 것으로 보고 판단을 종료한다 — 어떤 기준(들)에 왜 부합하는지가 투심보고서의 핵심 판단 결과다.

### 1. Retention-to-Pricing-Power

> Source of truth: `.claude/skills/judge-retention-pricing-power/`(pjueun) — SKILL.md가 곧 이 기준의 정의다. `references/`(Layer A-G, Pricing Power Test, Financial Transmission, Variant Perception, Catalyst/Entry, Scorecard/Gates, Output Template)에 전체 방법론이 있다.

- **정의**: 이 기업의 높은 Retention이 아직 시장이 충분히 가격에 반영하지 않은 Pricing Power로 전환되고 있는가 — `Retention ↑ → Purchase Frequency ↑/Churn ↓ → LTV ↑ → CAC Payback ↓ → Pricing/Mix ↑ → Gross Margin ↑ → Contribution Margin ↑ → Operating Leverage → EPS/FCF Revision → Multiple Re-rating`의 인과 체인이 실제로 이어지는지, 어디서 끊기는지를 본다(`references/financial_transmission.md`).
- **왜 가치가 있다고 보는가**: 가격 인상 후에도 갱신율·재구매가 유지된다는 사실 자체는 이미 널리 알려진 컨센서스 스토리인 경우가 많다. 진짜 초과수익은 그 가격결정력이 아직 상품마진/영업레버리지로 다 전이되지 않았는데 시장은 여전히 Volume/User Growth 중심으로만 가치평가하고 있는 지점에서 나온다 — 시장이 "이미 아는 좋은 점"과 "아직 반영 안 한 지점"을 구분해야 한다.
- **판정**: `references/scorecard_and_verdict.md`의 **최종 Verdict**(Core Thesis Test의 중간 판정 Supported/Partially/Not이 아니라, Gate 적용 후 나오는 최종 판정)를 기준으로 매핑한다 — **BUY → 부합**, **WATCH → 부분부합**, **PASS(또는 Gate 위반) → 미부합**. SELL은 기존 보유분 매도 판단용이라 신규 판단(1단계 필터링)에는 등장하지 않는다. 100점 스코어카드(Layer A-G, 4개 Gate)는 그대로 따르고 이 문서에서 별도 임계값을 만들지 않는다.
- **참고 예시**: [`.claude/skills/judge-retention-pricing-power/assets/example-memo-costco.html`](.claude/skills/judge-retention-pricing-power/assets/example-memo-costco.html) (Costco 적용 사례, pjueun).
- ⚠️ 이 스킬은 Claude.ai 출력 관례(`/mnt/user-data/outputs/`, `present_files`)로 작성돼 있어 `investment-desk`가 자동 호출할 때는 이 레포의 `reports/` 관례로 저장 경로를 바꿔 적용해야 한다(SKILL.md 자체는 원작자 그대로 유지, 호출 시점에 오케스트레이터가 보정).

### 2. Structural vs Cyclical Misclassification

> Source of truth: `.claude/skills/judge-structural-vs-cyclical/`(chaemin) — SKILL.md가 곧 이 기준의 정의다. `references/`(Layer A-G, Cyclical Contamination Test, Financial Transmission, Variant Perception, Catalyst/Entry, Scorecard/Gates, Output Template)에 전체 방법론이 있다.

- **정의**: 소비자 행동의 구조적 변화를 시장이 경기순환이나 일시적 유행으로 오인해 Multiple을 잘못 매기고 있는가(또는 반대로 순환적 변화를 구조적으로 오인해 고평가하고 있는가).
- **왜 가치가 있다고 보는가**: 구조적 성장기업이 경기순환주로 오분류되면 경기 저점에서 밸류에이션이 과도하게 할인되고, 오분류가 풀리는 리레이팅 시점에 이익 성장과 별개인 멀티플 확장 alpha가 발생한다. 이 철학은 확증편향 위험이 특히 크다 — "구조적이다"는 주장은 사후적으로만 완전히 검증되므로, 경기 하방 동행 여부(Layer 2, Cyclical Contamination Test)를 반드시 반증 시도해야 하며 Bear case를 Bull case와 동등한 무게로 다뤄야 한다.
- **판정**: `references/scorecard_and_verdict.md`의 **최종 Verdict**(Core Thesis Test의 중간 판정 Supported/Partially/Not이 아니라, Gate 적용 후 나오는 최종 판정)를 기준으로 매핑한다 — **BUY(Score ≥80, 전 Gate 통과) → 부합**, **WATCH(Score 65~79) → 부분부합**, **PASS(Score 50~64 또는 Gate 위반) → 미부합**. SELL은 기존 보유분 매도 판단용이라 신규 판단(1단계 필터링)에는 등장하지 않는다. 100점 스코어카드(Layer A-G 재가중, 4개 Gate)는 그대로 따르고 이 문서에서 별도 임계값을 만들지 않는다. 이 매핑 규칙은 `judge-structural-vs-cyclical/SKILL.md`와 `references/scorecard_and_verdict.md` 안에도 동일하게 명시돼 있다(2026-08-13 정합성 확인).
- **참고 예시**: [`.claude/skills/judge-structural-vs-cyclical/assets/example-memo-onon.html`](.claude/skills/judge-structural-vs-cyclical/assets/example-memo-onon.html) (chaemin).
- ⚠️ 이 스킬도 `/mnt/user-data/outputs/` 관례로 작성돼 있어 `investment-desk` 호출 시 `reports/` 관례로 저장 경로를 보정해야 한다(위 기준① 참고).

### 3. Underpriced Customer Love (ULRS)

- **정의**: 소비자가 실제로 사랑하지만(행동·표현·인게이지먼트 지표로 확인됨) 그 애착이 아직 재무성과나 시장 밸류에이션에 반영되지 않은 상태인가 — "진짜 애착(Love×Durability)" + "그걸 돈으로 바꿀 능력(Conversion)" + "그런데 시장은 아직 모름(Gap)" 3조건이 동시에 성립하는지 판단한다.
- **왜 가치가 있다고 보는가**: Love의 절대 수준이 아니라 Love와 Price 사이의 상대적 Gap이 alpha의 원천이다. Durability를 곱(AND) 구조로 결합해 "반짝 유행"을 구조적으로 걸러내고, 전환 능력은 있는데 시장이 아직 인식 못한 기업만 남긴다.
- **대체지표(proxy)**:
  - 종합 스코어: `ULRS = √(Love%ile × Durability%ile) × Conversion_Readiness_Gap × (1 − Risk_Penalty%)`
  - `Love%ile`: 12M 재구매율, 리뷰 볼륨 증가율(YoY), DAU/MAU, 브랜드 검색점유율 변화(YoY)
  - `Durability%ile`: Retention Decay Rate, Switching Cost Proxy, 신규 진입자 침투 속도
  - `Conversion_Readiness_Gap = (Financial Conversion Capacity%ile − Market Recognition%ile) / 100` — 값이 클수록 강한 매수 신호, 음수면 자동 배제
  - `Risk_Penalty% = Red Flag 개수 × 10%p (최대 50%)`, Red Flag 2개 이상이면 점수와 무관하게 강제 Avoid
  - 데이터 출처: DART 공시(매출·마진), FnGuide 컨센서스(Estimate Revision, EV/Sales) + `fetch-web`이 수집하는 리뷰/뉴스 데이터(Proxy, 데이터 신뢰도에 따라 0.6~1.0x 할인, 데이터 없음은 중립(50점) 처리 금지 — weight 배제 후 재정규화)
- **판정**: `references/scorecard_and_verdict.md`의 **최종 Verdict**(100점 스코어카드 + 5개 Gate 적용 후 나오는 판정 — 기준①②와 동일한 Score+Gate 임계값 아키텍처, 2026-08-13부터 적용)를 기준으로 매핑한다 — **BUY(Score ≥80, 전 Gate 통과) → 부합**, **WATCH(Score 65~79) → 부분부합**, **AVOID(Score 50~64 또는 Gate 위반, Red Flag 2개↑ 포함) → 미부합**. ULRS 공식은 폐기하지 않고 Market Recognition Gate 판정 근거·Entry Timing 산정용 진단 지표로 남는다(더 이상 ULRS 부호가 Verdict를 직접 정하지 않는다).
- **참고 예시**: [`.claude/skills/judge-underpriced-customer-love/assets/example-memo-duolingo.html`](.claude/skills/judge-underpriced-customer-love/assets/example-memo-duolingo.html) (Duolingo 적용 사례).
- 상세 방법론(Layer 정의, Gap 공식, Entry Timing, Red Flag 10종, 섹터 적합도): [`.claude/skills/judge-underpriced-customer-love/references/underpriced-customer-love-framework.md`](.claude/skills/judge-underpriced-customer-love/references/underpriced-customer-love-framework.md)

## 2단계 — 스크리닝 체크리스트

1단계에서 하나 이상의 기준에 부합한 기업만 대상으로, 아래 5개 항목을 추가로 평가해 **flag**한다. 이 항목들은 "왜 사야 하는가"(1단계 핵심 테제)와는 성격이 달라 점수화하지 않고, 항목별로 Pass/Caution/Fail만 표시한다 — "사도 되는가"에 대한 기초체력·리스크 점검이다.

| 항목 | 정의 | 대체지표(proxy) | Flag 기준 |
| --- | --- | --- | --- |
| 시장성 | 카테고리 시장 규모·성장성이 투자 매력을 뒷받침하는가 | TAM 추정치, 카테고리 성장률(YoY), TAM/현재 시가총액 배수 | TAM/시총 < 3x → Caution |
| 경쟁력 | 동종업계 대비 시장 지위·차별화가 견고한가 | 시장점유율 추이, 최근 2년 신규 경쟁 브랜드 진입 수 | 신규 경쟁 브랜드 5개↑ + 카테고리 성장 둔화 → Caution |
| 수익성 | 매출을 실제 이익으로 안정적으로 전환하는가 | Gross/영업이익률 수준·추이, Peer 대비 위치 | 영업적자 2개 분기 이상 지속 → Fail |
| 재무 효율성 | 자본을 효율적으로 운용하는가 | ROIC, 부채비율, 이자보상배율, 자산회전율 | 이자보상배율 &lt; 1이 2개 분기 연속 → Fail |
| ESG 부합 여부 | 지배구조·환경·사회 리스크가 투자를 저해할 수준인가 | 공시된 ESG 등급(있는 경우), 지배구조 관련 소송/제재 이력 | 최근 1년 내 중대 ESG 제재·소송 이력 → Caution/Fail |

데이터 출처: 시장성/경쟁력/수익성/재무효율성은 DART 공시·FnGuide 업종 비교로 대부분 커버 가능. ESG와 일부 경쟁력 지표(신규 경쟁사 동향)는 데이터 키트 밖 정보(뉴스, 외부 ESG 평가, `fetch-web` 스킬이 수집)가 필요해 Proxy로 표시한다.

## Output

- **최종 투심보고서 형식은 HTML 단일 파일이다** (`reports/<기업명>-<yyyymmdd>.html`). `docs/report-format-reference.md`에 정리된 증권사 리포트 양식(표지 스냅샷 박스, 투자판단/목표주가 verdict 박스, 표 중심 레이아웃, 색상 시스템)을 참고해 디자인한다 — 원본 리포트의 문장·수치를 베끼는 게 아니라 레이아웃·타이포그래피·표 구조만 재사용한다.
- 내용 구성은 동일하게 유지한다: (1) 1단계 — 어떤 핵심 기준에 부합하는지 + 근거 데이터, (2) 2단계 — 스크리닝 체크리스트 5개 항목의 Flag 결과, (3) 종합 의견.
- 작업 중간 산출물(각 판단 스킬의 마크다운 메모 등)은 `reports/`에 함께 남겨도 되지만, "완성된 결과물"로 인정되는 것은 HTML 파일이다. PDF 등 별도 바이너리 변환은 하지 않는다 — HTML 자체가 최종 산출물이다.

## 재현성 원칙

이 문서는 판단 도구(`.claude/agents/investment-desk.md` 및 관련 스킬)가 그대로 참조하는 단일 기준이다. 도구의 판단 로직이 이 문서와 다르면 안 된다 — 다른 팀이 이 문서와 도구만으로 새로운 기업을 판단할 수 있어야 완성으로 본다.

## 판단 일관성 원칙 (재현성의 운영 규칙)

오케스트레이션(`investment-desk`)의 산출물은 각 스킬 결과를 단순히 이어붙인 것이 아니라, **이 문서를 얼마나 충실히 따랐는가**로 검증된 결과여야 한다. 같은 기업을 같은 시점에 다른 사람이 판단해도 같은 결론이 나오려면 아래를 지킨다.

1. **임의 기준 추가·변형 금지**: 각 판단 스킬은 이 문서에 명시된 정의·대체지표·판단 기준(임계값)만 사용한다. 스킬이나 에이전트가 이 문서에 없는 새로운 기준, 가중치, 예외를 자체적으로 만들어내면 안 된다 — 그런 경우는 판단 규칙서를 먼저 개정하고, 그 개정판을 스킬에 반영하는 순서를 따른다.
2. **애매한 경우의 처리도 규칙화**: 데이터가 경계값에 걸치거나 불충분할 때 임의로 재량 판단하지 않는다. 각 스킬의 "데이터 부족 시 처리" 절차(판단 보류·부분부합으로 낮춤 등)를 그대로 따른다.
3. **근거 추적성(Traceability)**: 최종 보고서의 모든 판단 문장은 이 문서의 어느 조항(기준①/②/③, 스크리닝 항목명)과 어느 임계값에 근거했는지 괄호로 명시한다. 예: "매출총이익률 2개년 연속 유지 + 매출액 YoY +5.2% → **부합** (기준① 판단 기준: 매출총이익률 유지 AND 매출액 YoY (+))".
4. **오케스트레이터의 자기검증(Compliance Self-Check)**: `investment-desk` 에이전트는 보고서 초안을 쓴 뒤, 각 판단이 (a) 이 문서의 실제 조항에 근거하는지, (b) 그 조항의 임계값을 정확히 적용했는지 스스로 재확인한다. 규칙서에 근거가 없는 서술(단순 정보 나열, 규칙서 밖 주관적 평가)은 삭제하거나 규칙서 조항에 맞게 다시 쓴다. 규칙서와 상충하는 결론이 나오면 규칙서를 따르는 쪽으로 고친다 — 데이터가 규칙서 기준을 만족스럽게 판단하기에 부족하면 "판단 보류"로 명시하고 임의로 결론을 내지 않는다.
