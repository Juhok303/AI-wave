# AI-wave

B2C 개별기업에 대한 투자 판단을 자동화하는 Claude Code 기반 투자 데스크.

## 제출물 3종

1. **판단 규칙서** — [`judgment-rules.md`](judgment-rules.md)
2. **작동하는 도구** — `.claude/skills/`의 데이터 수집·판단 스킬들과 이를 오케스트레이션하는 `.claude/agents/investment-desk.md`
3. **실제 판단 1건** — [`reports/`](reports/)에 커밋되는 투심보고서

## 실행 방법

1. `.env.example`을 `.env`로 복사하고 `DART_API_KEY`, `FRED_API_KEY`(필수), `FNSPACE_API_KEY`(선택 — 아래 "FnGuide 관련 참고" 참조)를 채운다. `pip install -r requirements.txt`로 의존성을 설치한다.
2. Claude Code에서 이 레포를 열고 `investment-desk` 에이전트에게 판단하고 싶은 기업명을 준다.
   (예: "삼성전자 판단해줘")
3. 에이전트가 **0단계(요구사항 점검, `check-requirements`)**를 가장 먼저 실행해 `.env` 키가 실제로 동작하는지 확인한다. 필수 항목(DART/FRED)이 실패하면 여기서 멈추고 무엇을 채워야 하는지 안내한다.
4. 이어서 데이터 수집 → 1단계(핵심 기준 3가지 필터링) → 2단계(스크리닝 체크리스트 5개 항목 flag) → 보고서 작성까지 자동으로 수행하며, 결과는 `reports/<기업명>-<yyyymmdd>.md`에 저장된다.

### FnGuide 관련 참고 (2026-08-12 확인)
FnGuide 컨센서스는 로그인 방식(`FNGUIDE_ID`/`FNGUIDE_PW`)이지만, 이용권이 없는 계정으로는 실제 데이터를 볼 수 없는 것으로 확인됐다. 정식 경로는 **fnspace.com(FnGuide 공식 API, 유료 가입)**의 `FNSPACE_API_KEY`다. 이 키가 없으면 `fetch-fnguide`는 자동으로 건너뛰고 나머지 파이프라인은 정상 진행된다.

## 레포 구조

```
AI-wave/
├── judgment-rules.md          # 판단 규칙서 (1단계 핵심 기준 3개 + 2단계 스크리닝 체크리스트)
├── docs/
│   └── report-format-reference.md  # 보고서 양식 참고자료 (여러 기준이 공유)
├── .env.example                # API 키 자리표시자
├── requirements.txt             # lib/ 클라이언트 실행에 필요한 Python 패키지
├── .claude/
│   ├── skills/                 # check-requirements 1개 + 데이터 수집 4개(DART/FnGuide/FRED/웹) + 1단계 판단 기준 3개(모두 독립형 패키지: judge-retention-pricing-power, judge-structural-vs-cyclical, judge-underpriced-customer-love) + 2단계 스크리닝 1개
│   └── agents/investment-desk.md  # 오케스트레이터 에이전트
├── lib/                        # DART/FnGuide/FRED API 클라이언트 (fetch-web은 별도 클라이언트 없이 WebSearch/WebFetch 사용)
├── data/cache/                 # 기업별 원자료 캐시 (git 미추적)
└── reports/                    # 실제 판단 결과물
```

### 문서 배치 규칙
- `docs/`: 특정 기준 하나에 종속되지 않고 **여러 스킬이 공유**하는 문서만 (예: `report-format-reference.md`). 기준 하나만의 설계문서는 여기 두지 않는다.
- `.claude/skills/<스킬명>/references/`, `.../assets/`: 그 스킬 하나만 참조하는 설계문서·예시 (예: `judge-structural-vs-cyclical/references/thesis-tree.md`, `judge-retention-pricing-power/references/*.md`, `judge-underpriced-customer-love/references/underpriced-customer-love-framework.md`).

## 진행 상황

