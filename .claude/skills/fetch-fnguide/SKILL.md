---
name: fetch-fnguide
description: FnGuide 컨센서스 데이터(추정 실적, ASP 등)를 개별기업 기준으로 수집해 data/cache/에 저장한다. 투자 판단 파이프라인의 데이터 수집 단계 중 하나. 현재 이용 가능한 자격 증명이 없으면 건너뛴다(check-requirements 참고).
---

# fetch-fnguide

## 현재 상태 (2026-08-12 점검)
- FnGuide 컨센서스 웹 서비스(www.fnguide.com)는 로그인 방식이지만, 보유 계정에 컨센서스 이용권이 없어 데이터 조회가 불가능함을 실제 로그인 테스트로 확인했다.
- FnGuide 공식 API는 **fnspace.com(FnSpace)**를 통해 별도 유료 가입으로 제공된다(컨센서스·재무·경제지표 포함). 스크래핑보다 이쪽이 정식 경로다.
- 따라서 `check-requirements`에서 `FNSPACE_API_KEY`가 확인되기 전까지 이 스킬은 **건너뛴다**.

## 입력
- 기업명 또는 종목코드 1개

## 동작 (FNSPACE_API_KEY 확보 후)
1. `lib/fnguide_client.py`의 함수를 호출해 FnSpace API로 컨센서스(매출/이익 추정치, 추정 ASP, 목표주가 등)를 가져온다.
2. API 키는 `.env`의 `FNSPACE_API_KEY`를 사용한다.
3. 결과를 `data/cache/<기업명>/fnguide.json`에 저장한다.

## 출력
- `data/cache/<기업명>/fnguide.json` — 판단 스킬(judge-*)이 참조할 원자료.

## TODO
- [ ] FNSPACE_API_KEY 발급 후 실제 엔드포인트/응답 구조 확인하고 `lib/fnguide_client.py` 구현 (DART/FRED 클라이언트와 동일하게 실제 API로 검증)
- [ ] 컨센서스 오차(실제 vs 추정)를 structural-vs-cyclical 판단에서 어떻게 쓸지 필드 설계
