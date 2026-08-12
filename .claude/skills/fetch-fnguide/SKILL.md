---
name: fetch-fnguide
description: FnGuide 컨센서스 데이터(추정 실적, ASP 등)를 개별기업 기준으로 수집해 data/cache/에 저장한다. 투자 판단 파이프라인의 데이터 수집 단계 중 하나.
---

# fetch-fnguide

## 입력
- 기업명 또는 종목코드 1개

## 동작
1. `lib/fnguide_client.py`의 함수를 호출해 FnGuide 컨센서스(매출/이익 추정치, 추정 ASP, 목표주가 등)를 가져온다.
2. 접근 키/계정 정보는 `.env`의 `FNGUIDE_API_KEY`를 사용한다.
3. 결과를 `data/cache/<기업명>/fnguide.json`에 저장한다.

## 출력
- `data/cache/<기업명>/fnguide.json` — 판단 스킬(judge-*)이 참조할 원자료.

## TODO
- [ ] `lib/fnguide_client.py`의 실제 접근 방식(API/스크래핑) 확정 및 구현
- [ ] 컨센서스 오차(실제 vs 추정)를 structural-vs-cyclical 판단에서 어떻게 쓸지 필드 설계
