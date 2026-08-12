---
name: retention-pricing-power-memo
description: Generates a B2C stock investment decision memo (styled HTML, ledger/stamp aesthetic — same visual system as the team's structural-cyclical-misclassification-memo skill) by applying the "Retention-to-Pricing-Power" investment philosophy — the thesis that a company can raise prices (or shift toward higher-margin mix) without losing volume/retention, and the market hasn't fully priced in that margin durability. Use this skill whenever the user asks to analyze a company through this specific philosophy, asks "이 회사 가격결정력 있는지 봐줘", "P 올려도 Q 유지되는지 심화 분석해줘", asks for a thesis tree / scorecard / investment memo under this framework, or wants output matching the team's reference memo format for this philosophy. Also trigger when `judge-retention-pricing-power` (the quantitative screening skill in this repo) has already returned 부합/부분부합 for a company and the user wants that judgment expanded into a full memo — this skill is the qualitative deep-dive layer on top of that quantitative gate, not a replacement for it.
---

# Retention-to-Pricing-Power — Investment Memo Skill

이 스킬은 "가격을 올려도(또는 고마진 믹스로 전환해도) 판매량·고객 유지율이 훼손되지 않는다"는
투자 철학을 특정 회사에 적용해, 팀 표준 포맷의 HTML 투자메모를 생성한다.

같은 상위 시스템 안에 다른 철학을 쓰는 팀원의 스킬(`structural-cyclical-misclassification-memo`)이
있다 — 산출물의 **구조와 시각적 문법**은 통일하되(같은 Layer A–I 스코어카드, 같은 Gate 4종, 같은
14개 섹션 구성) **분석 내용/Layer 가중치/색상**은 이 철학 고유의 것을 쓴다.

또한 이 저장소에는 같은 기준을 정량으로 먼저 필터링하는 `judge-retention-pricing-power` 스킬이
`judgment-rules.md` 기준으로 이미 존재한다. 이 메모 스킬은 그 정량 게이트를 **대체하지 않는다** —
정량 판정이 부합/부분부합인 기업에 대해서만 이 스킬로 심화 분석하며, 정량 판정과 정성 결론이
모순되면 안 된다(모순 시 정량 판정이 우선한다).

## 언제 이 스킬을 쓰는가

- 사용자가 회사를 주고 "이 철학(가격결정력)으로 심화 분석해달라"고 할 때
- `judge-retention-pricing-power`가 부합/부분부합을 낸 기업에 대해 더 깊은 메모를 원할 때
- 이미 만든 메모를 다른 회사/최신 데이터로 다시 돌려달라고 할 때

## 필요한 것 (없으면 사용자에게 물어볼 것)

1. **대상 회사** — 없으면 반드시 먼저 확인. 임의로 고르지 말 것.
2. **정량 게이트 결과** — 가능하면 먼저 `judge-retention-pricing-power` 또는 `reports/`의 기존
   투심보고서를 확인해 1단계 판정(부합/부분부합/미부합)을 근거로 삼는다. 미부합이면 아래
   "셋 다 부합하지 않을 때" 절차를 따르고 이 스킬의 나머지 워크플로는 실행하지 않는다.
3. **데이터 접근성** — 웹 검색 도구·`data/cache/<기업명>/`의 DART 캐시가 있는지 확인. 있으면
   최신 실적·마진·상품믹스 데이터를 직접 조사해서 쓴다. 없으면(또는 확인 못한 항목이 있으면)
   절대 숫자를 지어내지 말고 아래 "Data Integrity 원칙"을 따른다.

## 워크플로

### 1단계 — 회사 리서치

`references/thesis-tree.md`의 Layer 1–4, Factor 단위로 빠짐없이 채운다 (DART 재무제표 + web
search, 없으면 명시적 Estimate/Insufficient Data 태그):

- 매출총이익률 다년 추이, 매출원가율과의 디커플링 여부 (Layer 1-1)
- 고마진 상품(PB 등) 비중과 그 성장률, 마진 격차 — **가격 인상 vs 믹스 전환 반드시 분해** (Layer 1-2)
- 매출액 YoY, 객수/객단가 분해(가능한 경우) — 판매량 훼손 여부 (Layer 1-3)
- Peer도 동반 개선 중인지(카테고리 효과 vs 자사 고유) (Layer 2-1)
- 회사가 가격을 결정할 수 없는 저마진/규제 카테고리의 매출 비중 (Layer 2-2)
- 최근 실적에 섞인 일시적 요인(날씨, 관광객, 원자재 등) (Layer 2-3)
- 컨센서스 마진 가정, 현재 Multiple (Layer 3 — 데이터 없으면 Insufficient)

**세부 Layer/Factor/Metric 정의는 `references/thesis-tree.md`를 반드시 참조할 것.** 매번 새 회사를
분석할 때 다시 읽어서 Factor 단위로 빠짐없이 체크한다.

### 2단계 — Core Thesis 작성

`references/thesis-tree.md`의 Core Thesis 템플릿을 이 회사에 맞게 구체적으로 다시 쓴다. 특히
"가격 인상"과 "믹스 전환"을 뭉뚱그리지 말고 그 회사에서 실제로 어느 쪽이 진짜 동인인지 문장에
명시한다.

### 3단계 — Layer A–I 채점 (재가중 적용)

`references/thesis-tree.md`의 재가중 테이블(A=8, B=14, C=22, D=14, E=6, F=16, G=12, H=4, I=4,
Risk 최대 -15)을 사용한다. 팀원의 다른 철학 스킬과 가중치가 다른 것은 의도된 것이니 임의로
통일하지 말 것.

채점 시 반드시:
- Layer 2(Confound & Reversibility Test)를 절대 생략하지 않는다 — "믹스 착시" 여부를 진짜로
  검증한다
- 데이터가 불확실한 항목은 낙관적으로 채점하지 않는다 (Data Integrity Gate)
- 정량 게이트(`judge-retention-pricing-power`)의 판정 근거 수치를 그대로 인용하고, 그 위에
  질적으로 확장한다 — 수치를 다시 지어내지 않는다

### 4단계 — Gate Condition 점검

원본 설계 문서(Chapter 9)의 4개 Gate를 그대로 적용한다:
1. Valuation Gate — 이미 Bull Case가 주가에 반영 중이면 점수 무관 PASS
2. Consensus Gate — "매출총이익률이 유지됐다"는 사실 자체는 이미 재무제표에 공개돼 시장이
   인지하고 있을 가능성이 높다. 진짜 Variant View는 "왜 유지됐는가(믹스 전환의 지속가능성 등)"에
   있어야 한다 — 표면적 사실 재진술이면 이 Gate에서 0점 처리
3. Financial Translation Gate — Layer C·B가 높아도 Layer F(마진의 실제 재무 전환, 일시적 요인
   배제 후 core margin)가 불확실하면 60점 상한 캡
4. Data Integrity Gate — 재구매율·컨센서스 등 핵심 데이터 비공개/추정 불가 시 보수적 최저점,
   임의 긍정 가정 금지

### 5단계 — 최종 판단 매핑

BUY(80점 이상) / WATCH(65~79점) / PASS(50~64점) / SELL·PASS(50점 미만 또는 Gate 위반). 보유 중
Thesis Break Signal 확정 시 점수 무관 SELL.

### 6단계 — HTML 메모 생성

`assets/example-memo-onon.html`(구조적/순환적 오분류 철학 스킬의 참조본)과 같은 시각 문법을
재사용한다 (ledger/paper 색상 변수, 원장 느낌 타이포그래피, stamp 형태의 verdict 블록, 14개
섹션 구성). **색상 변수(`--ledger`, `--ledger-2`, `--stamp`)는 다른 철학 스킬과 시각적으로
구분되도록 다른 계열(예: 브라운/러스트 계열 — 상품·마진·상거래를 연상시키는 톤)을 쓴다.**
완전히 동일한 파일을 복붙하지 말고 회사별 내용에 맞게 다시 쓴다.

섹션 구성 (참조본과 동일 순서, 제목만 이 철학에 맞게 조정):
1. Why This Company Fits the Philosophy
2. Core Thesis Test (근거/반대근거 2단 비교)
3. Layer 1 — Pricing Power Signal Identification
4. Layer 2/3 — Confound & Reversibility Test / Market Recognition
5. Financial Transmission
6. Layer A–I Analysis (재가중 명시)
7. Variant Perception (Market Believes / We Believe / Why Wrong / Evidence Needed 4카드 + Classification 배지)
8. Catalyst Map
9. Valuation
10. Expected Return (Bull/Base/Bear)
11. Entry Strategy
12. Thesis Break (Confirmation/Weakening/Break/Sell Trigger)
13. Scorecard (재가중 반영된 표)
14. Final Investment Decision (5개 Q&A + verdict box)

상단에는 항상 데이터 신뢰도 캐비어트 박스를 넣는다 — 실제 검증된(DART/web) 항목과
Estimate/Insufficient Data로 남은 항목을 구분해서 사용자가 어디를 재검증해야 하는지 알 수
있게 한다. `judge-retention-pricing-power`의 정량 판정 결과(부합/부분부합 + 근거)도 이 박스나
1절에 반드시 인용한다.

### 7단계 — 파일 저장 및 전달

이 저장소에서는 `reports/<기업명>-retention-pricing-power-memo-<yyyymmdd>.html`로 저장한다
(claude.ai 샌드박스 경로가 아니라 이 레포의 `reports/` 컨벤션을 따른다). 대화창에는 이 회사에
특화된 핵심 설계 판단(가중치를 왜 이렇게 줬는지, Gate가 왜 발동/미발동했는지, 결론이 왜 그
등급으로 나왔는지)을 2~4줄로 짧게 설명한다 — 메모 전체를 다시 요약하지 않는다.

## 셋 다 부합하지 않을 때

`judgment-rules.md`의 1단계 핵심 기준 3개(Retention-to-Pricing-Power, Structural vs Cyclical,
Underpriced Customer Love)가 모두 미부합이거나 판단할 근거 데이터 자체가 없다면, 이 스킬로
심화 메모를 억지로 만들지 않는다. 대신 `references/thesis-tree.md`의 "셋 다 부합하지 않을 때"
절차대로, 세 기준 각각에 대해 왜 해당하지 않는지(또는 왜 판단 불가인지)를 근거 수치와 함께
구체적으로 설명하는 짧은 메모만 남긴다 — 억지 Bull 서사를 만들지 않는 것이 Data Integrity
원칙의 핵심이다.

## Data Integrity 원칙 (모든 단계에 공통 적용)

- 데이터가 없거나 불확실하면 반드시 `Estimate` / `Insufficient Data` 태그를 달고, 그 항목은
  보수적으로(낙관적으로 채우지 않고) 채점한다.
- 구체적인 숫자(마진율, 비중, Multiple)를 검증 없이 확신하는 어조로 쓰지 않는다. "~로 알려짐",
  "검증 필요"처럼 불확실성을 남긴다.
- 이 메모는 투자 조언이 아니라 프레임워크 적용 예시이며, 실제 판단 전 원문 공시·최신 실적으로
  재검증이 필요하다는 점을 항상 메모 안에 명시한다.
