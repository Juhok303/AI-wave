---
name: fetch-dart
description: DART(전자공시시스템) 공시 데이터를 개별기업 기준으로 수집해 data/cache/에 저장한다. 투자 판단 파이프라인의 데이터 수집 단계 중 하나.
---

# fetch-dart

## 입력
- 기업명 또는 종목코드 1개

## 동작
1. `python lib/dart_client.py "<기업명>"`을 실행한다(또는 `get_company_filings(company_name)`을 직접 호출). `requirements.txt`의 패키지가 필요하다(`pip install -r requirements.txt`).
2. 내부적으로 corp_code 마스터 목록(`data/cache/dart_corp_codes.json`, 최초 1회 다운로드 후 캐싱)에서 기업명을 corp_code로 변환하고, 최근 사업보고서(연간)의 손익계산서(매출액/매출원가/매출총이익/영업이익, 당기·전기·전전기)와 최근 1년 공시 목록을 가져온다.
3. API 키는 `.env`의 `DART_API_KEY`를 사용한다.
4. 결과를 `data/cache/<기업명>/dart.json`에 저장한다.

## 출력
- `data/cache/<기업명>/dart.json` — `corp_code`, `income_statement`(계정별 당기/전기/전전기 금액), `recent_disclosures`를 담은 JSON. 판단 스킬(judge-*)이 참조할 원자료.

## TODO
- [ ] 판매량/ASP처럼 손익계산서에 직접 없는 지표는 사업보고서 본문(사업의 내용) 파싱이 추가로 필요 — 현재는 재무제표 계정과목만 구현됨
- [ ] 반기/분기 데이터가 필요하면 `lib/dart_client.py`의 `ANNUAL_REPORT_CODE`를 상황에 맞는 reprt_code로 교체