| 스킬/에이전트 | 상태 |
| --- | --- |
| `check-requirements` | ✅ 구현·검증 완료 (DART/FRED 라이브 체크) |
| `fetch-dart` | ✅ 구현 완료, 재무상태표 계정(부채총계·자본총계 등) 추가 반영 — BGF리테일 end-to-end 실행으로 검증됨 |
| `fetch-fred` | ✅ 구현·검증 완료 (실제 API로 테스트) |
| `fetch-fnguide` | ⏳ 보유 계정에 컨센서스 이용권 없음 확인됨 — FnSpace(fnspace.com) 유료 가입/키 발급 대기, 스텁만 존재 |
| `fetch-web` | 🔧 스킬 정의 완료 (WebSearch/WebFetch 사용, 로직은 실행 시점에 Claude가 수행) |
| `judge-structural-vs-cyclical` | ✅ chaemin의 공식 패키지(`SKILL.md` + `references/thesis-tree.md` + `assets/example-memo-onon.html`)로 통일 완료(2026-08-12) — jiwoong이 먼저 넣어둔 축약 버전은 폐기, 중복 폴더(`structural-cyclical-misclassification-memo`)는 삭제. `judge-retention-pricing-power`와 동일한 이슈(BUY/WATCH/PASS/SELL 산출, `/mnt/user-data/outputs/` 관례) 있음 |
| `judge-retention-pricing-power` | ✅ pjueun의 공식 패키지(`SKILL.md` + `references/` 7개 문서 + `assets/` memo_template.html·example-memo-costco.html)로 통일 완료(2026-08-12) — 제가 먼저 쓴 역추출 잠정 버전 및 중복 폴더(`retention-pricing-power-memo`)는 정리·삭제. ⚠️ 다만 이 SKILL.md는 `judgment-rules.md`/`investment-desk` 파이프라인과 무관하게 독립적으로 작성돼(부합/부분부합/미부합이 아니라 BUY/WATCH/PASS/SELL 산출, `judgment-rules.md` 미참조), 파일 출력 경로도 Claude.ai 전용 표현(`/mnt/user-data/outputs/`, `present_files`)이라 Claude Code(`investment-desk`)에서 그대로 호출하면 안 맞는 부분이 있음 — 아래 참고 |
| `judge-underpriced-customer-love` | ✅ 독립형 스킬로 재작성 완료(2026-08-12) — 사용자가 커밋한 원본 설계 HTML을 `references/underpriced-customer-love-framework.md`(마크다운 변환본)로 정리하고, `judge-retention-pricing-power`/`judge-structural-vs-cyclical`와 같은 형태(Universe Filter→Layer→Gate→Scorecard→메모)로 SKILL.md 재작성. 실제 리서치로 Duolingo(DUOL) 워크드 예시 완성(`assets/example-memo-duolingo.html`, 결과: WATCH, ULRS≈−0.10 — Gap이 이미 대부분 닫혀 매수 신호 아님). 이 스킬은 `investment-desk` 파이프라인용 부합/부분부합/미부합 환산 단계를 SKILL.md 안에 자체적으로 포함하고 있어 다른 둘과 달리 저장 경로 이슈가 없음 |
| `screen-fundamentals` | ✅ 5개 항목 계산식·임계값 반영 완료 (이자보상배율·ROIC·TAM/시가총액은 데이터 공백으로 일부 Proxy·미구현 상태, 스킬 파일에 명시) |
| `investment-desk` (오케스트레이터) | ✅ end-to-end 1건 실행 완료(제출물③, BGF리테일) — `reports/BGF리테일-20260812.md`. 실행 중 `dart_client.py`의 CIS/IS 버그 발견·수정. ⚠️ 이 보고서는 기준①②가 chaemin/pjueun 버전으로 교체되기 **전** 정의로 만들어졌으므로 최신 판단 규칙과 정확히 일치하지 않는다 — 별도로 `reports/BGF리테일_Investment_Memo.md`+`.html`(공식 retention-pricing-power 패키지로 재실행, PASS 39/100, Entry: WAIT)이 생성됐지만 이건 기준① 단독 메모이지 3기준 통합 재실행은 아직임 |

## 스킬 구조 개선 가이드 — 기준①(retention-pricing-power-memo) 골격에 맞추기

