# Output Template — Investment Memo Skeleton

Fill in this exact skeleton for every company (unless Framework Fit is Low, in which case give a
short explanation instead of forcing the full memo). Use this same structure for both the .md and
.html deliverable — the .html version renders the tables/scorecard/badges visually instead of as
plain markdown.

```markdown
# [Company Name] — Retention-to-Pricing-Power Investment Memo

## 0. Investment Snapshot

Ticker:
Current Price:
Market Cap:
Industry:
Framework Fit: High / Medium / Low

**Final Verdict: BUY / WATCH / PASS / SELL**
**Entry Timing: BUY NOW / BUY ON CONFIRMATION / BUY ON WEAKNESS / WAIT**
Score: XX / 100
Expected Holding Period:

### One-line Investment View
(one sentence)

---

## 1. Why This Company Fits / Does Not Fit the Philosophy
(retention-based business explanation)

---

## 2. Core Thesis Test
> "이 기업은 이미 Pricing Power를 보유하고 있으나 시장은 이를 충분히 반영하지 않는다."

Verdict: Supported / Partially Supported / Not Supported
핵심 근거 3개:
핵심 반대 근거 3개:

---

## 3. Retention Quality
(cohort / retention / churn / repeat purchase analysis)

---

## 4. Pricing Power Evidence
가격 인상 / 가격 인상 후 Churn / ASP / ARPU / Premium Mix / Peer Premium

---

## 5. Financial Transmission
| 단계 | 상태 | 핵심 근거 |
|---|---|---|
| Retention | | |
| Churn | | |
| Frequency | | |
| LTV/CAC | | |
| Pricing/Mix | | |
| Gross Margin | | |
| Contribution Margin | | |
| Operating Leverage | | |
| EPS/FCF Revision | | |

---

## 6. Layer A–G Analysis
| Layer | 핵심 판단 | 주요 수치 | Bull/Bear |
|---|---|---|---|
| A. Demand | | | |
| B. Product/Brand | | | |
| C. Customer Economics | | | |
| D. Competitive Advantage | | | |
| E. Distribution | | | |
| F. Financial Translation | | | |
| G. Expectations | | | |

---

## 7. Variant Perception
### Market Believes
### We Believe
### Why Market May Be Wrong
### Evidence
### Variant Classification
(1–6, see references/variant_perception.md)

---

## 8. Catalyst Map
| Catalyst | Leading Indicator | 예상 시점 | Earnings Impact |
|---|---|---|---|

---

## 9. Valuation
현재 Multiple / 역사적 Range / Peers / 현재 가격에 내재된 기대 / Bull-Base-Bear

---

## 10. Expected Return
| Scenario | Earnings Growth | Multiple | Expected Return |
|---|---:|---:|---:|
| Bull | | | |
| Base | | | |
| Bear | | | |

---

## 11. Entry Strategy
**Decision: BUY NOW / BUY ON CONFIRMATION / BUY ON WEAKNESS / WAIT**
구체적 진입 조건:
1.
2.
3.

---

## 12. Thesis Break
### Confirmation Signal
### Weakening Signal
### Break Signal
### Sell Trigger

---

## 13. Scorecard
| 항목 | 점수 | 최대 | 핵심 근거 |
|---|---:|---:|---|
| A | | 10 | |
| B | | 12 | |
| C | | 18 | |
| D | | 12 | |
| E | | 6 | |
| F | | 15 | |
| G | | 15 | |
| H | | 7 | |
| I | | 10 | |
| Risk | | -15 | |
| **Total** | | **100** | |

---

## 14. Final Investment Decision
1. **Why this company?**
2. **Why is the market wrong?**
3. **Why now?**
4. **What makes money?**
5. **What proves us wrong?**

> **VERDICT:**
> **ENTRY:**
> **EXPECTED HOLDING PERIOD:**
> **PRIMARY CATALYST:**
> **THESIS BREAK:**
```

## Notes for the HTML version

- Section 0's Final Verdict should render as a colored badge (green=BUY, amber=WATCH, gray=PASS,
  red=SELL) near the top.
- Sections 5, 6, 8, 10, 13 must render as real `<table>` elements, not preformatted text.
- Use `assets/memo_template.html` for the CSS/layout scaffold; drop the filled sections into it.
