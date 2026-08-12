# Output Template — Investment Memo Skeleton

이 스켈레톤을 모든 기업에 그대로 채운다(Framework Fit이 Low면 예외 — 전체 메모 대신 짧은 설명만
쓴다). `.md`와 `.html` 산출물 모두 같은 구조를 쓴다 — `.html`은 표·Scorecard·배지를 시각적으로
렌더링한다.

```markdown
# [Company Name] — Underpriced Customer Love (ULRS) Investment Memo

## 0. Investment Snapshot

Ticker:
Current Price:
Market Cap:
Industry:
Framework Fit: High / Medium / Low

**Final Verdict: BUY / WATCH / AVOID**
**Entry Timing: BUY NOW / BUY ON CONFIRMATION / BUY ON WEAKNESS / WAIT**
ULRS:
Score: XX / 100
Expected Holding Period:

### One-line Investment View
(한 문장)

---

## 1. Why This Company Fits / Does Not Fit the Philosophy
(Sector Fit Matrix 근거 포함)

---

## 2. Core Thesis Test
> "이 기업은 진짜 애착(Love×Durability)을 갖고 있고, 그것을 재무 성과로 전환할 능력도 있으나,
> 시장은 아직 이를 가격에 반영하지 않았다."

Verdict: Supported / Partially Supported / Not Supported
핵심 근거 3개:
핵심 반대 근거 3개:

---

## 3. Love & Durability Evidence (Layer 1~2)
(재구매율/리뷰/DAU 등 Behavioral·Expressed·Engagement·WTP + Durability 시험대)

---

## 4. Gap Evidence (Layer 3~5)
Operating Monetization Gap / Financial Conversion Capacity / Market Recognition Gap
(`references/underpricing_gap_test.md`의 Gap 5종 표 포함)

---

## 5. Financial Transmission
| 단계 | 상태 | 핵심 근거 |
|---|---|---|
| Customer Love | | |
| Durability | | |
| Operating Monetization Gap | | |
| Financial Conversion Capacity | | |
| Market Recognition Gap | | |
| Re-rating | | |

---

## 6. Layer 1–5 Analysis
| Layer | 핵심 판단 | 주요 수치 | Bull/Bear |
|---|---|---|---|
| 1. Customer Love | | | |
| 2. Love Durability & Defensibility | | | |
| 3. Operating Monetization Gap | | | |
| 4. Financial Conversion Capacity | | | |
| 5. Market Recognition Gap | | | |

---

## 7. Variant Perception (Market Recognition Gap)
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
현재 Multiple / 역사적 Range / Peers / 현재 가격에 내재된 기대

---

## 10. Expected Return
| Scenario | Financial Conversion 개선 가정 | Multiple 가정 | Expected Return |
|---|---|---|---:|
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

## 12. Thesis Break / Exit
### Confirmation Signal
### Weakening Signal
### Break Signal
### Sell Trigger
### Exit 유형 (Successful / Thesis-break / Time-stop)

---

## 13. Scorecard
| Layer | 점수 | 최대 | 핵심 근거 |
|---|---:|---:|---|
| 1. Customer Love | | 15 | |
| 2. Love Durability & Defensibility | | 15 | |
| 3. Operating Monetization Gap | | 20 | |
| 4. Financial Conversion Capacity | | 20 | |
| 5. Market Recognition Gap | | 15 | |
| 6. Catalyst 근접성 | | 10 | |
| Risk Penalty | | -0~15 | |
| **Total** | | **100** | |

**ULRS = √(Love%ile × Durability%ile) × Conversion_Readiness_Gap × (1 − Risk_Penalty%) = ?**

---

## 14. Final Investment Decision
1. **Why this company?**
2. **Why is the market wrong (or no longer wrong)?**
3. **Why now?**
4. **What makes money?**
5. **What proves us wrong?**

> **VERDICT:**
> **ULRS:**
> **ENTRY:**
> **EXPECTED HOLDING PERIOD:**
> **PRIMARY CATALYST:**
> **THESIS BREAK:**
```

## Notes for the HTML version

- Section 0의 Final Verdict는 색상 배지로 렌더링(초록=BUY, 호박색=WATCH, 빨강=AVOID) 상단에 배치.
- Section 5, 6, 8, 10, 13은 실제 `<table>`로 렌더링(서식 없는 텍스트 금지).
- `assets/memo_template.html`을 CSS/레이아웃 뼈대로 쓰고, 채운 섹션을 그 안에 넣는다.
