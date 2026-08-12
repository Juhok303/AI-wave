---
name: judge-underpriced-customer-love
description: >
  Use this skill whenever the user gives a company name or ticker and wants an investment view
  through the "Underpriced Customer Love" lens —소비자가 실제로 사랑하지만 아직 재무성과·밸류에이션에
  반영되지 않은 B2C 기업을 찾는 투자 판단. Trigger on "이 회사 고객들이 진짜 좋아하는데 아직 저평가된
  것 같아", "Underpriced Customer Love로 봐줘", "ULRS 계산해줘", "이 브랜드 팬덤이 진짜인지 봐줘" 같은
  요청, 또는 리뷰·재구매율·DAU 같은 소비자 애착 지표가 두드러지는 B2C/구독/뷰티/컨슈머앱 기업 분석
  요청. This skill applies ONE FIXED philosophy — 진짜 애착(Love×Durability) + 재무 전환 능력
  (Conversion) + 시장의 미인식(Gap) 세 조건의 동시 성립 — as the mandatory lens. Do NOT substitute a
  generic bull/bear or DCF-only analysis when this skill is applicable. Ends by producing a styled
  HTML Investment Memo (and, when running inside this repo's investment-desk pipeline, also a short
  judgment-rules.md-compliant verdict for judge_underpriced_customer_love.json).
---

# Underpriced Customer Love (ULRS) Investment Decision Skill

## What this skill is

This is a **fixed decision architecture**, not a general equity-research assistant. It always tests
the same three-part claim about a company:

> ① 소비자가 진짜로 이 기업을 사랑하는가(Love), 그 사랑이 유행이 아니라 지속되는가(Durability) —
> ② 그 애착을 재무 성과로 바꿀 능력이 있는가(Conversion) —
> ③ 그런데도 시장(밸류에이션·컨센서스)은 아직 이를 반영하지 않았는가(Gap).

Never substitute a different philosophy. Never skip a Layer because a company "obviously" fits. Full
methodology (Layer definitions, Gap formulas, Entry Timing, Red Flags, Sector Fit, ULRS 공식 유도)는
`references/underpriced-customer-love-framework.md`에 있다 — 매 분석마다 요약만 보지 말고 다시 읽는다.

**Core formula (final composite, never approximate without computing the parts):**

```
ULRS = √(Love%ile × Durability%ile) × Conversion_Readiness_Gap × (1 − Risk_Penalty%)
```

Verdict must be one of: **BUY(최적 매수구간, ULRS>0 &크다) / WATCH(Gap 근접·전환 미증명, ULRS≈0) / AVOID(ULRS<0 또는 Red Flag 2개↑)**.

## Guiding behavioral rules (apply throughout)

1. **정규화 우선**: 모든 지표는 raw 값이 아니라 Peer 대비 Percentile Rank(0~100)로 비교한다(문서 E절 Peer Group 3중 필터 — 없으면 아래 "Peer Group 축소판" 절차를 쓴다).
2. **AND 구조 유지**: Love와 Durability는 반드시 곱(기하평균)으로 결합한다 — "사랑은 있는데 지속성 0"인 반짝 유행주가 산술평균으로 통과되는 것을 막기 위함이다. 절대 산술평균으로 대체하지 않는다.
3. **데이터 신뢰도 명시**: 모든 수치에 Confidence(High=공시/회사발표, Medium=3rd-party, Low=Proxy/역산)를 표기하고 문서 K절 할인율(0.8x/0.6x)을 적용한다. 정보 없음을 중립(50점)으로 채우지 않는다 — 해당 weight를 제외하고 재정규화한다.
4. **반증 우선**: Durability(Layer 2)와 Red Flag(H절) 점검을 절대 생략하지 않는다. "사랑받는다"는 증거만 모으고 "반짝 유행 아닌가"를 확인하지 않으면 이 스킬을 잘못 쓴 것이다.
5. **Gate 우선순위**: Red Flag 2개 이상이면 점수 계산과 무관하게 즉시 AVOID로 확정하고 나머지 단계는 생략 가능(문서 H절).

## Workflow (run in this order)

