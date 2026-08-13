---
name: judge-retention-pricing-power
description: >
  Use this skill whenever the user gives a company name or ticker and wants an investment view, a
  buy/watch/pass/sell call, an Investment Memo, or any deep-dive equity analysis — even if they
  don't mention "retention" or "pricing power" explicitly. Also trigger on phrases like "이 기업
  어때", "지금 사도 될까", "투자 관점에서 분석해줘", "Investment Memo 만들어줘", or any request to
  evaluate a B2C, subscription, membership, consumer-brand, or repeat-purchase company for
  investment purposes. This skill applies ONE FIXED investment philosophy — high retention
  converts into pricing power, and the market underestimates the speed and size of that conversion
  — as the mandatory analytical lens. Do NOT invent a different framework (DCF-only, generic SWOT,
  simple bull/bear list, etc.) when this skill is applicable. The skill ends by producing two
  deliverable files, a Markdown Investment Memo and a styled HTML Investment Memo.
---

# Retention-to-Pricing-Power Investment Decision Skill

## What this skill is

This is not a general equity-research assistant. It is a **fixed decision architecture** that always asks
the same question about every company:

> "이 기업의 높은 Retention이 아직 시장이 충분히 가격에 반영하지 않은 Pricing Power로 전환되고 있는가?"
> ("Is this company's high retention converting into pricing power that the market has not yet
> priced in?")

Never substitute a different investment philosophy. Never skip steps because a company "obviously"
passes or fails. Always run the full causal chain below, and always look for where the chain breaks.

**Core belief driving every analysis:**

> Retention → Churn 하락/반복구매 → 가격 인상 수용능력 → ASP/Mix 상승 → Gross Margin 개선 →
> Contribution Margin 개선 → Operating Leverage → EPS/FCF 상향 → Earnings Revision → Multiple Re-rating

**Core Thesis to test on every company (never assume true):**

> "이 기업은 이미 가격결정권을 보유하고 있거나 초기 신호가 나타나고 있으나, 시장은 여전히 이를
> Volume/User Growth 중심의 스토리로 가치평가하고 있다."

Verdict must be one of: **Supported / Partially Supported / Not Supported**.

## Guiding behavioral rules (apply throughout, not just once)

1. **재무제표 우선순위**: 항상 최신 데이터를 검색해서 사용한다 (web search / 회사 IR, 10-K/10-Q,
   earnings call, investor day, 신뢰도 높은 산업 데이터·언론, app/web traffic, 소비자 리뷰 순).
   숫자는 항상 **값 + 기간 + 출처**로 표기한다. 데이터가 없으면 만들지 말고 "Insufficient Data"라고 쓴다.
   Fact / Estimate / Inference를 명확히 구분한다.
2. **반증 우선 원칙**: 분석을 시작하기 전에 "이 기업이 이 투자철학에 맞지 않는다는 가장 강한 증거는
   무엇인가?"를 먼저 묻고, 최소 3개의 반대 근거를 적극적으로 찾은 뒤에 Thesis를 평가한다. PASS로
   끝나는 것도 정상적인 결과다. Bull case를 만들기 위해 이 스킬이 존재하는 게 아니다.
3. **인과 전달 확인**: 각 Layer를 독립 체크리스트로 채점하지 말고, 앞 Layer의 결과가 실제로 뒤
   Layer로 전달되는지 확인한다. 연결이 끊어지는 지점을 반드시 찾아 명시한다.
4. **추상적 표현 금지**: "브랜드가 강하다", "고객이 만족한다" 같은 표현은 금지. 항상 관찰 가능한
   데이터(리뷰 평점, NPS, repeat purchase rate, ASP 등)로 뒷받침한다.
5. **Variant Perception 자기검증**: 시장이 이미 알고 있는 좋은 점을 Variant View로 인정하지 않는다.
   "정말 시장이 모르는가?"를 항상 먼저 검증한다.

## Workflow (run in this order)

1. **Universe Filter** — read `references/layers_a_to_g.md` §Universe Filter first. Output
   `Framework Fit: High / Medium / Low`. If Low, explain why and stop the deep analysis (still produce
   a short memo stating the mismatch — don't force a full workflow onto a bad-fit company).
2. **Data gathering** — before writing any layer, search for the company's latest retention/cohort
   data, pricing history, ASP/ARPU, margins, and consensus estimates. Use web search liberally; this
   skill is only as good as the data behind it. Cite value + period + source for every number.
   이 레포(Claude Code) 안에서 실행할 때는 `data/cache/<기업명>/*.json`(fetch-dart/fetch-fnguide/
   fetch-fred/fetch-web이 이미 수집한 원자료)이 있으면 먼저 재사용하고, 거기 없는 retention/가격/
   ASP 등 이 철학 고유 지표만 웹 검색으로 보완한다.
3. **Layers A → G** — follow `references/layers_a_to_g.md` in order (Demand → Product/Brand →
   Customer Economics → Competitive Advantage → Distribution → Financial Translation →
   Variant Perception). Run the **Pricing Power Test** (4 sub-tests) inside Layer C/D per
   `references/pricing_power_test.md`.
4. **Financial Transmission Chain** — mark each link Confirmed / Emerging / Broken / Insufficient
   Data per `references/financial_transmission.md`, and state how far the chain has progressed.
5. **Variant Perception** — build Market Believes / We Believe / Why Market May Be Wrong / Evidence /
   Recognition Trigger, then classify into the 6-category self-check per
   `references/variant_perception.md`. Category 1 never counts as a variant view.
6. **Catalyst Map, Entry Timing, Valuation, Expected Return, Holding Period, Thesis Break** — follow
   `references/catalyst_and_entry.md`.
7. **Scorecard, Gates, Final Verdict** — follow `references/scorecard_and_verdict.md` exactly. Do not
   award points a gate has blocked. Show score/max + 1-2 line justification for every row.
8. **Write the memo** — follow the exact structure in `references/output_template.md` (this mirrors
   the required section 27 format: Snapshot → Thesis Test → Retention Quality → Pricing Power Evidence
   → Financial Transmission table → Layer A-G table → Variant Perception → Catalyst Map → Valuation →
   Expected Return → Entry Strategy → Thesis Break → Scorecard → Final Investment Decision).
9. **Produce deliverable files** — see "Final file output" below. This step is mandatory; a
   conversational answer alone is not a complete run of this skill.
10. **(이 레포 파이프라인에서 호출될 때만) 축약 판정 반환** — `investment-desk`가 1단계 필터링용으로
    호출한 경우, 위 Final Verdict를 `judgment-rules.md` 기준① 매핑(BUY→부합, WATCH→부분부합,
    PASS 또는 Gate 위반→미부합)으로 환산해 짧게 반환한다. SELL은 신규 판단(1단계 필터링)에는
    등장하지 않는다. 두 출력(전체 메모 vs 파이프라인용 축약 판정)은 같은 계산에서 나와야 한다.

## Final file output (mandatory)

Once the memo content is finalized, always generate BOTH of the following files, with identical
content, using the company's name (spaces replaced with underscores, no special characters):

- `[Company]_Investment_Memo.md` — the memo exactly as structured in `references/output_template.md`.
- `[Company]_Investment_Memo.html` — the same content rendered as a polished, IM-style report:
  the Scorecard, Financial Transmission Chain, Layer A-G table, Catalyst Map, and Valuation/Expected
  Return sections must render as actual styled tables (not plain text), with the Final Verdict
  (BUY/WATCH/PASS/SELL) visually prominent near the top (e.g., a colored badge — green=BUY,
  yellow=WATCH, gray=PASS, red=SELL). Use `assets/memo_template.html` as the base template/CSS;
  do not reinvent styling from scratch each time.

**저장 위치**: 이 레포(Claude Code) 안에서 실행할 때는 Claude.ai 관례(`/home/claude/`,
`/mnt/user-data/outputs/`, `present_files`)를 쓰지 않는다 — 워크드 예시/템플릿은 `assets/`에,
`investment-desk`가 실제 대상 기업으로 실행한 최종 결과는
`reports/<기업명>_Investment_Memo_retention-pricing-power.md`(+`.html`)에 저장한다. 파일을 저장한
뒤에는 저장된 두 경로만 짧게 알려준다 — 긴 후기(post-amble)는 붙이지 않는다.

## Reference files (load as needed)

- `references/layers_a_to_g.md` — Universe Filter + full Layer A-G definitions and required metrics.
- `references/pricing_power_test.md` — the 4 mandatory pricing-power sub-tests.
- `references/financial_transmission.md` — the Retention→Re-rating chain and how to mark each link.
- `references/variant_perception.md` — Market Believes/We Believe structure + 6-way self-check.
- `references/catalyst_and_entry.md` — Catalyst Map, Entry Timing (4 options), Valuation, Expected
  Return, Holding Period, Thesis Break/Sell Discipline.
- `references/scorecard_and_verdict.md` — 100-point scorecard, Gate Conditions, and BUY/WATCH/PASS/SELL
  thresholds.
- `references/output_template.md` — the exact memo skeleton to fill in (matches required output format).
- `assets/memo_template.html` — base HTML/CSS template for the HTML deliverable.
