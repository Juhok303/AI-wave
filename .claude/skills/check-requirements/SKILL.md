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
3. FnGuide/FnSpace는 현재 자동화 가능한 경로가 없어(2026-08-12 기준: 보유 계정은 컨센서스 이용권 없음, FnSpace는 별도 유료 가입 필요) 선택 항목으로 표시하고 안내만 출력한다.
4. 결과를 요약해서 출력한다: 항목별 OK/WARN/FAIL + 안내 메시지.

## 출력
- 콘솔 요약 (DART/FRED는 필수 — 하나라도 FAIL이면 종료 코드 1). FnGuide/FnSpace는 WARN이어도 파이프라인은 계속 진행 가능.

## 사용 시점
`investment-desk` 에이전트가 기업 판단을 시작하기 전 **가장 먼저** 이 스킬을 호출한다. DART/FRED 중 하나라도 FAIL이면, 나머지 파이프라인(fetch-dart 등)을 실행하지 않고 사용자에게 무엇을 `.env`에 채워야 하는지 안내한 뒤 중단한다.

## TODO
- [ ] FnSpace API 키를 실제로 발급받으면 `check_fnguide()`에 라이브 체크 추가
