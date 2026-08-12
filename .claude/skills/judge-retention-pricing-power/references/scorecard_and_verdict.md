# Scorecard, Gates, and Final Verdict

## Scorecard (100 points)

| 평가 항목 | 최대 점수 |
|---|---:|
| A. Structural Demand | 10 |
| B. Product / Brand Strength | 12 |
| C. Customer Economics | 18 |
| D. Competitive Advantage | 12 |
| E. Distribution | 6 |
| F. Financial Translation | 15 |
| G. Variant Perception | 15 |
| H. Catalyst | 7 |
| I. Valuation | 10 |

Risk / Thesis Durability is scored separately as a deduction of up to **-15 points**.

Every row must show **score / max + 1–2 line justification**. Never leave a row unjustified.

## Gate Conditions (apply AFTER scoring, can override a high raw score)

- **Valuation Gate** — 현재 가격이 이미 Bull Case를 반영하는 경우 → can block a BUY even with a
  high score (state explicitly that the gate was checked, whether it passed).
- **Consensus Gate** — Variant View가 시장이 이미 알고 있는 내용에 불과한 경우 (category 1 in
  `variant_perception.md`) → Variant Perception score forced to 0.
- **Financial Translation Gate** — Customer Economics와 Competitive Advantage가 좋아도 Financial
  Translation이 장기간 나타나지 않는 경우 → cap the overall score (don't let strong upstream layers
  alone justify BUY).
- **Data Integrity Gate** — Retention/Cohort/Churn 등 핵심 데이터가 공개되지 않고 합리적 추정도
  불가능하다면, 임의로 긍정적인 가정을 만들지 말 것. Mark "Insufficient Data" and score
  conservatively (do not average toward a middling score — treat missing critical data as a real
  negative for conviction).

State explicitly, for each gate, whether it was triggered and how it affected the score/verdict.

## Final Verdict Thresholds

- **BUY** — Score ≥ 80 AND all gates passed AND a clear Variant Perception exists AND a Valuation Gap
  exists AND a Catalyst exists within 6–12 months.
- **WATCH** — Score 65–79. Thesis valid but Catalyst / Valuation / data confirmation still needed.
- **PASS** — Score 50–64, OR any gate is violated (even with a high raw score).
- **SELL** — For an existing holding, when a Thesis Break Signal (per `catalyst_and_entry.md`) has
  been confirmed.

A BUY score with a failed gate must resolve to PASS, not BUY — the gates are hard constraints, not
soft adjustments.
