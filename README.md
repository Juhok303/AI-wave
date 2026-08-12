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
│   ├── skills/                 # check-requirements 1개 + 데이터 수집 4개(DART/FnGuide/FRED/웹) + 1단계 판단 기준 3개 + 2단계 스크리닝 1개 + 독립형 메모 스킬 2개
│   └── agents/investment-desk.md  # 오케스트레이터 에이전트
├── lib/                        # DART/FnGuide/FRED API 클라이언트 (fetch-web은 별도 클라이언트 없이 WebSearch/WebFetch 사용)
├── data/cache/                 # 기업별 원자료 캐시 (git 미추적)
└── reports/                    # 실제 판단 결과물
```

### 문서 배치 규칙
- `docs/`: `judgment-rules.md`(공식 판단 규칙서)가 직접 링크하는 참고자료만 (예: `underpriced-customer-love-framework.md`, `report-format-reference.md`).
- `.claude/skills/<스킬명>/references/`, `.../assets/`: 그 스킬 하나만 참조하는 설계문서·예시 (judgment-rules.md 파이프라인과 무관한 개인 기여 스킬 전용, 예: `structural-cyclical-misclassification-memo`, `retention-pricing-power-memo`).

## 진행 상황

| 스킬/에이전트 | 상태 |
| --- | --- |
| `check-requirements` | ✅ 구현·검증 완료 (DART/FRED 라이브 체크) |
| `fetch-dart` | ✅ 구현 완료, 재무상태표 계정(부채총계·자본총계 등) 추가 반영 — BGF리테일 end-to-end 실행으로 검증됨 |
| `fetch-fred` | ✅ 구현·검증 완료 (실제 API로 테스트) |
| `fetch-fnguide` | ⏳ 보유 계정에 컨센서스 이용권 없음 확인됨 — FnSpace(fnspace.com) 유료 가입/키 발급 대기, 스텁만 존재 |
| `fetch-web` | 🔧 스킬 정의 완료 (WebSearch/WebFetch 사용, 로직은 실행 시점에 Claude가 수행) |
| `judge-retention-pricing-power` / `judge-structural-vs-cyclical` / `judge-underpriced-customer-love` | ✅ `judgment-rules.md` 대체지표 정의 확정 + 스킬에 계산식·임계값 반영 완료. 실 데이터로 실행 검증은 아직 |
| `screen-fundamentals` | ✅ 5개 항목 계산식·임계값 반영 완료 (이자보상배율·ROIC·TAM/시가총액은 데이터 공백으로 일부 Proxy·미구현 상태, 스킬 파일에 명시) |
| `investment-desk` (오케스트레이터) | ✅ end-to-end 1건 실행 완료(제출물③, BGF리테일) — `reports/BGF리테일-20260812.md`. 실행 중 `dart_client.py`의 CIS/IS 버그 발견·수정 |
| `structural-cyclical-misclassification-memo` | ✅ 독립형 스킬 완료 (chaemin 기여, `.claude/skills/`로 경로 정리함). `judgment-rules.md` 파이프라인과 별개로 기준②(Structural vs Cyclical) 철학을 자체 Layer A–I 스코어카드·4개 Gate로 채점해 HTML 투자메모를 생성. `references/thesis-tree.md`, `assets/example-memo-onon.html` 포함 |
| `retention-pricing-power-memo` | ✅ 완료 — 원작자가 먼저 올린 프로토타입 `assets/example-memo-costco.html`을 짝 스킬 구조에 맞춰 `SKILL.md`+`references/thesis-tree.md`(Layer 재가중 포함)로 공식화, 색상 팔레트는 costco 예시 기준(짙은 그린/틸)으로 통일. BGF리테일로 실행 검증(`reports/BGF리테일-retention-pricing-power-memo-20260812.html`, PASS 53/100) |

## 기여자 ↔ 스킬 매핑 (1인 1기여)

각 팀원은 스킬 또는 에이전트를 최소 1개 만들어 커밋합니다. 구현 상태는 위 "진행 상황" 표를 참고하고, 아래는 담당자만 채워 나갑니다.

| 담당자 | 스킬/에이전트 |
| --- | --- |
| | `check-requirements` |
| | `fetch-dart` |
| | `fetch-fnguide` |
| | `fetch-fred` |
| | `fetch-web` |
| | `judge-retention-pricing-power` |
| | `judge-structural-vs-cyclical` |
| | `judge-underpriced-customer-love` |
| | `screen-fundamentals` |
| | `investment-desk` (오케스트레이터) |
| chaemin | `structural-cyclical-misclassification-memo` |
| | `retention-pricing-power-memo` — 프로토타입 예시(costco)는 원작자 기여, SKILL.md/thesis-tree.md 공식화는 Claude Code로 완료. 담당자 이름 기입 필요 |

## 완성 기준

다른 팀 사람이 `judgment-rules.md`와 `.claude/` 도구만 받아서, 우리 팀이 보지 않은 기업에 대해서도 판단을 낼 수 있으면 완성입니다.