세 철학 스킬(기준①·②·③)의 **깊이를 통일**하기 위한 가이드. 기준①이 가장 정교하게 설계돼 있어 이를 기준선으로 삼는다. 아래 8개 요소가 기준①에는 있고 기준②에는 없는 것들이며, 앞으로 만들 기준③은 처음부터 이 8개를 갖춰야 한다.

### 1. Guiding Behavioral Rules (SKILL.md 상단에 명시)
기준①은 SKILL.md 최상단에 "이 스킬이 매번 지켜야 할 행동원칙" 5개를 명시한다 — ① 데이터는 항상 값+기간+출처로 표기(Fact/Estimate/Inference 구분), ② 반증 우선 원칙(분석 시작 전 반대 근거 최소 3개부터 찾기), ③ 인과 전달 확인(Layer 간 연결이 끊기는 지점을 반드시 명시), ④ 추상적 표현 금지("브랜드가 강하다" 같은 서술을 숫자 없이 쓰지 않기), ⑤ Variant Perception 자기검증("정말 시장이 모르는가?"를 항상 먼저 검증).
**기준② 개선 방안**: `SKILL.md` 최상단에 같은 형식의 5개 원칙을 이 철학에 맞게 다시 쓴다. 예: "④ 추상적 표현 금지"는 구조적/순환적 철학에서는 "'구조적이다'라는 판단은 반드시 침투율·세대별 채택 데이터 등 수치로 뒷받침, '느낌상 구조적'은 금지"로 구체화.

### 2. Universe Filter (본분석 전 적합성 판정)
기준①은 본분석 전에 이 철학이 그 기업에 적용 가능한지부터 판정한다 — Good fit(상장·B2C·반복구매 구조)/Poor fit(순수 B2B·원자재 커머디티·가격규제 산업) 조건을 명시적으로 나열하고, `Framework Fit: High/Medium/Low`를 먼저 출력한다. Low면 14섹션 전체를 강행하지 않고 짧은 설명만 남긴다.
**기준② 개선 방안**: 현재는 Universe Filter 없이 바로 Layer 1 분석을 시작한다. "이 기업이 신생 상장사라 경기 하방 데이터 자체가 없는가", "카테고리 자체가 침투율 개념이 성립하지 않는 산업인가"를 먼저 판정하는 단계를 추가한다.

### 3. 철학 고유 하위 테스트를 별도 문서로 명문화
기준①은 "Pricing Power Test"라는 4개 하위테스트를 `references/pricing_power_test.md`로 분리해 체크리스트화했다(① 실제 가격 인상 여부 ② 인상 후 Retention/Churn 비교 ③ Mix를 통한 가격 인상 ④ 경쟁사 대비 ASP Premium).
**기준② 개선 방안**: `references/thesis-tree.md` Layer 2(Cyclical Contamination Test)에 이미 있는 내용(Historical Macro Sensitivity, Peer Divergence, Growth Decomposition)을 별도 `references/cyclical_contamination_test.md`로 승격해 기준①과 같은 형식(테스트 번호 + 데이터 요구사항 + "Insufficient Data면 추론 금지")으로 재작성한다.

### 4. Financial Transmission Chain을 명시적 인과사슬로
기준①: `Retention → Churn↓/Frequency↑ → LTV↑ → CAC Payback↓ → Pricing/Mix↑ → Gross Margin↑ → Contribution Margin↑ → Operating Leverage → EPS/FCF Revision → Multiple Re-rating`처럼 9단계 화살표 체인을 문서로 명시하고, 각 링크를 Confirmed/Emerging/Broken/Insufficient Data로 마킹한다.
**기준② 개선 방안**: 구조적 성장 철학에 맞는 인과사슬을 정의한다. 예: `Penetration Rate↑ → Category Volume↑ → Company Revenue↑ → Peer Divergence 확인 → Sell-side 섹터 재분류 → Multiple 확장`. 지금은 이런 명시적 체인 없이 "Financial Transmission" 섹션에 표만 있다.

