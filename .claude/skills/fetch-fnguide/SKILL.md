---
name: fetch-fnguide
description: FnGuide 컨센서스·재무 데이터(추정 실적, 목표주가, EPS 등)를 fnspace MCP 도구로 조회해 data/cache/에 저장한다. 투자 판단 파이프라인의 데이터 수집 단계 중 하나.
---

# fetch-fnguide

## 현재 상태 (2026-08-13 갱신)
- FnGuide 컨센서스는 [`fnspace-mcp`](https://github.com/xavierchoi/fnspace-mcp) 플러그인(FnGuide 공식 API인 FnSpace를 감싼 MCP 서버)으로 연결 완료. `claude mcp list`에서 `plugin:fnspace:fnspace ✔ Connected` 확인됨.
- ⚠️ **키 출처**: 현재는 이 플러그인 레포에 동봉된 임시 공유 키로 동작 중이며 **2026-08-15에 만료**된다. 그 이후에도 계속 쓰려면 팀 자체 `FNSPACE_API_KEY`를 발급받아 환경변수로 설정해야 한다(설정하면 동봉된 임시 키보다 우선 적용됨 — `mcp-fnspace/server.py`의 `load_api_key()` 우선순위 참고).
- www.fnguide.com 로그인 방식(`FNGUIDE_ID`/`FNGUIDE_PW`, `lib/fnguide_client.py`)은 계정에 이용권이 없어 여전히 불가 — 이제 이 경로는 쓰지 않는다. `lib/fnguide_client.py`는 참고용으로만 남겨둔다.
- `/reload-plugins`를 실행해야 현재 세션에서 도구가 보인다(플러그인을 새로 설치/업데이트한 직후 1회).

## 입력
- 기업명 또는 종목코드(6자리, 예: `005930`) 1개

## 동작
아래 fnspace MCP 도구를 필요에 따라 조합해 호출한다(모두 종목코드에 `A` 접두를 자동으로 붙여준다):

1. `mcp__fnspace__quickstart` — 최초 1회, 키/연결 상태를 자가 진단(무료 호출).
2. `mcp__fnspace__get_financials(code, from_year, to_year, quarterly=False)` — 확정 재무(매출액·영업이익·당기순이익·자산총계·자본총계). `judge-retention-pricing-power`/`judge-structural-vs-cyclical`의 Financial Transmission·Layer F 근거로 쓸 수 있다.
3. `mcp__fnspace__get_target_price(code, from_date, to_date)` — 목표주가(Adj.)·투자의견·괴리율·참여증권사 일별 컨센서스. Market Recognition Gap(기준③ Layer 5), Consensus Gate 판단(기준①②)에 직접 쓴다.
4. `mcp__fnspace__get_estimates(code, from_year, to_year)` — 추정실적(연간): 매출액·영업이익·순이익·EPS·BPS·ROE·P/E·P/B 컨센서스.
5. `mcp__fnspace__get_estimates_daily(code, from_date, to_date, from_year, to_year, quarterly=False)` — 추정실적 컨센서스가 날짜에 따라 어떻게 갱신되는지(Estimate Revision Momentum 계산에 사용).
6. `mcp__fnspace__get_forward_metrics(code, from_date, to_date)` — Fwd.12M 롤링 EPS/매출/영업이익/P/E. 특정 회계연도에 안 묶인 밸류에이션 참고치.
7. `mcp__fnspace__list_items(apigb)` — 항목 코드 카탈로그가 궁금할 때만(`A000002`=재무, `A000003`=목표주가, `A000004`=추정실적 연간, `A000005`=추정실적 일별, `A000006`=Fwd.12M).

각 도구 응답은 "요약 텍스트 + 원시 JSON"이 함께 온다 — 요약을 그대로 읽고, 정확한 수치가 필요하면 원시 JSON의 `dataset[].DATA[]`를 파싱한다.

## 출력
- `data/cache/<기업명>/fnguide.json` — 위 도구 호출 결과(요약 또는 파싱된 값)를 정리해 저장. 판단 스킬(`judge-*`, `screen-fundamentals`)이 참조할 원자료.
- 저장 형식 예: `{"target_price": {...}, "estimates": {...}, "forward_metrics": {...}, "financials": {...}, "fetched_at": "..."}`.

## 원칙
- **재배포 금지**: FnSpace 약관상 조회한 원시 데이터를 그대로 산출물에 옮겨 싣는 것은 금지다. 투심보고서에는 원자료에서 도출한 판단(비율·추세·괴리 여부 등)만 쓰고, 근시일 내 만료되는 임시 키 상황을 감안해 "FnGuide/FnSpace 컨센서스, 조회일자" 정도로만 출처 표기한다.
- 유료 도구(재무·컨센서스)가 키 만료·구독 문제로 실패하면 `mcp__fnspace__quickstart`로 원인(키 미설정/구독 만료/네트워크)을 먼저 진단하고, 실패 시 `data/cache/<기업명>/fnguide.json` 없이 넘어가되 그 사실을 보고서에 명시한다(`check-requirements`의 WARN 처리와 동일한 원칙 — 데이터 없음을 임의로 채우지 않는다).

## TODO
- [ ] 2026-08-15 임시 키 만료 전 팀 자체 FNSPACE_API_KEY 발급 후 `.env`(및 `claude mcp` 환경변수)에 반영
- [ ] 컨센서스 오차(Estimate Revision Momentum)를 `judge-structural-vs-cyclical`(Layer 3 시장 프레이밍)에서 어떻게 계량화할지 필드 설계
- [ ] `data/cache/<기업명>/fnguide.json` 저장 스키마를 실제 1~2개 기업으로 실행해 확정
