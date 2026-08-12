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

## 스킬 구조 개선 가이드 — 기준①(`judge-retention-pricing-power`) 골격에 맞추기

**2026-08-12 업데이트**: 기준②(`judge-structural-vs-cyclical`)는 chaemin의 공식 패키지로 폴더만 정리(이동)됐을 뿐 SKILL.md 내용 자체는 아래 격차와 동일하게 유지되고 있음을 재확인했다. 기준③(`judge-underpriced-customer-love`)도 새로 완성됐지만, 확인해보니 기준①과 같은 격차가 상당수 그대로 있다. 아래를 최신 상태로 갱신한다.

### ⚠️ 가장 시급한 문제 — 판단 규칙서(`judgment-rules.md`) 정합성

세 스킬 깊이를 맞추는 것보다 **이게 먼저 고쳐져야 한다** — "결과물은 판단 규칙서를 최대한 따라가야 한다"는 원칙이 지금 기준①②에서 깨져 있다.

- `judge-retention-pricing-power`, `judge-structural-vs-cyclical`는 **`judgment-rules.md`를 전혀 참조하지 않는다.** Verdict를 부합/부분부합/미부합이 아니라 자체 체계(BUY/WATCH/PASS/SELL)로만 산출하고, `judgment-rules.md`에 문서화된 매핑 규칙(Supported→부합 등)을 스킬 파일 자신이 실행하는 절차로 갖고 있지 않다 — 매핑이 규칙서에만 적혀 있고 스킬엔 없어서, `investment-desk`가 실제로 호출했을 때 이 변환을 빠뜨릴 위험이 크다(`investment-desk.md` TODO에 이미 미검증 상태로 남아있음).
- 두 스킬 모두 파일 출력 경로가 Claude.ai 전용 표현(`/mnt/user-data/outputs/`, `present_files`)으로 돼 있다 — 이 레포(Claude Code)에서 그대로 실행하면 안 맞는다.
- **반면 `judge-underpriced-customer-love`는 이미 이 문제를 스스로 해결해뒀다** — SKILL.md 10단계에 "이 레포 파이프라인에서 호출될 때만 `judgment-rules.md` 기준③ 표기(부합=ULRS>0 등)로 환산해 반환한다"는 절차가 명시돼 있고, 저장 경로도 이 레포의 `reports/` 관례를 따르도록 돼 있다. **기준①②도 이 방식을 그대로 따라야 한다.**
- **개선 방안**: 기준①②의 SKILL.md 끝에 기준③과 동일한 형태로 "(이 레포 파이프라인에서 호출될 때만) 축약 판정 반환" 단계를 추가한다 — Verdict(BUY/WATCH/PASS/SELL)를 `judgment-rules.md`가 이미 정의해둔 매핑 규칙 그대로 부합/부분부합/미부합으로 환산해 반환하고, 저장 경로도 `reports/`로 보정한다.

### 깊이 격차 8가지 (기준①이 가진 것, 기준②·③에 없는 것)

| # | 기준①에 있는 것 | 기준② 상태 | 기준③ 상태 |
|---|---|---|---|
| 1 | Guiding Behavioral Rules 5개(SKILL.md 최상단, 값+기간+출처/반증우선/인과전달확인/추상적표현금지/Variant자기검증) | ❌ 없음 | ✅ 있음(5개 원칙 명시) |
| 2 | Universe Filter (Good/Poor fit 판정 → Framework Fit: High/Medium/Low, Low면 축약 종료) | ❌ 없음, 바로 Layer 1 시작 | ✅ 있음(Sector Fit Matrix로 판정) |
| 3 | 철학 고유 하위 테스트를 별도 파일로 명문화(`pricing_power_test.md`, 4개 테스트) | ❌ Layer 서술에 뭉뚱그려짐 | ❌ `underpriced-customer-love-framework.md` 한 파일에 다 있음, 별도 승격 안 됨 |
| 4 | Financial Transmission을 9단계 화살표 인과사슬로 명시, 링크별 Confirmed/Emerging/Broken/Insufficient 마킹 | ❌ 표만 있고 명시적 체인 없음 | ❌ ULRS 계산 절차는 있으나 링크별 상태 마킹 체계는 없음 |
| 5 | Variant Perception 6-category 자기검증(1번은 Variant View로 불인정) | ❌ 자유서술 class-badge만 | ❌ 없음(Market Recognition Gap으로 대체되나 6-category 체계는 아님) |
| 6 | Entry Timing 4-category 고정(BUY NOW/CONFIRMATION/WEAKNESS/WAIT) | ❌ 자유서술("Buy on Confirmation" 예시적) | ❌ BUY/WATCH/AVOID 3-category로 다름(Confirmation·Weakness 구분 없음) |
| 7 | `.md` + `.html` 이중 산출물 필수 | ❌ HTML만 | ❌ HTML만(`[Company]_ULRS_Investment_Memo.html`) |
| 8 | `output_template.md`로 정확한 스켈레톤 고정 | ❌ 없음 | ❌ 없음 |

### 기준②·③ 공통 개선 방안 (기준①과 같은 형식으로)
1. **SKILL.md 최상단에 Guiding Behavioral Rules 5개** 추가 — 이 철학에 맞게 다시 쓴다. 예) 기준②의 "④ 추상적 표현 금지"는 "'구조적이다'는 판단은 침투율·세대별 채택 데이터로 뒷받침, '느낌상 구조적'은 금지"로. 기준③은 이미 있으니 문구만 기준①과 형식 통일.
2. **Universe Filter 신설/보강** — 기준②는 아예 신설(예: "신생 상장사라 경기 하방 데이터가 없는가", "침투율 개념이 성립 안 하는 산업인가"). 기준③은 이미 있는 Sector Fit Matrix를 기준①과 같은 출력 형식(`Framework Fit: High/Medium/Low`)으로 맞춘다.
3. **하위 테스트를 별도 `references/*_test.md` 파일로 승격** — 기준②는 Layer 2의 Historical Macro Sensitivity/Peer Divergence/Growth Decomposition을 `references/cyclical_contamination_test.md`로. 기준③은 문서 H절 Red Flag 10종을 `references/red_flag_test.md`로, E절 Gap 공식 5종을 `references/underpricing_gap_test.md`로 승격.
4. **Financial Transmission Chain 명문화** — 기준②: `Penetration Rate↑ → Category Volume↑ → Company Revenue↑ → Peer Divergence 확인 → Sell-side 섹터 재분류 → Multiple 확장`. 기준③: `Love↑ → Durability 확인(AND) → Operating Monetization Gap 축소 → Financial Conversion 확인 → Market Recognition Gap 축소 → Re-rating`.
5. **Variant Perception 6-category 도입** — 기준②·③ 모두 동일 6개 카테고리 체계를 `references/`에 명문화하고 재사용(1번 판정 시 Consensus Gate로 점수 강제 하향).
6. **Entry Timing을 4-category로 통일** — 기준③의 현재 BUY/WATCH/AVOID 3단계를 BUY NOW/CONFIRMATION/WEAKNESS/WAIT 4단계로 재매핑(문서 F절 Stage 1~5를 4-category에 대응).
7. **`.md` 버전 추가 생성** — 둘 다 HTML만 생성 중이니 Markdown 버전을 동시에 만들도록 SKILL.md에 추가.
8. **`references/output_template.md` 신설** — 기준①처럼 채워야 할 정확한 스켈레톤을 못박는다.

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
