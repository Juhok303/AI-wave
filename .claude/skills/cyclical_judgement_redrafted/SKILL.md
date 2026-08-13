---
name: judge-structural-vs-cyclical
description: >
  회사명/티커를 주고 투자 판단, BUY/WATCH/PASS/SELL 콜, Investment Memo, 또는 이 회사가 "구조적
  성장"인지 "경기·유행 순환"인지 판정해달라는 요청이 오면 이 스킬을 쓴다 — "이 회사 구조적이야
  순환적이야 봐줘", "내 investment philosophy로 분석해줘"(이 철학을 가리킬 때), "포트폴리오에
  있는 종목들 이 철학으로 하나씩 돌려봐줘" 같은 표현도 트리거. 이 스킬은 하나의 고정된 투자철학만
  적용한다 — 소비자 행동의 구조적 변화를 시장이 경기·유행 순환으로 오인해 Multiple을 잘못
  매긴다는 가설을 검증하는 것. 다른 프레임워크(DCF-only, 일반 SWOT, 단순 Bull/Bear 나열)로
  대체하지 않는다. 이 스킬은 항상 Markdown Investment Memo와 스타일이 적용된 HTML Investment
  Memo 두 개의 산출물을 만드는 것으로 끝난다.
---

# Structural vs. Cyclical Misclassification — Investment Decision Skill

## 이 스킬이 무엇인가

이건 일반 리서치 어시스턴트가 아니다. 모든 회사에 항상 같은 질문을 던지는 **고정된 판단
구조**다:

> "이 회사 소비자 행동의 [성장/둔화]는 경기 순환이나 일시적 유행이 아니라 구조적 전환이며,
> 시장은 순환적 Multiple/할인율을 적용해 이를 오평가하고 있는가?"

다른 투자철학으로 절대 대체하지 않는다. 회사가 "뻔히" 통과/탈락할 것 같아도 스텝을 건너뛰지
않는다. 항상 아래 인과사슬 전체를 실행하고, 어디서 체인이 끊기는지를 찾는다.

**모든 분석을 관통하는 핵심 믿음:**

> Penetration/Adoption ↑ → Category Volume ↑ → Company Revenue ↑(자사 고유, 카테고리 편승
> 아님) → Peer Divergence 확인 → Sell-side 섹터 재분류 → Multiple Re-rating

**매번 새로 검증할 Core Thesis (참으로 가정하지 않는다):**

> "[회사]의 최근 [성장/둔화] 궤적은 경기 순환이나 일시적 유행이 아니라 구조적 전환이며, 시장은
> 순환적 Multiple/할인율을 적용해 이를 오평가하고 있다."

Verdict는 반드시 다음 중 하나: **Supported / Partially Supported / Not Supported**.

## Guiding behavioral rules (전 과정에 적용, 한 번만 적용하는 게 아님)

1. **재무제표 우선순위**: 항상 최신 데이터를 검색해서 사용한다(web search / 회사 IR, 10-K/10-Q,
   실적콜, investor day, 신뢰도 높은 산업 데이터·언론, 셀사이드 리포트 순). 숫자는 항상
   **값 + 기간 + 출처**로 표기한다. 데이터가 없으면 만들지 말고 "Insufficient Data"라고 쓴다.
   Fact / Estimate / Inference를 명확히 구분한다.
2. **반증 우선 원칙**: 분석을 시작하기 전에 "이 회사가 이 투자철학(구조적 전환)에 맞지 않고
   실은 순환적/유행성이라는 가장 강한 증거는 무엇인가?"를 먼저 묻고, 최소 3개의 반대 근거를
   적극적으로 찾은 뒤에 Thesis를 평가한다. **Layer 2(Cyclical Contamination Test)는 절대
   생략하지 않는다** — 진짜로 반증을 시도한다. PASS로 끝나는 것도 정상적인 결과다. Bull case를
   만들기 위해 이 스킬이 존재하는 게 아니다.
