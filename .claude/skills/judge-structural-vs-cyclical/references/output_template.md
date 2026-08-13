# Output Template — Investment Memo Skeleton

모든 회사에 대해 이 스켈레톤을 정확히 채운다(Framework Fit이 Low면 예외 — 그 경우 전체 메모
대신 짧은 설명을 준다). .md와 .html 산출물 모두 같은 구조를 쓴다 — .html은 표/스코어카드/배지를
시각적으로 렌더링한다는 점만 다르다.

```markdown
# [Company Name] — Structural vs. Cyclical Misclassification Investment Memo

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
(한 문장)

---

## 1. Why This Company Fits / Does Not Fit the Philosophy
(구조 대 순환 논쟁이 있는 회사인지 설명)

---

## 2. Core Thesis Test
> "[회사]의 최근 [성장/둔화] 궤적은 경기 순환이나 일시적 유행이 아니라 구조적 전환이며, 시장은
> 순환적 Multiple/할인율을 적용해 이를 오평가하고 있다."

Verdict: Supported / Partially Supported / Not Supported
핵심 근거 3개:
핵심 반대 근거 3개:

---

## 3. Structural Signal Evidence (Layer A)
(침투율, 세대별 채택, 구조 변화 동인의 영구성 분석 — `layers_a_to_g.md` Layer A)

---

## 4. Cyclical Contamination & Market Framing Test
Historical Macro Sensitivity / Peer Divergence / Growth Decomposition
(`cyclical_contamination_test.md`) + Sell-side 섹터 분류, Multiple-Fundamental Cycle Mismatch

---

## 5. Financial Transmission
| 단계 | 상태 | 핵심 근거 |
|---|---|---|
| Penetration/Adoption | | |
| Category Volume | | |
| Company Revenue (Volume-driven) | | |
| Peer Divergence | | |
| Sell-side 재분류 | | |
| Multiple Re-rating | | |

---

## 6. Layer A–G Analysis
| Layer | 핵심 판단 | 주요 수치 | Bull/Bear |
|---|---|---|---|
| A. Structural Demand | | | |
| B. Product/Brand | | | |
| C. Customer Economics | | | |
| D. Competitive Advantage | | | |
| E. Distribution | | | |
| F. Financial Translation | | | |
| G. Variant Perception | | | |

---

## 7. Variant Perception
### Market Believes
### We Believe
### Why Market May Be Wrong
### Evidence
### Variant Classification
(1–6, `variant_perception.md` 참조)

---

## 8. Catalyst Map
| Catalyst | Leading Indicator | 예상 시점 | Earnings Impact |
|---|---|---|---|

---

## 9. Valuation
현재 Multiple / 역사적 Range / Peers / 현재 가격에 내재된 기대 / Bull-Base-Bear

---

## 10. Expected Return
| Scenario | 구조/순환 판정 | Multiple 반응 | Expected Return |
|---|---|---|---|
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
| A. Structural Demand | | 18 | |
| B. Product/Brand | | 10 | |
| C. Customer Economics | | 12 | |
| D. Competitive Advantage | | 10 | |
| E. Distribution | | 8 | |
| F. Financial Translation | | 12 | |
| G. Variant Perception | | 18 | |
| H. Catalyst | | 6 | |
| I. Valuation | | 6 | |
| Risk (감점) | | -15 | |
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

- Section 0의 Final Verdict는 상단에 스탬프 형태 배지로 렌더링한다(BUY=bull색, WATCH=neutral/
  gold, PASS=gray/ink-soft, SELL=red).
- Section 5, 6, 8, 10, 13은 실제 `<table>` 요소로 렌더링한다(plain text 나열 금지).
- CSS/레이아웃 스캐폴드는 `assets/memo_template.html`을 쓴다.
