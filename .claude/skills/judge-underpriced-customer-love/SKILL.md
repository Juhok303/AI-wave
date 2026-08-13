---
name: judge-underpriced-customer-love
description: >
  Use this skill whenever the user gives a company name or ticker and wants an investment view
  through the "Underpriced Customer Love" lens — even if they don't say "ULRS" explicitly. Trigger
  on "이 회사 고객들이 진짜 좋아하는데 아직 저평가된 것 같아", "Underpriced Customer Love로 봐줘",
  "ULRS 계산해줘", "이 브랜드 팬덤이 진짜인지 봐줘", or any request to evaluate a B2C/구독/뷰티/
  컨슈머앱 기업 where consumer affection (리뷰·재구매율·DAU) is the central question. This skill
  applies ONE FIXED philosophy — 진짜 애착(Love×Durability) + 재무 전환 능력(Conversion) + 시장의
  미인식(Gap), 세 조건의 동시 성립 — as the mandatory lens. Do NOT substitute a generic bull/bear or
  DCF-only analysis when this skill is applicable. Ends by producing BOTH a Markdown and a styled
  HTML Investment Memo.
---

# Underpriced Customer Love (ULRS) Investment Decision Skill

## What this skill is

This is a **fixed decision architecture**, not a general equity-research assistant. It always tests
the same three-part claim about a company:

> ① 소비자가 진짜로 이 기업을 사랑하는가(Love), 그 사랑이 유행이 아니라 지속되는가(Durability) —
> ② 그 애착을 재무 성과로 바꿀 능력이 있는가(Conversion) —
> ③ 그런데도 시장(밸류에이션·컨센서스)은 아직 이를 반영하지 않았는가(Gap).

Never substitute a different philosophy. Never skip a Layer because a company "obviously" fits.

**Core belief driving every analysis:**

> Customer Love ↑ → Durability 확인(AND) → Operating Monetization Gap 존재 → Financial Conversion
> Capacity 확인 → Market Recognition Gap 확인 → Re-rating

**Core Thesis to test on every company (never assume true):**

> "이 기업은 진짜 애착(Love×Durability)을 갖고 있고 그것을 재무 성과로 전환할 능력도 있으나, 시장은
> 아직 이를 가격에 반영하지 않았다."

Verdict must be one of: **Supported / Partially Supported / Not Supported** (Core Thesis Test) →
최종적으로 **BUY / WATCH / AVOID** (Final Verdict, `references/scorecard_and_verdict.md`의
Score+Gate 임계값 적용 후 — 기준①②와 동일 아키텍처, 2026-08-13부터 ULRS 부호가 아니라 이 방식이
Verdict를 정한다).

전체 방법론(Layer 정의, Gap 공식, Red Flag, Sector Fit, ULRS 공식 유도)은
`references/underpriced-customer-love-framework.md`에 있다 — 매 분석마다 요약만 보지 말고 다시 읽는다.

## Guiding behavioral rules (apply throughout, not just once)

1. **값+기간+출처 우선**: 웹 검색/공시로 최신 데이터를 확인한다. 숫자는 항상 **값 + 기간 + 출처**로
   표기한다. 데이터가 없으면 절대 만들어내지 말고 "Insufficient Data"라고 쓴다. Fact/Estimate/
   Inference를 명확히 구분한다.
2. **반증 우선 원칙**: Durability(Layer 2)와 Red Flag 10종을 절대 생략하지 않는다 — "사랑받는다"는
   증거만 모으고 "반짝 유행 아닌가"를 확인하지 않으면 이 스킬을 잘못 쓴 것이다. 최소 3개의 반대
   근거를 적극적으로 찾은 뒤 Thesis를 평가한다.
3. **인과 전달 확인**: Financial Transmission의 각 링크를 독립적으로 채점하지 말고, 앞 링크의
   결과가 실제로 뒤 링크로 전달되는지 확인한다. 연결이 끊어지는 지점을 반드시 명시한다.
