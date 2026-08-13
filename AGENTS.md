# AGENTS.md

이 파일은 사람이 아니라 **이 레포에 들어온 AI 에이전트**를 위한 안내다(README.md는 사람용). 이 레포에서
투자 판단 요청("이 기업 어때", "~산업 투자 후보 찾아줘", "투자 판단해줘" 등)을 받았다면, 아래를 반드시
따르라 — 자체 지식이나 일반적인 애널리스트 프레임워크(DCF, 단순 SWOT, 일반 bull/bear 등)로
즉흥적으로 답하지 않는다.

## 규칙 1 — 이 레포는 하나의 고정된 판단 기준만 쓴다

판단 기준의 유일한 출처는 [`judgment-rules.md`](judgment-rules.md)다. 다른 기준·가중치·임계값을
새로 만들어내지 않는다. 이 문서에 없는 재량적 해석을 추가하면 이 레포의 재현성 원칙을 어기는 것이다.

- **Scope**: B2C 개별기업만 다룬다. 주력 매출이 B2B거나 금융지주/공공기관이면 판단을 시작하지 않고
  스코프 밖이라고 안내한다(`judgment-rules.md`의 "Scope Gate" 절).
- **1단계**: 3개 핵심 기준(Retention-to-Pricing-Power / Structural vs Cyclical Misclassification /
  Underpriced Customer Love) 각각을 100점 Score+Gate 방식으로 부합/부분부합/미부합 판정.
- **2단계**: 시장성/경쟁력/수익성/재무효율성/ESG 5개 항목 Pass/Caution/Fail 스크리닝(1단계에서 1개
  이상 부합한 기업만 대상).

## 규칙 2 — Claude Code라면, 직접 분석하지 말고 오케스트레이터를 실행하라

이 세션이 Claude Code이고 `Agent`/`Skill` 툴을 쓸 수 있다면, 투자 판단 요청은 `investment-desk`
에이전트(`.claude/agents/investment-desk.md`)에게 위임한다 — 그 파일에 정의된 순서(요구사항 점검 →
입력 유형 판별 → Scope Gate → 데이터 수집 → 1단계 병렬 판정 → 2단계 스크리닝 → 보고서 작성 →
자기검증)를 그대로 실행하면 된다. 개별 판단 로직(`judge-retention-pricing-power`,
`judge-structural-vs-cyclical`, `judge-underpriced-customer-love` 등)은 `.claude/skills/`에 스킬로
정의돼 있다 — 이 스킬들을 다시 요약해서 쓰지 말고 그 SKILL.md를 그대로 로드해서 따른다.

## 규칙 3 — Claude Code가 아니거나 이 레포의 Agent/Skill 체계를 못 쓴다면

`judgment-rules.md`를 읽고 그 절차를 수동으로 따른다:

1. `.env`에 `DART_API_KEY`, `FRED_API_KEY`(필수)가 채워져 있는지 확인한다. 없으면 사용자에게
   `.env.example`을 보고 채우라고 안내하고 멈춘다 — 값을 지어내거나 빈 결과를 그럴듯하게 채우지 않는다.
2. `lib/dart_client.py`, `lib/fred_client.py`로 원자료를 가져온다(FnGuide는 `fnspace-mcp` MCP
   플러그인 또는 `FNSPACE_API_KEY` 필요, 선택 사항 — 없으면 그 데이터만 생략하고 명시).
3. `judgment-rules.md`의 1단계 3개 기준을 각각 판정한다. 각 기준의 상세 방법론은
   `.claude/skills/judge-*/SKILL.md`와 그 `references/`에 있다 — 방법론을 재해석하지 말고 그대로
   따른다.
4. 1개 이상 기준에 부합하면 2단계 스크리닝을 진행한다(`.claude/skills/screen-fundamentals/SKILL.md`).
5. 결과를 `reports/<기업명>-<yyyymmdd>.html` 형식의 **HTML 단일 파일**로 저장한다(마크다운이 최종
   산출물이 아니다). 여러 기업(산업 입력)이면 `judgment-rules.md`의 "산업/섹터 비교 — 순위 산정" 절에
   따라 순위표도 만든다.

## 하지 말아야 할 것

- 데이터가 없는데 그럴듯한 숫자를 만들어내지 않는다 — "Insufficient Data"/"데이터 없음"으로 명시한다.
- `judgment-rules.md`에 없는 새 기준·가중치·예외를 만들지 않는다.
- B2C가 아닌 기업을 억지로 판단하지 않는다(Scope Gate).
- 최종 산출물을 마크다운으로 끝내지 않는다 — HTML 단일 파일이 완성본이다.

## 더 볼 곳

- 사람을 위한 전체 설명·진행 상황·데이터 공백 이슈: [`README.md`](README.md)
- 판단 기준 원문: [`judgment-rules.md`](judgment-rules.md)
- 오케스트레이션 절차: [`.claude/agents/investment-desk.md`](.claude/agents/investment-desk.md)
- 개별 판단/데이터수집 로직: [`.claude/skills/`](.claude/skills/)