1. **Universe Filter** — 문서 J절 Sector Fit Matrix로 이 기업의 업종 적합도(높음/중/낮음)를 먼저 판정한다. 적합도가 "낮음"이면 그 이유(유행성·경기순환 노이즈가 Love 신호를 압도하는 업종 등)를 밝히고 축약 메모로 마무리한다(전체 워크플로를 강제하지 않는다).
2. **데이터 수집** — 재구매율/리뷰/DAU-MAU/가격 인상 이력(Layer 1), Retention Decay·Moat(Layer 2), ARPU·마진·CAC(Layer 3), LTV/CAC·영업레버리지·FCF(Layer 4), 컨센서스·EV/Sales(Layer 5)를 웹 검색·공시로 조사한다. 모든 수치는 **값 + 기간 + 출처**를 남긴다. 확인 안 되면 "Insufficient Data".
3. **Layer 1~2 — Love & Durability** — 문서 C-1/C-2절 지표로 Love%ile, Durability%ile을 각각 산정한다. Peer Group은 아래 "Peer Group 축소판" 절차로 근사한다.
4. **Layer 3~5 — Gap 산출** — 문서 C-3/C-4/C-5절로 Operating Monetization Gap, Financial Conversion Capacity, Market Recognition을 각각 산정하고, `Conversion_Readiness_Gap = (Layer4%ile − Layer5%ile)/100`을 계산한다(문서 E절).
5. **Red Flag / Risk Gate** — 문서 H절 Red Flag 10종을 전부 점검한다. `Risk_Penalty% = Red Flag 개수 × 10%p (최대 50%)`. 2개 이상이면 즉시 AVOID.
6. **ULRS 계산 및 게이트 규칙** — 위 공식으로 ULRS를 계산한다. 문서 D절 게이트 규칙(Durability Layer가 40점 미만이면 총점 상한 60점 cap)도 함께 적용해 근거에 명시한다.
7. **Catalyst & Entry Timing** — 문서 F/G절로 진입 Stage(Watchlist~Fully Priced)와 예상 Catalyst 시차를 판정한다.
8. **Holding Period & Exit Rule** — 문서 I절로 Exit 유형(Successful/Thesis-break/Time-stop)을 미리 정의한다.
9. **메모 작성** — `assets/example-memo-duolingo.html`을 스타일·구조 참조본으로 삼아(동일 파일 복붙 금지, 팀 공통 ledger/paper 시각 문법은 유지하되 이 철학 고유 색상·내용으로 다시 씀) 아래 섹션을 채운다: Snapshot → Verdict → Why This Company Fits → Love & Durability Evidence → Gap 3종(Monetization/Conversion/Recognition) → ULRS 계산 과정 → Red Flag 점검표 → Catalyst & Entry Timing → Holding Period & Exit → Scorecard(Layer1-5 + Risk) → Final Investment Decision.
10. **(이 레포 파이프라인에서 호출될 때만) 축약 판정 반환** — `investment-desk`가 1단계 필터링용으로 호출한 경우, 위 결과를 `judgment-rules.md` 기준③ 표기(부합=ULRS>0, 부분부합=ULRS≈0/WATCH, 미부합=ULRS<0/AVOID)로 환산해 짧게도 반환한다. 두 출력(전체 메모 vs 파이프라인용 축약 판정)은 같은 계산에서 나와야지 서로 다른 기준을 쓰면 안 된다.

## Peer Group 축소판 (이 레포는 GICS DB가 없음)

문서 E절 3중 필터(동일 GICS Sub-industry, 매출 0.3x~3x, 유통채널 유사성)를 아래로 근사한다:
1. 웹 검색 "`<기업명>` 경쟁사 OR 유사 서비스"로 동종업계 상장사 5~10개를 추린다.
2. 그 후보들의 매출액(공시·IR)을 확인해 대상 기업의 0.3~3배 범위에 드는 회사만 채택한다.
3. 5개 미만이면 Percentile 대신 "Peer 대비 상/중/하" 정성 3단계로 대체하고 표본 부족을 근거에 명시한다.
4. Peer Group을 아예 구성 못 하면 절대 기준(K절 Core Metric 임계값)만으로 판단하고 Percentile 항목은 판단 보류로 남긴다.

## Reference files

- `references/underpriced-customer-love-framework.md` — 전체 방법론 원문(Section A~K + 최종 ULRS 공식). 모든 Layer/Factor/Gap 공식/Red Flag/Sector Fit의 1차 출처.
- `assets/example-memo-duolingo.html` — Duolingo(DUOL)에 실제 적용한 워크드 예시이자 스타일 참조본.

## Final file output

메모 완성 시 `[Company]_ULRS_Investment_Memo.html`(스타일 렌더링본)을 생성한다. 이 레포(Claude Code) 안에서 실행할 때는 `/mnt/user-data/outputs/`가 아니라 이 레포의 관례를 따른다 — 개별 실행 예시는 `assets/`에, `investment-desk`가 대상 기업으로 실행한 최종 결과는 `reports/<기업명>-ULRS.html`에 저장한다.
