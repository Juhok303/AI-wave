# Scorecard, Gates, and Final Verdict

기준①(`judge-retention-pricing-power`)·기준②(`judge-structural-vs-cyclical`)와 동일한 Score+Gate
임계값 아키텍처를 쓴다(2026-08-13 개편) — 이전에는 이 100점 스코어카드가 참고 지표일 뿐이고
**ULRS 공식의 부호**가 최종 Verdict를 직접 정했으나, 세 기준의 판정 구조를 통일하기 위해 이 스킬도
Score+Gate 임계값이 Verdict를 정하는 방식으로 바꿨다. ULRS는 폐기하지 않는다 — Gap의 크기를
정량화하는 진단 지표로 남아 Market Recognition Gate 판정과 Entry Timing/Expected Return 산정에
계속 쓰인다.

## Scorecard (100점)

`references/underpriced-customer-love-framework.md` D절의 원 가중치 합이 95였던 것을 100으로
맞췄다(Layer 3을 20→25로 상향 — 원 문서가 이미 "이 Thesis의 핵심"이라고 설명한 항목이라 그
설명과 일치시킴).

| Layer | 가중치 | 배분 논리 |
| --- | ---: | --- |
| 1. Customer Love | 15 | 필요조건이지만 그 자체로는 주가와 직결 안 됨(가장 흔한 착시 원인) |
| 2. Love Durability & Defensibility | 15 | Love가 진짜인지 검증하는 게이트. 낮으면 이후 Layer 전체에 페널티 |
| 3. Operating Monetization Gap | **25** | 이 Thesis의 핵심 — Gap이 클수록 잠재 alpha 큼 |
| 4. Financial Conversion Capacity | 20 | Gap이 실제 재무성과로 "전환될 능력"이 있는지가 성패를 가름 |
| 5. Market Recognition Gap | 15 | 아무리 좋아도 시장이 이미 안다면 alpha 없음(핵심 절제 조건) |
| 6. Catalyst 근접성 | 10 | 전환 시점의 가시성 — Holding Period와 IRR에 직결 |
| **합계** | **100** | |

Risk Penalty는 별도로 최대 **-15점** 감점한다(Red Flag 개수 × 계산은 `red_flag_test.md` 기준).

```
Layer Score = Σ(Metric Peer Percentile × Metric Weight)      [0~100]
Total Score = Σ(Layer Score × Layer Weight%) − Risk Penalty
```

모든 행에 **점수/최대 + 1~2줄 근거**를 남긴다. 근거 없는 행을 남기지 않는다.

## Gate Conditions (채점 이후 적용, 높은 원점수를 override 가능)

- **Market Recognition Gate** (기준①②의 Valuation Gate에 대응) — `Conversion_Readiness_Gap =
  (Layer4 %ile − Layer5 %ile)/100`이 0 이하(전환 능력보다 시장 인식이 이미 같거나 앞섬)면 점수와
  무관하게 BUY를 막는다. Gate를 점검했는지, 통과했는지 명시적으로 서술한다.
- **Consensus Gate** — Variant View가 "시장이 이미 아는 좋은 점"(`variant_perception.md` category
  1)뿐이면 Layer5(Market Recognition Gap) 점수를 0으로 강제한다.
- **Durability Gate** (기준①②의 Financial Translation Gate에 대응) — Layer2(Durability)가 40점
  미만이면 Total Score에 상한 60점을 캡한다 — Love만 높고 지속성이 없는 "반짝 유행"을 상위
  Layer만으로 BUY 정당화하지 못하게 막는다.
- **Red Flag Gate** (이 철학 고유) — `references/red_flag_test.md`의 Red Flag가 2개 이상이면
  점수와 무관하게 즉시 AVOID를 강제한다.
- **Data Integrity Gate** — 재구매율/Retention Decay/컨센서스 등 핵심 데이터가 비공개거나 합리적
  추정이 불가능하면 임의로 긍정적인 가정을 만들지 않는다. "Insufficient Data"로 표기하고
  보수적으로(중간값으로 평균 내지 않고) 채점한다 — 데이터 결여 자체를 확신에 대한 실질적 감점
  요인으로 취급한다.

각 Gate마다 발동 여부와 그것이 점수/Verdict에 어떤 영향을 줬는지 명시적으로 서술한다.

## Final Verdict Thresholds

- **BUY** — Score ≥ 80 AND 모든 Gate 통과 AND 명확한 Variant Perception 존재(Market Recognition
  Gate 통과와 동일 조건) AND 6~12개월 내 Catalyst 존재.
- **WATCH** — Score 65~79. Thesis는 유효하나 Catalyst/전환 확인이 더 필요.
- **AVOID** — Score 50~64, 또는 Gate 하나라도 위반(원점수가 높아도). Red Flag Gate 위반은 항상
  AVOID로 직행한다.

BUY 점수인데 Gate를 위반했다면 반드시 AVOID로 귀결된다 — Gate는 소프트 조정이 아니라 하드 제약이다.

## ULRS의 새 역할 — 진단 지표 (Verdict를 직접 정하지 않음)

```
ULRS = √(Love%ile × Durability%ile) × Conversion_Readiness_Gap × (1 − Risk_Penalty%)
```

ULRS 공식과 해석(값 클수록 매수 신호, 음수면 배제 신호)은 그대로 유지하되, 이제 다음 두 곳에만
쓴다:
1. **Market Recognition Gate 판정의 근거 수치** — `Conversion_Readiness_Gap` 부호가 곧 이 Gate의
   통과/위반 여부다.
2. **Entry Timing/Expected Return 산정** — `references/catalyst_and_entry.md`(원문
   `entry_timing.md`)의 Gap 크기 기반 Entry Timing 4-category, Expected Return 시나리오 계산에
   계속 쓰인다.

메모에는 ULRS 수치도 함께 표시하되(참고 지표로), Final Verdict 배지는 이 문서의 Score+Gate
임계값 결과를 표시한다 — 둘이 다른 결론을 내는 경우(예: ULRS>0인데 Gate 위반으로 AVOID) 반드시
근거에 그 이유를 명시한다.

## 이 레포 파이프라인에서 호출될 때의 축약 판정 매핑

`judgment-rules.md`(기준③, 2026-08-13 확인)가 정의한 규칙 그대로 최종 Verdict를 다음처럼
환산해 반환한다(Claude.ai 단독 실행 시에도 이 Verdict 자체는 동일하게 적용한다 — 부합/부분부합/
미부합 환산만 파이프라인 호출 시 추가):

- **BUY → 부합**
- **WATCH → 부분부합**
- **AVOID(Gate 위반 포함) → 미부합**

이 절차는 `judgment-rules.md` 원문과 대조해 확인된 것이며, 그 문서가 개정되면 이 표도 함께
갱신한다.