### 5. Variant Perception 6-category 자기검증
기준①: 발견한 관점을 반드시 6개 카테고리 중 하나로 분류한다(1. 시장이 이미 아는 좋은 점 / 2. 알지만 중요도를 낮게 봄 / 3. 아직 인식 못함 / 4. 잘못 해석 / 5. 재무제표 밖 선행지표 / 6. Valuation 미반영 Optionality). **1번은 Variant View로 인정하지 않는다**는 규칙까지 명시.
**기준② 개선 방안**: 지금은 `class-badge`로 자유서술 분류만 한다("주로 4번이나 6번에 가깝고..."). 6개 카테고리 정의를 `references/`에 명문화하고, 1번 판정 시 Variant Perception 점수를 자동으로 낮추는 규칙(Consensus Gate)을 SKILL.md에 명시적으로 연결한다.

### 6. Entry Timing 4-category 고정
기준①: BUY NOW / BUY ON CONFIRMATION / BUY ON WEAKNESS / WAIT 중 반드시 하나를 선택하고, 각 카테고리가 뭘 의미하는지 정의돼 있다.
**기준② 개선 방안**: 지금은 "Buy on Confirmation" 같은 문구를 예시적으로만 쓴다. 4개 카테고리를 고정 용어로 명문화한다.

### 7. 이중 산출물 (.md + .html)
기준①은 Markdown과 HTML을 **둘 다** 필수로 생성한다(`[Company]_Investment_Memo.md` + `.html`, 동일 내용).
**기준② 개선 방안**: 지금은 HTML만 생성한다. Markdown 버전도 추가하면 diff 리뷰·재사용성이 좋아진다.

### 8. output_template.md로 정확한 스켈레톤 고정
기준①은 채워야 할 정확한 마크다운 골격이 `references/output_template.md`로 고정돼 있다.
**기준② 개선 방안**: 이런 고정 템플릿 파일이 없다 — `references/output_template.md`를 신설해 14섹션 스켈레톤을 못박는다.

### 기준③을 새로 만들 때 (처음부터 이 골격으로)
`docs/underpriced-customer-love-framework.md`에 이미 있는 소재를 활용하면 대부분 재료가 준비돼 있다:
- **Universe Filter**: "리뷰·검색량·앱 데이터가 확보 가능한 B2C 소비재/구독/플랫폼"을 Good fit으로.
- **철학 고유 하위 테스트**: 문서 H절의 Red Flag 10종을 `references/red_flag_test.md`로, E절의 Gap 공식 5종을 `references/underpricing_gap_test.md`로 승격.
- **Financial Transmission Chain**: `Love↑ → Durability 확인(AND 조건) → Operating Monetization Gap 축소 → Financial Conversion 확인 → Market Recognition Gap 축소 → Re-rating`.
- **Variant Perception 6-category**: 기준①·②와 동일 체계 재사용.
- **Entry Timing**: 문서 F절의 Stage 1~5(Watchlist/Early/Main/Late/Fully Priced)를 4-category(BUY NOW/CONFIRMATION/WEAKNESS/WAIT)에 매핑.
- **이중 산출물 + output_template.md**: 처음부터 포함.

## 기여자 ↔ 스킬 매핑 (1인 1기여)

각 팀원은 스킬 또는 에이전트를 최소 1개 만들어 커밋합니다. 구현 상태는 위 "진행 상황" 표를 참고하고, 아래는 담당자만 채워 나갑니다.

| 담당자 | 스킬/에이전트 |
| --- | --- |
| | `check-requirements` |
| | `fetch-dart` |
| | `fetch-fnguide` |
| | `fetch-fred` |
| | `fetch-web` |
| pjueun | `judge-retention-pricing-power` — SKILL.md·references 7개·assets(memo_template, example-memo-costco) 전체 기여 |
| chaemin | `judge-structural-vs-cyclical` — SKILL.md·references/thesis-tree.md·assets/example-memo-onon.html 전체 기여 |
| | `judge-underpriced-customer-love` |
| | `screen-fundamentals` |
| | `investment-desk` (오케스트레이터) |

## 완성 기준

다른 팀 사람이 `judgment-rules.md`와 `.claude/` 도구만 받아서, 우리 팀이 보지 않은 기업에 대해서도 판단을 낼 수 있으면 완성입니다.
