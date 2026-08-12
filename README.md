# AI-wave

B2C 개별기업에 대한 투자 판단을 자동화하는 Claude Code 기반 투자 데스크.

## 제출물 3종

1. **판단 규칙서** — [`judgment-rules.md`](judgment-rules.md)
2. **작동하는 도구** — `.claude/skills/`의 데이터 수집·판단 스킬들과 이를 오케스트레이션하는 `.claude/agents/investment-desk.md`
3. **실제 판단 1건** — [`reports/`](reports/)에 커밋되는 투심보고서

## 실행 방법

1. `.env.example`을 `.env`로 복사하고 `DART_API_KEY`, `FNGUIDE_API_KEY`, `FRED_API_KEY`를 채운다. `pip install -r requirements.txt`로 의존성을 설치한다.
2. Claude Code에서 이 레포를 열고 `investment-desk` 에이전트에게 판단하고 싶은 기업명을 준다.
   (예: "삼성전자 판단해줘")
3. 에이전트가 데이터 수집 → 1단계(핵심 기준 3가지 필터링) → 2단계(스크리닝 체크리스트 5개 항목 flag) → 보고서 작성까지 자동으로 수행하며, 결과는 `reports/<기업명>-<yyyymmdd>.md`에 저장된다.

## 레포 구조

```
AI-wave/
├── judgment-rules.md          # 판단 규칙서 (1단계 핵심 기준 3개 + 2단계 스크리닝 체크리스트)
├── docs/
│   └── underpriced-customer-love-framework.md  # 기준③(ULRS) 상세 방법론 참고자료
├── .env.example                # API 키 자리표시자
├── requirements.txt             # lib/ 클라이언트 실행에 필요한 Python 패키지
├── .claude/
│   ├── skills/                 # 데이터 수집 4개(DART/FnGuide/FRED/웹) + 1단계 판단 기준 3개 + 2단계 스크리닝 1개 스킬
│   └── agents/investment-desk.md  # 오케스트레이터 에이전트
├── lib/                        # DART/FnGuide/FRED API 클라이언트 (fetch-web은 별도 클라이언트 없이 WebSearch/WebFetch 사용)
├── data/cache/                 # 기업별 원자료 캐시 (git 미추적)
└── reports/                    # 실제 판단 결과물
```

## 진행 상황

| 스킬/에이전트 | 상태 |
| --- | --- |
| `fetch-dart` | ✅ 구현 완료, 재무상태표 계정(부채총계·자본총계 등) 추가 반영 — 실 API 재검증 필요(코드 변경 후 삼성전자 재테스트 대기) |
| `fetch-fred` | ✅ 구현·검증 완료 (실제 API로 테스트) |
| `fetch-fnguide` | ⏳ FnGuide 키 확보 대기, 스텁만 존재 |
| `fetch-web` | 🔧 스킬 정의 완료 (WebSearch/WebFetch 사용, 로직은 실행 시점에 Claude가 수행) |
| `judge-retention-pricing-power` / `judge-structural-vs-cyclical` / `judge-underpriced-customer-love` | ✅ `judgment-rules.md` 대체지표 정의 확정 + 스킬에 계산식·임계값 반영 완료. 실 데이터로 실행 검증은 아직 |
| `screen-fundamentals` | ✅ 5개 항목 계산식·임계값 반영 완료 (이자보상배율·ROIC·TAM/시가총액은 데이터 공백으로 일부 Proxy·미구현 상태, 스킬 파일에 명시) |
| `investment-desk` (오케스트레이터) | 🔧 실행 순서 정의 완료, end-to-end 실행(제출물③)은 아직 — Python 설치 + DART/FRED API 키 필요 |

## 기여자 ↔ 스킬 매핑 (1인 1기여)

각 팀원은 스킬 또는 에이전트를 최소 1개 만들어 커밋합니다. 구현 상태는 위 "진행 상황" 표를 참고하고, 아래는 담당자만 채워 나갑니다.

| 담당자 | 스킬/에이전트 |
| --- | --- |
| | `fetch-dart` |
| | `fetch-fnguide` |
| | `fetch-fred` |
| | `fetch-web` |
| | `judge-retention-pricing-power` |
| | `judge-structural-vs-cyclical` |
| | `judge-underpriced-customer-love` |
| | `screen-fundamentals` |
| | `investment-desk` (오케스트레이터) |

## 완성 기준

다른 팀 사람이 `judgment-rules.md`와 `.claude/` 도구만 받아서, 우리 팀이 보지 않은 기업에 대해서도 판단을 낼 수 있으면 완성입니다.