3. **인과 전달 확인**: 각 Layer를 독립 체크리스트로 채점하지 말고, 앞 Layer의 결과가 실제로
   Financial Transmission Chain으로 전달되는지 확인한다. 연결이 끊어지는 지점을 반드시 찾아
   명시한다.
4. **추상적 표현 금지**: "구조적인 느낌이다", "확실히 트렌드가 바뀌었다" 같은 표현은 금지한다.
   "구조적이다"라는 판단은 항상 침투율(%), 세대별 채택 데이터(pp 변화), 카테고리 성장률 같은
   관찰 가능한 숫자로 뒷받침한다. "느낌상 구조적"은 근거가 아니다.
5. **Variant Perception 자기검증**: 시장이 이미 공개적으로 논쟁 중인 "구조냐 순환이냐" 이슈를
   Variant View로 인정하지 않는다. "정말 시장이 모르는가?"를 항상 먼저 검증한다. 이 철학은
   Consensus Gate에 특히 취약하다 — 실적콜에서 애널리스트가 반복 질문하는 이슈는 대부분 이미
   컨센서스에 편입돼 있기 때문이다.

## Workflow (이 순서대로 실행)

1. **Universe Filter** — `references/layers_a_to_g.md` §Universe Filter를 먼저 읽는다.
   `Framework Fit: High / Medium / Low`를 출력한다. Low면 왜 안 맞는지 평이하게 설명하고
   14섹션 전체 메모를 억지로 만들지 않는다 — 짧은 설명이 Low-fit 회사에는 정확하고 완전한
   산출물이다.
2. **데이터 수집** — 어떤 Layer도 쓰기 전에 이 회사의 최신 침투율/코호트 데이터, 과거 경기
   하방기 실적, Peer 실적, Volume/Price 분해, 셀사이드 섹터 분류, 현재/역사적 Multiple을
   검색한다. web search를 적극 활용한다 — 이 스킬은 그 뒤의 데이터만큼만 좋다. 숫자마다 값 +
   기간 + 출처를 남긴다.
3. **Layers A → G** — `references/layers_a_to_g.md`를 순서대로 따른다(Structural Demand →
   Product/Brand → Customer Economics → Competitive Advantage → Distribution → Financial
   Translation → Variant Perception). Layer F(Financial Translation) 안에서
   `references/cyclical_contamination_test.md`의 **Cyclical Contamination Test**(3개 하위
   테스트)를 반드시 실행한다.
4. **Financial Transmission Chain** — `references/financial_transmission.md`에 따라 각 링크를
   Confirmed / Emerging / Broken / Insufficient Data로 마킹하고, 체인이 어디까지 진행됐는지 한
   문장으로 진단한다.
5. **Variant Perception** — Market Believes / We Believe / Why Market May Be Wrong / Evidence /
   Recognition Trigger를 작성한 뒤, `references/variant_perception.md`의 6-category 자기검증으로
   분류한다. Category 1은 절대 Variant View로 인정하지 않는다.
6. **Catalyst Map, Entry Timing, Valuation, Expected Return, Holding Period, Thesis Break** —
   `references/catalyst_and_entry.md`를 따른다. Entry Timing은 반드시 4개 중 하나로 고정한다.
7. **Scorecard, Gates, Final Verdict** — `references/scorecard_and_verdict.md`를 정확히
   따른다. Gate가 막은 점수는 주지 않는다. 모든 행에 점수/최대 + 1-2줄 근거를 남긴다.
8. **메모 작성** — `references/output_template.md`의 정확한 구조를 따른다(0. Snapshot → 1. Fit
   → 2. Core Thesis Test → 3. Structural Signal Evidence → 4. Cyclical Contamination & Market
   Framing Test → 5. Financial Transmission → 6. Layer A-G → 7. Variant Perception → 8. Catalyst
   Map → 9. Valuation → 10. Expected Return → 11. Entry Strategy → 12. Thesis Break → 13.
   Scorecard → 14. Final Investment Decision).
9. **산출물 생성** — 아래 "Final file output" 참조. 이 단계는 필수다 — 대화창 답변만으로는 이
   스킬을 완료한 게 아니다.

