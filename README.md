# AI-wave

B2C 개별기업에 대한 투자 판단을 자동화하는 Claude Code 기반 투자 데스크.

## 제출물 3종

1. **판단 규칙서** — [`judgment-rules.md`](judgment-rules.md)
2. **작동하는 도구** — `.claude/skills/`의 데이터 수집·판단 스킬들과 이를 오케스트레이션하는 `.claude/agents/investment-desk.md`
3. **실제 판단 1건** — [`reports/`](reports/)에 커밋되는 투심보고서

## 실행 방법

1. `.env.example`을 `.env`로 복사하고 `DART_API_KEY`, `FNGUIDE_API_KEY`, `FRED_API_KEY`를 채운다.
2. Claude Code에서 이 레포를 열고 `investment-desk` 에이전트에게 판단하고 싶은 기업명을 준다.
   (예: "삼성전자 판단해줘")
3. 에이전트가 데이터 수집 → 1단계(핵심 기준 3가지 필터링) → 2단계(스크리닝 체크리스트 5개 항목 flag) → 보고서 작성까지 자동으로 수행하며, 결과는 `reports/<기업명>-<yyyymmdd>.md`에 저장된다.

## 레포 구조

```
AI-wave/
├── judgment-rules.md          # 판단 규칙서
├── .env.example                # API 키 자리표시자
├── .claude/
│   ├── skills/                 # 데이터 수집 3개 + 1단계 판단 기준 3개 + 2단계 스크리닝 1개 스킬
│   └── agents/investment-desk.md  # 오케스트레이터 에이전트
├── lib/                        # DART/FnGuide/FRED API 클라이언트
├── data/cache/                 # 기업별 원자료 캐시 (git 미추적)
└── reports/                    # 실제 판단 결과물
```

## 기여자 ↔ 스킬 매핑 (1인 1기여)

각 팀원은 스킬 또는 에이전트를 최소 1개 만들어 커밋합니다. 아래 표를 채워 나갑니다.

| 담당자 | 스킬/에이전트 | 상태 |
| --- | --- | --- |
| | `fetch-dart` | TODO |
| | `fetch-fnguide` | TODO |
| | `fetch-fred` | TODO |
| | `judge-retention-pricing-power` | TODO |
| | `judge-structural-vs-cyclical` | TODO |
| | `judge-underpriced-customer-love` | TODO |
| | `screen-fundamentals` | TODO |
| | `investment-desk` (오케스트레이터) | TODO |

## 완성 기준

다른 팀 사람이 `judgment-rules.md`와 `.claude/` 도구만 받아서, 우리 팀이 보지 않은 기업에 대해서도 판단을 낼 수 있으면 완성입니다.
