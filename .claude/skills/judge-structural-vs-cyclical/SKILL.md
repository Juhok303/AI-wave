---
name: judge-structural-vs-cyclical
description: Generates a B2C stock investment decision memo (styled HTML, ledger/stamp aesthetic) by applying the "Structural vs. Cyclical Misclassification" investment philosophy — the thesis that the market mistakes a durable structural consumer-behavior shift for a temporary cyclical/fad swing and misprices the multiple as a result. Use this skill whenever the user asks to analyze a company (any ticker) through this specific philosophy, asks "이 회사가 구조적 성장인지 순환적인지 봐줘", "내 investment philosophy로 분석해줘" (when that philosophy is this one), asks for a thesis tree / scorecard / investment memo under this framework, or wants output matching the reference memo format even without naming the philosophy explicitly (e.g. "포트폴리오에 있는 종목들 이 철학으로 하나씩 돌려봐줘"). Also trigger for requests to update, re-run, or extend a memo already produced by this skill for a new ticker or new quarter's data.
---

# Structural vs. Cyclical Misclassification — Investment Memo Skill

이 스킬은 "구조적 변화를 시장이 경기·유행 순환으로 오인해 Multiple을 잘못 매긴다"는
투자 철학을 특정 회사에 적용해, 팀 표준 포맷의 HTML 투자메모를 생성한다.

같은 상위 시스템 안에 다른 철학을 쓰는 팀원의 스킬(예: Retention-to-Pricing-Power)이
있을 수 있다 — 산출물의 **구조와 시각적 문법**은 통일하되 **분석 내용/Layer 가중치**는
이 철학 고유의 것을 쓴다.

## 언제 이 스킬을 쓰는가

- 사용자가 회사/티커를 주고 "이 철학으로 분석해달라"고 할 때
- 사용자가 "구조적이냐 순환적이냐" 논쟁이 있는 종목을 분석해달라고 할 때
- 이미 만든 메모를 다른 회사/최신 데이터로 다시 돌려달라고 할 때

## 필요한 것 (없으면 사용자에게 물어볼 것)

1. **대상 회사/티커** — 없으면 반드시 먼저 확인. 임의로 고르지 말 것.
2. **데이터 접근성** — 웹 검색 도구가 있는지 확인. 있으면 최신 실적/주가/Multiple을
   직접 조사해서 쓴다. 없으면(또는 검색해도 확인 못한 항목이 있으면) 절대 숫자를
   지어내지 말고 아래 "Data Integrity 원칙"을 따른다.

## 워크플로

### 1단계 — 회사 리서치

다음 항목을 최대한 채운다 (가능하면 web search, 없으면 학습 지식 + 명시적 Estimate 태그):

- 카테고리 침투율/참여 지표 (Layer 1)
- 세대별/코호트별 채택 데이터 (Layer 1)
- 구조 변화 동인의 성격 — 기술적/영구적인가 vs 유행성인가 (Layer 1)
- 과거 경기 하방기 실적 동행 여부 (Layer 2) — 상장 이력이 짧으면 "Insufficient Data"
- Peer/카테고리 전체와의 실적 divergence (Layer 2)
- 최근 성장/둔화의 Volume vs Price/Cost 분해, 특히 관세·규제·원자재 등
  정책적/일시적 요인이 섞여 있는지 (Layer 2)
- 셀사이드가 이 회사를 어떤 섹터/Multiple 밴드로 다루는지, 그 논쟁이 이미
  얼마나 공개적으로 논의되고 있는지 (Layer 3 — Consensus Gate 판단 근거)
- 현재 Multiple, 역사적 Range, Peer Multiple (Valuation)
- 최근 실적발표/IR 자료의 Bull/Bear 증거

**세부 Layer/Factor/Metric 정의는 `references/thesis-tree.md`를 반드시 참조할 것.**
이 문서는 SKILL.md 요약만 보고 건너뛰지 말고, 매번 새 회사를 분석할 때 다시 읽어서
Factor 단위로 빠짐없이 체크한다.

### 2단계 — Core Thesis 작성

`references/thesis-tree.md`의 Core Thesis 템플릿을 이 회사에 맞게 구체적으로 다시 쓴다.
막연히 복붙하지 말 것 — 그 회사의 실제 논쟁 지점(예: 관세, 신제품, 세대교체 등)을
문장에 반영한다.

### 3단계 — Layer A–G 채점 (재가중 적용)