4. **추상적 표현 금지**: "고객이 좋아한다", "브랜드가 강하다" 같은 표현은 금지. 항상 관찰 가능한
   데이터(재구매율, 리뷰 점수, DAU/MAU, 가격 인상 후 유지율 등)로 뒷받침한다.
5. **Variant Perception 자기검증**: 시장이 이미 알고 있는 좋은 점을 Variant View로 인정하지 않는다.
   "정말 시장이 모르는가?"를 항상 먼저 검증한다(`references/variant_perception.md`).

## AND 구조 / 정규화 원칙 (이 철학 고유)

- Love와 Durability는 반드시 **곱(기하평균)**으로 결합한다 — 산술평균은 "사랑은 있는데 지속성 0"인
  반짝 유행주도 통과시키므로 절대 쓰지 않는다.
- 모든 지표는 raw 값이 아니라 Peer 대비 Percentile Rank로 비교한다(`references/
  underpricing_gap_test.md`).
- Red Flag 2개 이상이면 점수와 무관하게 즉시 AVOID(`references/red_flag_test.md`).

## Workflow (run in this order)

1. **Universe Filter** — `references/underpriced-customer-love-framework.md` J절(Sector Fit
   Matrix)로 판정한다. Output `Framework Fit: High / Medium / Low`. Low면 짧은 설명으로 마무리하고
   전체 14-section 메모를 강제하지 않는다.
2. **데이터 수집** — 재구매율/리뷰/DAU-MAU/가격 인상 이력(Layer 1), Retention Decay·Moat(Layer 2),
   ARPU·마진·CAC(Layer 3), LTV/CAC·영업레버리지·FCF(Layer 4), 컨센서스·EV/Sales(Layer 5)를 웹
   검색·공시로 조사한다. 모든 수치는 값+기간+출처를 남긴다.
3. **Layer 1~5** — `underpriced-customer-love-framework.md` C-1~C-5절로 각 Layer를 채점한다.
   Peer Group은 아래 "Peer Group 축소판" 절차로 근사한다.
4. **Gap 계산** — `references/underpricing_gap_test.md`로 Gap 5종(특히 Conversion-Readiness Gap)을
   계산한다.
5. **Financial Transmission** — `references/financial_transmission.md`로 6개 링크를 Confirmed/
   Emerging/Broken/Insufficient Data로 마킹하고, 체인이 어디까지 진행됐는지 진단한다.
6. **Variant Perception (Market Recognition Gap)** — `references/variant_perception.md`의
   Market Believes/We Believe/Why Wrong/Evidence/Recognition Trigger를 쓰고, 6-category로 분류한다
   (Category 1이면 Variant View 불인정).
7. **Red Flag Gate** — `references/red_flag_test.md` 10종을 전부 점검한다. 2개 이상이면 즉시 AVOID.
8. **ULRS 계산(진단 지표)** — `ULRS = √(Love%ile × Durability%ile) × Conversion_Readiness_Gap ×
   (1 − Risk_Penalty%)`. Verdict를 직접 정하지 않는다 — Market Recognition Gate 판정 근거와 Entry
   Timing/Expected Return 산정에 쓰인다(`references/scorecard_and_verdict.md` 참고).
9. **Catalyst, Entry Timing, Valuation, Expected Return, Holding Period, Exit** —
   `references/entry_timing.md`를 따른다. Entry Timing은 반드시 BUY NOW / BUY ON CONFIRMATION /
   BUY ON WEAKNESS / WAIT 중 하나로 확정한다.
10. **Scorecard, Gates, Final Verdict** — `references/scorecard_and_verdict.md`를 정확히 따른다.
    100점 스코어카드를 채우고 5개 Gate(Market Recognition/Consensus/Durability/Red Flag/Data
    Integrity)를 점검한 뒤, Score+Gate 임계값(BUY ≥80·전 Gate 통과, WATCH 65~79, AVOID 50~64 또는
    Gate 위반)으로 **최종 Verdict**를 정한다 — Gate가 막은 점수는 주지 않는다. 모든 행에 점수/최대
    + 1-2줄 근거를 남긴다.
11. **메모 작성** — `references/output_template.md`의 정확한 스켈레톤을 채운다. `.md`와 `.html`
    모두 같은 구조를 쓴다.
