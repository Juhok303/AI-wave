---
name: fetch-fnguide
description: FnGuide 컨센서스 데이터(추정 실적, ASP 등)를 개별기업 기준으로 수집해 data/cache/에 저장한다. 투자 판단 파이프라인의 데이터 수집 단계 중 하나. 현재 이용 가능한 자격 증명이 없으면 건너뛴다(check-requirements 참고).
---

# fetch-fnguide

## 현재 상태 (2026-08-12 점검)
- `lib/fnguide_client.py`의 `login()`으로 **브라우저 없이** (requests 세션 + RSA-OAEP 암호화 비밀번호) www.fnguide.com 로그인이 가능함을 확인했다 — 로그인 자체는 성공한다.
- 하지만 컨센서스 서비스(`/Consensus/*`)는 로그인 여부와 무관하게 **보유 계정에 이용권이 없어** 여전히 조회가 불가능함을 `has_consensus_entitlement()`로 라이브 확인했다. 즉 막힌 지점은 "브라우저가 필요해서"가 아니라 계정 자체의 서비스 이용권 부재다.
- FnGuide 공식 API는 **fnspace.com(FnSpace)**를 통해 별도 유료 가입으로 제공된다(컨센서스·재무·경제지표 포함). 이용권을 구매하거나 FnSpace로 전환하기 전까지는 어느 접근 방식(브라우저든 requests든)으로도 컨센서스 데이터를 가져올 수 없다.
- 따라서 `check-requirements`에서 이용권 보유(또는 `FNSPACE_API_KEY`)가 확인되기 전까지 이 스킬은 **건너뛴다**.

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
- [ ] (이용권을 구매하게 될 경우) `login()`이 반환하는 인증 세션으로 `/Consensus/Stock` 등 실제 페이지를 파싱하는 스크래핑 경로도 대안으로 검토 가능 — 다만 정식 API(FnSpace)가 우선