## Final file output (필수)

메모 내용이 확정되면 항상 아래 두 파일을 **동일한 내용**으로 생성한다(회사명 공백은
언더스코어로, 특수문자는 제거):

- `[Company]_Investment_Memo.md` — `references/output_template.md`에 정의된 구조 그대로.
- `[Company]_Investment_Memo.html` — 같은 내용을 ledger/paper/stamp 스타일 IM 리포트로 렌더링.
  Scorecard, Financial Transmission Chain, Layer A-G 표, Catalyst Map, Valuation/Expected
  Return은 반드시 실제 `<table>`로 렌더링하고(plain text 나열 금지), Final Verdict
  (BUY/WATCH/PASS/SELL)는 상단에 스탬프 형태 배지로 눈에 띄게 표시한다. `assets/memo_template.html`
  을 베이스로 쓰고, 매번 스타일을 새로 만들지 않는다.

Steps:
1. 두 파일을 먼저 `/home/claude/`에 쓰고, 최종본을 `/mnt/user-data/outputs/`로 복사한다.
2. `present_files`로 두 경로를 전달한다(.md 먼저, .html 다음).
3. 파일 전달 후 긴 후기를 붙이지 않는다 — 이 회사에 특화된 핵심 설계 판단(가중치가 왜 이렇게
   나왔는지, Gate가 왜 발동/미발동했는지, 결론이 왜 그 등급인지)을 2-4줄로 짧게 설명한다.

## 이 레포 파이프라인(judgment-rules.md)에서 호출될 때만 적용하는 절차

Claude.ai 단독 실행이 아니라 `investment-desk` 오케스트레이터가 이 스킬을 호출하는 레포
파이프라인 안에서 실행될 때는:

- 파일 저장 경로를 위 `/mnt/user-data/outputs/` / `present_files` 관례 대신 그 레포의
  `reports/` 관례로 보정한다(SKILL.md 본문 자체는 원작자 그대로 유지, 호출 시점에
  오케스트레이터가 경로만 보정).
- 최종 Verdict를 `judgment-rules.md`(기준②)가 정의한 매핑 규칙 그대로 축약해 반환한다:
  - **BUY → 부합**
  - **WATCH → 부분부합**
  - **PASS (Gate 위반 포함) → 미부합**
  - SELL은 신규 판단(1단계 필터링)에는 등장하지 않는다 — 기존 보유분 매도 판단에서만 쓴다.
  - Core Thesis Test의 중간 판정(Supported/Partially/Not Supported)이 아니라, **Gate 적용 후
    나오는 최종 Verdict**를 기준으로 매핑한다.
- 100점 스코어카드(Layer A-G 재가중), 4개 Gate, 채점 로직 자체는 그대로 따르고 이 절차에서
  별도 임계값을 새로 만들지 않는다.

이 매핑 규칙의 유일한 출처는 `judgment-rules.md`이며, 그 문서가 개정되면 이 절차도 함께
갱신한다.

## Reference files (필요할 때 로드)

- `references/layers_a_to_g.md` — Universe Filter + Layer A-G 전체 정의와 필요 지표.
- `references/cyclical_contamination_test.md` — Layer F 안에서 실행하는 3개 필수 하위 테스트.
- `references/financial_transmission.md` — Penetration→Re-rating 체인과 링크별 마킹법.
- `references/variant_perception.md` — Market Believes/We Believe 구조 + 6-way 자기검증.
- `references/catalyst_and_entry.md` — Catalyst Map, Entry Timing(4개 고정), Valuation, Expected
  Return, Holding Period, Thesis Break/Sell Discipline.
- `references/scorecard_and_verdict.md` — 100점 스코어카드(재가중), Gate 조건, BUY/WATCH/PASS/
  SELL 임계값.
- `references/output_template.md` — 채워야 할 정확한 메모 스켈레톤(요구되는 14-섹션 포맷과
  일치).
- `assets/memo_template.html` — HTML 산출물의 베이스 CSS/레이아웃 템플릿.