12. **산출물 생성** — 아래 "Final file output" 참조. **필수 단계다** — 대화창 답변만으로는 완료가
    아니다.
13. **(이 레포 파이프라인에서 호출될 때만) 축약 판정 반환** — `investment-desk`가 1단계 필터링용으로
    호출한 경우, `references/scorecard_and_verdict.md`의 매핑(BUY→부합, WATCH→부분부합, AVOID→
    미부합)으로 환산해 짧게 반환한다. 두 출력(전체 메모 vs 파이프라인용 축약 판정)은 같은 계산에서
    나와야 한다.

## Peer Group 축소판 (이 레포는 GICS DB가 없음)

1. 웹 검색 "`<기업명>` 경쟁사 OR 유사 서비스"로 동종업계 상장사 5~10개를 추린다.
2. 그 후보들의 매출액(공시·IR)을 확인해 대상 기업의 0.3~3배 범위에 드는 회사만 채택한다.
3. 5개 미만이면 Percentile 대신 "Peer 대비 상/중/하" 정성 3단계로 대체하고 표본 부족을 근거에 명시한다.
4. Peer Group을 아예 구성 못 하면 절대 기준(`references/red_flag_test.md`의 임계값)만으로 판단하고 Percentile 항목은 판단 보류로 남긴다.

## Reference files (load as needed)

- `references/underpriced-customer-love-framework.md` — Universe Filter(J절) + 전체 Layer 1-5
  정의(C절) + Entry Timing 5-stage 원본(F절) + Catalyst(G절) + Holding/Exit(I절) + Core
  Version(K절) + ULRS 공식 유도(진단 지표로서의 역할).
- `references/scorecard_and_verdict.md` — 100점 스코어카드(재가중), Gate 5종, Final Verdict
  임계값(BUY/WATCH/AVOID) — 기준①②와 동일 아키텍처. **최종 Verdict는 이 문서가 정한다.**
- `references/underpricing_gap_test.md` — 정규화 원칙, Peer Group 3중 필터, Gap 공식 5종.
- `references/red_flag_test.md` — Red Flag 10종 + 강제 AVOID 규칙.
- `references/financial_transmission.md` — Love→Re-rating 6단계 체인, 링크별 마킹 방법.
- `references/variant_perception.md` — Market Recognition Gap 6-category 자기검증(팀 공통 체계).
- `references/entry_timing.md` — Catalyst Map, Entry Timing 4-category(F절 5-stage 재매핑),
  Valuation, Expected Return, Holding Period, Exit Rule.
- `references/output_template.md` — 14-section 메모 스켈레톤.
- `assets/memo_template.html` — HTML 산출물의 CSS/레이아웃 뼈대.
- `assets/example-memo-duolingo.html` — Duolingo(DUOL) 워크드 예시이자 스타일 참조본.

## Final file output (mandatory)

메모 내용이 확정되면 아래 두 파일을 **동일한 내용**으로 항상 생성한다(기업명은 공백 없이):

- `[Company]_ULRS_Investment_Memo.md` — `references/output_template.md` 그대로.
- `[Company]_ULRS_Investment_Memo.html` — 같은 내용을 스타일 렌더링. Scorecard, Financial
  Transmission, Layer 표, Catalyst Map, Expected Return은 실제 `<table>`로 렌더링하고, Final
  Verdict를 상단에 색상 배지로 표시한다(초록=BUY, 호박색=WATCH, 빨강=AVOID). `assets/
  memo_template.html`을 CSS 뼈대로 쓰고, 완전히 동일한 파일을 복붙하지 말고 회사별 내용에 맞게
  다시 쓴다.

**저장 위치**: 이 레포(Claude Code) 안에서 실행할 때는 Claude.ai 관례(`/mnt/user-data/outputs/`,
`present_files`)를 쓰지 않는다 — 워크드 예시/템플릿은 `assets/`에, `investment-desk`가 실제
대상 기업으로 실행한 최종 결과는 `reports/<기업명>_ULRS_Investment_Memo.md`(+`.html`)에 저장한다.
