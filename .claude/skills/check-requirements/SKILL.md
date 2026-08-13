---
name: check-requirements
description: 판단을 시작하기 전, 필요한 API 키/로그인 정보가 .env에 있고 실제로 동작하는지(라이브 체크) 확인한다. investment-desk가 가장 먼저 호출해야 하는 스킬. "이 레포 처음 세팅하는데 뭐가 필요해?" 같은 요청에도 사용.
---

# check-requirements

## 입력
- 없음 (`.env`를 읽는다)

## 동작
1. `python lib/check_requirements.py`를 실행한다(`requirements.txt` 설치 필요).
2. DART_API_KEY, FRED_API_KEY는 값이 있는지뿐 아니라 실제 API를 호출해 라이브로 동작하는지까지 확인한다(단순 "키가 채워져 있다"가 아니라 "실제로 이 키로 데이터를 가져올 수 있다"를 확인).
3. FnGuide는 이제 `fnspace-mcp` MCP 플러그인(`mcp__fnspace__*` 도구)이 실제 경로다(2026-08-13 갱신). 이 Python 스크립트는 Claude Code 세션 밖에서 돌기 때문에 MCP 연결 상태를 직접 확인할 수 없다 — `check_fnguide()`는 항상 WARN을 내며, 대신 `claude mcp list`로 `plugin:fnspace:fnspace`가 Connected인지, 세션 안에서 `mcp__fnspace__quickstart` 결과가 정상인지 확인하라고 안내한다. 참고로 현재는 동봉된 임시 공유 키로 동작 중이며 **2026-08-15 만료** — 그 이후엔 팀 자체 `FNSPACE_API_KEY`가 필요하다.
4. 결과를 요약해서 출력한다: 항목별 OK/WARN/FAIL + 안내 메시지.

## 출력
- 콘솔 요약 (DART/FRED는 필수 — 하나라도 FAIL이면 종료 코드 1). FnGuide/FnSpace는 WARN이어도 파이프라인은 계속 진행 가능.

## 사용 시점
`investment-desk` 에이전트가 기업 판단을 시작하기 전 **가장 먼저** 이 스킬을 호출한다. DART/FRED 중 하나라도 FAIL이면, 나머지 파이프라인(fetch-dart 등)을 실행하지 않고 사용자에게 무엇을 `.env`에 채워야 하는지 안내한 뒤 중단한다.

## TODO
- [ ] FnSpace API 키를 실제로 발급받으면 `check_fnguide()`에 FnSpace용 라이브 체크 추가