`references/thesis-tree.md`의 재가중 테이블(A=18, B=10, C=12, D=10, E=8, F=12,
G=18, H=6, I=6, Risk 최대 -15)을 사용한다. 팀원의 다른 철학 스킬과 가중치가
다른 것은 의도된 것이니 임의로 통일하지 말 것.

채점 시 반드시:
- Bear case를 Bull case와 동등한 무게로 조사한다 (이 철학은 확증편향 위험이 특히 큼)
- Layer 2(Cyclical Contamination Test)를 절대 생략하지 않는다 — 진짜로 반증을 시도한다
- 데이터가 불확실한 항목은 낙관적으로 채점하지 않는다 (Data Integrity Gate)

### 4단계 — Gate Condition 점검

원본 설계 문서(Chapter 9)의 4개 Gate를 그대로 적용:
1. Valuation Gate — 이미 Bull Case가 주가에 반영 중이면 점수 무관 PASS
2. Consensus Gate — Variant View가 "시장이 이미 아는 좋은 점"뿐이면 해당 View 0점.
   **이 철학은 특히 이 Gate에 취약하다** — "구조냐 순환이냐" 논쟁 자체가 이미
   언론/실적콜에서 공개적으로 다뤄지는 경우가 많기 때문. 반드시 명시적으로 점검할 것.
3. Financial Translation Gate — Layer C·D가 높아도 Layer F가 장기 정체면 60점 상한 캡
4. Data Integrity Gate — 핵심 데이터 비공개/추정 불가 시 보수적 최저점, 임의 긍정 가정 금지

### 5단계 — 최종 판단 매핑

BUY(80점 이상) / WATCH(65~79점) / PASS(50~64점) / SELL·PASS(50점 미만 또는 Gate 위반).
보유 중 Thesis Break Signal 확정 시 점수 무관 SELL.

### 6단계 — HTML 메모 생성

`assets/example-memo-onon.html`을 스타일/구조 참조본으로 삼아 같은 시각 문법을
재사용한다 (ledger/paper 색상 변수, 원장 느낌 타이포그래피, stamp 형태의 verdict
블록, 14개 섹션 구성). 색상 변수(`--ledger`, `--ledger-2`)는 다른 철학 스킬과
구분되도록 슬레이트 계열을 유지하되, 완전히 동일한 파일을 복붙하지 말고 회사별
내용에 맞게 다시 쓴다.

섹션 구성 (참조본과 동일 순서):
1. Why This Company Fits the Philosophy
2. Core Thesis Test (근거/반대근거 2단 비교)
3. Layer 1 — Structural Signal Identification
4. Layer 2/3 — Cyclical Contamination & Market Framing Test
5. Financial Transmission
6. Layer A–G Analysis (재가중 명시)
7. Variant Perception (Market Believes / We Believe / Why Wrong / Evidence Needed
   4카드 + Classification 배지)
8. Catalyst Map
9. Valuation
10. Expected Return (Bull/Base/Bear)
11. Entry Strategy
12. Thesis Break (Confirmation/Weakening/Break/Sell Trigger)
13. Scorecard (재가중 반영된 표)
14. Final Investment Decision (5개 Q&A + verdict box)

상단에는 항상 데이터 신뢰도 캐비어트 박스를 넣는다 — 실시간 검색으로 검증한
항목과 Estimate/Insufficient Data로 남은 항목을 구분해서 사용자가 어디를
재검증해야 하는지 알 수 있게 한다.

### 7단계 — 파일 저장 및 전달

`/mnt/user-data/outputs/`에 `{ticker}-structural-cyclical-memo.html` 형식으로
저장하고 present_files로 전달한다. 대화창에는 이 회사에 특화된 핵심 설계
판단(가중치를 왜 이렇게 줬는지, Gate가 왜 발동/미발동했는지, 결론이 왜 그
등급으로 나왔는지)을 2~4줄로 짧게 설명한다 — 메모 전체를 다시 요약하지 않는다.

## Data Integrity 원칙 (모든 단계에 공통 적용)

- 웹 검색 결과가 없거나 불확실하면 반드시 `Estimate` / `Insufficient Data` 태그를
  달고, 그 항목은 보수적으로(낙관적으로 채우지 않고) 채점한다.
- 구체적인 숫자(주가, 정확한 % 성장률, Multiple)를 검증 없이 확신하는 어조로
  쓰지 않는다. "~로 알려짐", "검증 필요"처럼 불확실성을 남긴다.
- 이 메모는 투자 조언이 아니라 프레임워크 적용 예시이며, 실제 판단 전 원문
  10-K/10-Q/실적발표로 재검증이 필요하다는 점을 항상 메모 안에 명시한다.
