# Scorecard, Gates, and Final Verdict

## Scorecard (100점) — 재가중 (기본 스코어카드 대비)

이 철학은 Layer A(구조적 수요)와 Layer G(시장의 오분류 여부)가 판단의 핵심이므로 기본
가중치(A=10, G=15)를 상향하고 나머지는 비례 축소한다.

| 평가 항목 | 기본 가중치 | 이 철학 가중치 | 이유 |
|---|---:|---:|---|
| A. Structural Demand | 10 | **18** | 구조적 수요 존재 자체가 Thesis의 뿌리 |
| B. Product/Brand | 12 | 10 | |
| C. Customer Economics | 18 | 12 | 이 철학에서는 부차적(Retention 철학과 다름) |
| D. Competitive Advantage | 12 | 10 | |
| E. Distribution | 6 | 8 | |
| F. Financial Translation | 15 | 12 | |
| G. Variant Perception | 15 | **18** | "시장이 오분류했는가" = 이 철학의 핵심 검증 지점 |
| H. Catalyst | 7 | 6 | |
| I. Valuation | 10 | 6 | |
| **합계** | **100** | **100** | |

Risk / Thesis Durability는 별도로 최대 **-15점** 감점한다.

모든 행에 **점수/최대 + 1~2줄 근거**를 남긴다. 근거 없는 행을 남기지 않는다.

## Gate Conditions (채점 이후 적용, 높은 원점수를 override 가능)

- **Valuation Gate** — 이미 Bull Case가 주가에 반영 중이면 점수와 무관하게 BUY를 막을 수
  있다(Gate를 점검했는지, 통과했는지 명시적으로 서술한다).
- **Consensus Gate** — Variant View가 "시장이 이미 아는 좋은 점"(`variant_perception.md`
  category 1)뿐이면 Variant Perception 점수를 0으로 강제한다. **이 철학은 특히 이 Gate에
  취약하다** — "구조냐 순환이냐" 논쟁 자체가 이미 언론/실적콜에서 공개적으로 다뤄지는 경우가
  많기 때문에 반드시 명시적으로 점검한다.
- **Financial Translation Gate** — Layer C·D가 높아도 Layer F(Financial Translation)가 장기
  정체면 전체 점수 상한을 캡(예: 60점)한다 — 상위 Layer만으로 BUY를 정당화하지 않는다.
- **Data Integrity Gate** — Historical Macro Sensitivity, Peer Divergence 등 핵심 데이터가
  비공개거나 합리적 추정이 불가능하면 임의로 긍정적인 가정을 만들지 않는다. "Insufficient
  Data"로 표기하고 보수적으로(중간값으로 평균 내지 않고) 채점한다 — 데이터 결여 자체를 확신에
  대한 실질적 감점 요인으로 취급한다.

각 Gate마다 발동 여부와 그것이 점수/Verdict에 어떤 영향을 줬는지 명시적으로 서술한다.

## Final Verdict Thresholds

- **BUY** — Score ≥ 80 AND 모든 Gate 통과 AND 명확한 Variant Perception 존재 AND Valuation
  Gap 존재 AND 6~12개월 내 Catalyst 존재.
- **WATCH** — Score 65~79. Thesis는 유효하나 Catalyst/Valuation/데이터 확인이 더 필요.
- **PASS** — Score 50~64, 또는 Gate 하나라도 위반(원점수가 높아도).
- **SELL** — 기존 보유 종목에서 `catalyst_and_entry.md`의 Thesis Break Signal이 확정된 경우.

BUY 점수인데 Gate를 위반했다면 반드시 PASS로 귀결된다 — Gate는 소프트 조정이 아니라 하드
제약이다.

## 이 레포 파이프라인에서 호출될 때의 축약 판정 매핑

`judgment-rules.md`(기준②, 2026-08-13 확인)가 정의한 규칙 그대로 최종 Verdict를 다음처럼
환산해 반환한다(Claude.ai 단독 실행 시에는 이 절차를 적용하지 않는다 — SKILL.md 본문 참조):

- **BUY → 부합**
- **WATCH → 부분부합**
- **PASS(Gate 위반 포함) → 미부합**
- SELL은 신규 판단(1단계 필터링)에는 등장하지 않는다 — 기존 보유분 매도 판단에서만 쓴다.
- 이 매핑은 Core Thesis Test의 중간 판정(Supported/Partially/Not)이 아니라, Gate 적용 후
  나오는 **최종 Verdict**를 기준으로 한다.

이 절차는 `judgment-rules.md` 원문과 대조해 확인된 것이며, 그 문서가 개정되면 이 표도 함께
갱신한다.
