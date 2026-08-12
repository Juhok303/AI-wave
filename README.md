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
│   └── underpriced-customer-love-framework.md  # 기준③(ULRS) 상세 방법론 참고자료
├── .env.example                # API 키 자리표시자
├── requirements.txt             # lib/ 클라이언트 실행에 필요한 Python 패키지
├── .claude/
│   ├── skills/                 # check-requirements 1개 + 데이터 수집 4개(DART/FnGuide/FRED/웹) + 1단계 판단 기준 3개(judge-retention-pricing-power는 독립형 메모 패키지로 통일됨) + 2단계 스크리닝 1개 + 독립형 메모 스킬 1개(structural-cyclical-misclassification-memo)
│   └── agents/investment-desk.md  # 오케스트레이터 에이전트
├── lib/                        # DART/FnGuide/FRED API 클라이언트 (fetch-web은 별도 클라이언트 없이 WebSearch/WebFetch 사용)
├── data/cache/                 # 기업별 원자료 캐시 (git 미추적)
└── reports/                    # 실제 판단 결과물
```

### 문서 배치 규칙
- `docs/`: `judgment-rules.md`(공식 판단 규칙서)가 직접 링크하는 참고자료만 (예: `underpriced-customer-love-framework.md`, `report-format-reference.md`).
- `.claude/skills/<스킬명>/references/`, `.../assets/`: 그 스킬 하나만 참조하는 설계문서·예시 (예: `structural-cyclical-misclassification-memo/references/thesis-tree.md`, `judge-retention-pricing-power/references/*.md`).

## 진행 상황

| 스킬/에이전트 | 상태 |
| --- | --- |
| `check-requirements` | ✅ 구현·검증 완료 (DART/FRED 라이브 체크) |
| `fetch-dart` | ✅ 구현 완료, 재무상태표 계정(부채총계·자본총계 등) 추가 반영 — BGF리테일 end-to-end 실행으로 검증됨 |
| `fetch-fred` | ✅ 구현·검증 완료 (실제 API로 테스트) |
| `fetch-fnguide` | ⏳ 보유 계정에 컨센서스 이용권 없음 확인됨 — FnSpace(fnspace.com) 유료 가입/키 발급 대기, 스텁만 존재 |
| `fetch-web` | 🔧 스킬 정의 완료 (WebSearch/WebFetch 사용, 로직은 실행 시점에 Claude가 수행) |
| `judge-structural-vs-cyclical` | ✅ chaemin의 `thesis-tree.md`(source of truth)를 파이프라인 데이터로 근사한 축약판으로 재작성 완료(2026-08-12). 실 데이터 실행 검증은 아직 |
| `judge-retention-pricing-power` | ✅ pjueun의 공식 패키지(`SKILL.md` + `references/` 7개 문서 + `assets/` memo_template.html·example-memo-costco.html)로 통일 완료(2026-08-12) — 제가 먼저 쓴 역추출 잠정 버전 및 중복 폴더(`retention-pricing-power-memo`)는 정리·삭제. ⚠️ 다만 이 SKILL.md는 `judgment-rules.md`/`investment-desk` 파이프라인과 무관하게 독립적으로 작성돼(부합/부분부합/미부합이 아니라 BUY/WATCH/PASS/SELL 산출, `judgment-rules.md` 미참조), 파일 출력 경로도 Claude.ai 전용 표현(`/mnt/user-data/outputs/`, `present_files`)이라 Claude Code(`investment-desk`)에서 그대로 호출하면 안 맞는 부분이 있음 — 아래 참고 |
| `judge-underpriced-customer-love` | ✅ `judgment-rules.md` 대체지표 정의 확정 + 스킬에 계산식·임계값 반영 완료. 실 데이터로 실행 검증은 아직 |
| `screen-fundamentals` | ✅ 5개 항목 계산식·임계값 반영 완료 (이자보상배율·ROIC·TAM/시가총액은 데이터 공백으로 일부 Proxy·미구현 상태, 스킬 파일에 명시) |
| `investment-desk` (오케스트레이터) | ✅ end-to-end 1건 실행 완료(제출물③, BGF리테일) — `reports/BGF리테일-20260812.md`. 실행 중 `dart_client.py`의 CIS/IS 버그 발견·수정. ⚠️ 이 보고서는 기준①②가 chaemin/pjueun 버전으로 교체되기 **전** 정의로 만들어졌으므로 최신 판단 규칙과 정확히 일치하지 않는다 — 별도로 `reports/BGF리테일_Investment_Memo.md`+`.html`(공식 retention-pricing-power 패키지로 재실행, PASS 39/100, Entry: WAIT)이 생성됐지만 이건 기준① 단독 메모이지 3기준 통합 재실행은 아직임 |
| `structural-cyclical-misclassification-memo` | ✅ 독립형 스킬 완료 (chaemin 기여, `.claude/skills/`로 경로 정리함). `judgment-rules.md` 파이프라인과 별개로 기준②(Structural vs Cyclical) 철학을 자체 Layer A–G 스코어카드·Gate 조건으로 채점해 HTML 투자메모를 생성. `references/thesis-tree.md`, `assets/example-memo-onon.html` 포함 |

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
| | `judge-structural-vs-cyclical` |
| | `judge-underpriced-customer-love` |
| | `screen-fundamentals` |
| | `investment-desk` (오케스트레이터) |
| chaemin | `structural-cyclical-misclassification-memo` |

## 완성 기준

다른 팀 사람이 `judgment-rules.md`와 `.claude/` 도구만 받아서, 우리 팀이 보지 않은 기업에 대해서도 판단을 낼 수 있으면 완성입니다.
