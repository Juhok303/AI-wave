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

### FnGuide 관련 참고 (2026-08-13 갱신 — 연결됨)
FnGuide 컨센서스·재무 데이터는 **[`fnspace-mcp`](https://github.com/xavierchoi/fnspace-mcp) MCP 플러그인**으로 연결 완료됐다(`mcp__fnspace__*` 도구 7개). 설치·연결 방법:
```
claude plugin marketplace add https://github.com/xavierchoi/fnspace-mcp
claude plugin install fnspace@fnspace-mcp --scope user
```
그 다음 세션에서 `/reload-plugins`를 실행해야 도구가 보인다. `claude mcp list`에서 `plugin:fnspace:fnspace ✔ Connected`인지 확인할 것.

⚠️ **키 만료 임박**: 현재 이 플러그인에 동봉된 임시 공유 키(원작자 xavierchoi 제공, 학습/해커톤용으로 보임)로 동작 중이며 **2026-08-15에 만료**된다. 그 전에 팀 자체 `FNSPACE_API_KEY`를 발급받아 환경변수로 export하면(동봉된 키보다 우선 적용) 계속 쓸 수 있다. 참고로 www.fnguide.com 로그인 방식(`FNGUIDE_ID`/`FNGUIDE_PW`)은 계정에 이용권이 없어 여전히 사용 불가 — 이제 이 경로는 쓰지 않는다.

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
| `fetch-fnguide` | ✅ `fnspace-mcp` MCP 플러그인으로 연결 완료(2026-08-13, `mcp__fnspace__*` 도구 7개 — 재무/목표주가/추정실적/Fwd지표). ⚠️ 동봉된 임시 공유 키가 2026-08-15 만료 — 팀 자체 FNSPACE_API_KEY로 교체 필요. `lib/fnguide_client.py`(www.fnguide.com 로그인)는 이용권 없어 폐기, 참고용으로만 보관 |
| `fetch-web` | 🔧 스킬 정의 완료 (WebSearch/WebFetch 사용, 로직은 실행 시점에 Claude가 수행) |
| `judge-structural-vs-cyclical` | ✅ chaemin의 공식 패키지(`SKILL.md` + `references/thesis-tree.md` + `assets/example-memo-onon.html`)로 통일 완료(2026-08-12) — jiwoong이 먼저 넣어둔 축약 버전은 폐기, 중복 폴더(`structural-cyclical-misclassification-memo`)는 삭제. `judge-retention-pricing-power`와 동일한 이슈(BUY/WATCH/PASS/SELL 산출, `/mnt/user-data/outputs/` 관례) 있음 |
| `judge-retention-pricing-power` | ✅ pjueun의 공식 패키지(`SKILL.md` + `references/` 7개 문서 + `assets/` memo_template.html·example-memo-costco.html)로 통일 완료(2026-08-12) — 제가 먼저 쓴 역추출 잠정 버전 및 중복 폴더(`retention-pricing-power-memo`)는 정리·삭제. ⚠️ 다만 이 SKILL.md는 `judgment-rules.md`/`investment-desk` 파이프라인과 무관하게 독립적으로 작성돼(부합/부분부합/미부합이 아니라 BUY/WATCH/PASS/SELL 산출, `judgment-rules.md` 미참조), 파일 출력 경로도 Claude.ai 전용 표현(`/mnt/user-data/outputs/`, `present_files`)이라 Claude Code(`investment-desk`)에서 그대로 호출하면 안 맞는 부분이 있음 — 아래 참고 |
| `judge-underpriced-customer-love` | ✅ 기준①(pjueun) 깊이에 맞춰 전면 재작성 완료(2026-08-12) — 아래 "깊이 격차 8가지" 전 항목 반영: Guiding Rules 5개, Universe Filter, 하위테스트 파일 승격(`references/underpricing_gap_test.md`, `references/red_flag_test.md`), Financial Transmission 6단계 체인+링크별 마킹(`references/financial_transmission.md`), Variant Perception 6-category(`references/variant_perception.md`, 기준①과 동일 체계 재사용), Entry Timing 4-category 재매핑(`references/entry_timing.md`), `output_template.md` 14-section 스켈레톤, `.md`+`.html` 이중 산출물. Duolingo(DUOL) 워크드 예시를 새 구조로 재생성(`assets/example-memo-duolingo.md`+`.html`, 결과: WATCH, ULRS≈−0.10, Score 56/100). 파이프라인용 부합/부분부합/미부합 환산 단계도 SKILL.md에 포함 |
| `screen-fundamentals` | ✅ 5개 항목 계산식·임계값 반영 완료 (이자보상배율·ROIC·TAM/시가총액은 데이터 공백으로 일부 Proxy·미구현 상태, 스킬 파일에 명시) |
| `investment-desk` (오케스트레이터) | ✅ end-to-end 1건 실행 완료(제출물③, BGF리테일) — `reports/BGF리테일-20260812.md`. 실행 중 `dart_client.py`의 CIS/IS 버그 발견·수정. ⚠️ 이 보고서는 기준①②가 chaemin/pjueun 버전으로 교체되기 **전** 정의로 만들어졌으므로 최신 판단 규칙과 정확히 일치하지 않는다 — 별도로 `reports/BGF리테일_Investment_Memo.md`+`.html`(공식 retention-pricing-power 패키지로 재실행, PASS 39/100, Entry: WAIT)이 생성됐지만 이건 기준① 단독 메모이지 3기준 통합 재실행은 아직임. **Scope Gate 추가(2026-08-13)** — 1단계로 대상 기업이 B2C인지부터 확인하고, B2B 등 스코프 밖이면 데이터 수집·판단을 아예 시작하지 않고 그 자리에서 사용자에게 안내(`judgment-rules.md`의 "Scope Gate" 절 참고). 아직 실제 B2B 기업으로 실행 검증은 안 함 |

## 공통 데이터 공백 — 시가총액/주가 소스 부재

세 철학 스킬(기준①②③) 전부와 `screen-fundamentals`가 동시에 막혀 있는 공통 병목. 하나만 고치면 여러 곳의 품질이 동시에 올라간다.

### 문제
이 레포의 데이터 키트(DART/FRED/FnGuide) 중 어느 것도 **현재 주가·시가총액·발행주식수**를 제공하지 않는다.
- **DART**: `lib/dart_client.py`가 가져오는 건 정기보고서 재무제표(손익계산서·재무상태표)와 공시 목록뿐 — 시세 데이터는 DART API 자체에 없음.
- **FRED**: 미국 거시지표(CPI/기준금리/소매판매/실업률)만 제공 — 개별 종목 주가와 무관.
- **FnGuide/FnSpace**: 컨센서스·목표주가는 `fnspace-mcp`로 연결됐지만(2026-08-13), 재무 항목(`get_financials`)에도 시가총액·발행주식수는 포함되지 않음 — 시세 자체는 별도 소스가 필요.

### 영향받는 곳
- `screen-fundamentals`의 "시장성" 항목 — TAM/시가총액 배수를 계산해야 하는데 시가총액 자체가 없어 `web.json` 검색 Proxy에만 의존(스킬 파일의 "알려진 데이터 공백"에 이미 명시돼 있음).
- `judge-retention-pricing-power`, `judge-structural-vs-cyclical`의 **Valuation 섹션** — 현재 Multiple(PER/EV·EBITDA 등), 역사적 Range, Peer Multiple을 전부 계산해야 하는데 매번 "Insufficient Data"로 빠짐. BGF리테일 실행 사례(`reports/BGF리테일_Investment_Memo.md`)에서 실제로 이 섹션 전체가 Insufficient Data였고, Scorecard의 "I. Valuation" 항목이 매번 최저점 근처로 깎이는 구조적 원인이 됨.
- `judge-underpriced-customer-love`의 Layer 5(Market Recognition Gap) — `EV/Sales Percentile` 계산에 시가총액이 필요.

### 진행 상황 (2026-08-13, 잠정 해결)
- **`pykrx` 시도 → 막힘**: `.venv`를 새로 만들어(전역 anaconda의 numpy/matplotlib ABI 충돌 회피) `pykrx`를 설치·실행했으나, KRX 데이터 엔드포인트가 세션 쿠키를 정상적으로 받아온 뒤에도 `400 LOGOUT`을 반환한다 — 알려진 pykrx/KRX anti-bot 이슈로 보이며, 헤더 한두 개 고치는 수준으로 해결되지 않았다.
- **KRX Open API 키 발급됨 → 아직 미승인**: `openapi.krx.co.kr` 인증키는 받았고 서버 인증까지는 통과하지만(`data-dbg.krx.co.kr` 실측), 시세 API 서비스 자체의 활용신청·관리자 승인이 아직이라 `401 Unauthorized API Call`. 승인 대기 중.
- **잠정 해결(팀 결정, 2026-08-13)**: KRX 승인을 기다리는 대신 `fetch-web`이 웹 검색으로 시가총액/현재가를 가져와 `web.json`의 `market_data` 필드에 채우도록 구현 완료 — `screen-fundamentals`(시장성)와 `judge-underpriced-customer-love`(Valuation)가 이미 이 필드를 참조하도록 연결됨. Medium Confidence(3rd-party 웹, 공식 API 아님)로 명시.
- **남은 일**: KRX API 승인되면 `lib/market_data_client.py`를 신설해 그쪽 값을 우선 채택(웹 검색은 보조/검증용으로 격하). `judge-retention-pricing-power`/`judge-structural-vs-cyclical`(pjueun/chaemin 스킬)는 원래도 "웹 검색을 적극 활용하라"는 지침이 있어 별도 수정 없이도 시가총액을 스스로 찾을 수 있지만, 실제로 잘 찾는지는 재실행해서 확인 필요.

### 우선순위
`judgment-rules.md` 정합성 다음으로 이게 두 번째로 시급했고, 웹 검색 기반으로 잠정 해결됐다 — 다만 Medium Confidence 데이터라는 한계는 남아있다.

## 스킬 구조 개선 가이드 — 기준①(`judge-retention-pricing-power`) 골격에 맞추기

**2026-08-12 업데이트 (2차)**: 기준③(`judge-underpriced-customer-love`)의 깊이 격차 8가지를 전부 반영 완료. 기준②(`judge-structural-vs-cyclical`, chaemin 작성)는 아직 폴더 이동만 됐을 뿐 아래 격차가 그대로 남아있다 — 다음 작업 대상.

### ⚠️ 가장 시급한 문제 — 판단 규칙서(`judgment-rules.md`) 정합성

세 스킬 깊이를 맞추는 것보다 **이게 먼저 고쳐져야 한다** — "결과물은 판단 규칙서를 최대한 따라가야 한다"는 원칙이 지금 기준①②에서 깨져 있다.

- `judge-retention-pricing-power`, `judge-structural-vs-cyclical`는 **`judgment-rules.md`를 전혀 참조하지 않는다.** Verdict를 부합/부분부합/미부합이 아니라 자체 체계(BUY/WATCH/PASS/SELL)로만 산출하고, `judgment-rules.md`에 문서화된 매핑 규칙(Supported→부합 등)을 스킬 파일 자신이 실행하는 절차로 갖고 있지 않다 — 매핑이 규칙서에만 적혀 있고 스킬엔 없어서, `investment-desk`가 실제로 호출했을 때 이 변환을 빠뜨릴 위험이 크다(`investment-desk.md` TODO에 이미 미검증 상태로 남아있음).
- 두 스킬 모두 파일 출력 경로가 Claude.ai 전용 표현(`/mnt/user-data/outputs/`, `present_files`)으로 돼 있다 — 이 레포(Claude Code)에서 그대로 실행하면 안 맞는다.
- **반면 `judge-underpriced-customer-love`는 이미 이 문제를 스스로 해결해뒀다** — SKILL.md 10단계에 "이 레포 파이프라인에서 호출될 때만 `judgment-rules.md` 기준③ 표기(부합=ULRS>0 등)로 환산해 반환한다"는 절차가 명시돼 있고, 저장 경로도 이 레포의 `reports/` 관례를 따르도록 돼 있다. **기준①②도 이 방식을 그대로 따라야 한다.**
- **개선 방안**: 기준①②의 SKILL.md 끝에 기준③과 동일한 형태로 "(이 레포 파이프라인에서 호출될 때만) 축약 판정 반환" 단계를 추가한다 — Verdict(BUY/WATCH/PASS/SELL)를 `judgment-rules.md`가 이미 정의해둔 매핑 규칙 그대로 부합/부분부합/미부합으로 환산해 반환하고, 저장 경로도 `reports/`로 보정한다.

### 깊이 격차 8가지 (기준①이 가진 것, 기준②·③에 없는 것)

| # | 기준①에 있는 것 | 기준② 상태 | 기준③ 상태(2026-08-12 반영 완료) |
|---|---|---|---|
| 1 | Guiding Behavioral Rules 5개(SKILL.md 최상단, 값+기간+출처/반증우선/인과전달확인/추상적표현금지/Variant자기검증) | ❌ 없음 | ✅ 있음(5개 원칙 기준①과 동일 형식으로 명시) |
| 2 | Universe Filter (Good/Poor fit 판정 → Framework Fit: High/Medium/Low, Low면 축약 종료) | ❌ 없음, 바로 Layer 1 시작 | ✅ Sector Fit Matrix로 `Framework Fit: High/Medium/Low` 동일 출력 형식 |
| 3 | 철학 고유 하위 테스트를 별도 파일로 명문화(`pricing_power_test.md`, 4개 테스트) | ❌ Layer 서술에 뭉뚱그려짐 | ✅ `references/underpricing_gap_test.md`(Gap 공식 5종), `references/red_flag_test.md`(Red Flag 10종)로 승격, 메인 문서는 포인터만 남김 |
| 4 | Financial Transmission을 9단계 화살표 인과사슬로 명시, 링크별 Confirmed/Emerging/Broken/Insufficient 마킹 | ❌ 표만 있고 명시적 체인 없음 | ✅ `references/financial_transmission.md` — Love→Re-rating 6단계 체인 + 링크별 마킹 |
| 5 | Variant Perception 6-category 자기검증(1번은 Variant View로 불인정) | ❌ 자유서술 class-badge만 | ✅ `references/variant_perception.md` — 기준①과 동일 6개 카테고리 재사용, Market Recognition Gap에 적용 |
| 6 | Entry Timing 4-category 고정(BUY NOW/CONFIRMATION/WEAKNESS/WAIT) | ❌ 자유서술("Buy on Confirmation" 예시적) | ✅ `references/entry_timing.md` — 4-category로 통일, 문서 F절 5-stage를 재매핑 |
| 7 | `.md` + `.html` 이중 산출물 필수 | ❌ HTML만 | ✅ `assets/example-memo-duolingo.md` + `.html` 동시 생성, SKILL.md에 필수로 명시 |
| 8 | `output_template.md`로 정확한 스켈레톤 고정 | ❌ 없음 | ✅ `references/output_template.md` — 14-section 스켈레톤 |

### 기준② 개선 방안 (남은 작업, 기준①③과 같은 형식으로)
1. **SKILL.md 최상단에 Guiding Behavioral Rules 5개** 추가 — 이 철학에 맞게 다시 쓴다. 예) "④ 추상적 표현 금지"는 "'구조적이다'는 판단은 침투율·세대별 채택 데이터로 뒷받침, '느낌상 구조적'은 금지"로.
2. **Universe Filter 신설** — 예: "신생 상장사라 경기 하방 데이터가 없는가", "침투율 개념이 성립 안 하는 산업인가"를 판정해 `Framework Fit: High/Medium/Low` 출력.
3. **하위 테스트를 별도 `references/*_test.md` 파일로 승격** — Layer 2의 Historical Macro Sensitivity/Peer Divergence/Growth Decomposition을 `references/cyclical_contamination_test.md`로.
4. **Financial Transmission Chain 명문화** — `Penetration Rate↑ → Category Volume↑ → Company Revenue↑ → Peer Divergence 확인 → Sell-side 섹터 재분류 → Multiple 확장`, 링크별 상태 마킹 추가.
5. **Variant Perception 6-category 도입** — 기준①③과 동일 6개 카테고리 체계를 `references/`에 명문화하고 재사용.
6. **Entry Timing을 4-category로 통일** — BUY NOW/BUY ON CONFIRMATION/BUY ON WEAKNESS/WAIT로 재매핑.
7. **`.md` 버전 추가 생성** — HTML만 생성 중이니 Markdown 버전을 동시에 만들도록 SKILL.md에 추가.
8. **`references/output_template.md` 신설** — 채워야 할 정확한 스켈레톤을 못박는다.

이 8가지는 chaemin이 작성한 SKILL.md/thesis-tree.md를 구조적으로 다시 쓰는 작업이라, 원작자 확인 후 진행하는 게 안전하다(pjueun 패키지를 그대로 통합한 것과 달리, 이건 다른 사람의 콘텐츠를 실질적으로 재작성하는 것).

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
