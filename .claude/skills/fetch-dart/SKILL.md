---
name: fetch-dart
description: DART(전자공시시스템) 공시 데이터를 개별기업 기준으로 수집해 data/cache/에 저장한다. 투자 판단 파이프라인의 데이터 수집 단계 중 하나.
---

# fetch-dart

## 입력
- 기업명 또는 종목코드 1개

## 동작
1. `lib/dart_client.py`의 함수를 호출해 DART Open API에서 최근 사업보고서/분기보고서, 매출·원가·판매량 관련 공시 항목을 가져온다.
2. API 키는 `.env`의 `DART_API_KEY`를 사용한다.
3. 결과를 `data/cache/<기업명>/dart.json`에 저장한다.

## 출력
- `data/cache/<기업명>/dart.json` — 판단 스킬(judge-*)이 참조할 원자료.

## TODO
- [ ] `lib/dart_client.py`의 실제 API 호출 구현과 연결
- [ ] 어떤 공시 항목(매출, 판매량, ASP 등)을 어떤 필드명으로 저장할지 확정 — `judgment-rules.md`의 대체지표 정의와 맞출 것
