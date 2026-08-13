---
name: fetch-dart
description: DART(전자공시시스템) 공시 데이터를 개별기업 기준으로 수집해 data/cache/에 저장한다. 투자 판단 파이프라인의 데이터 수집 단계 중 하나.
---

# fetch-dart

## 입력
- 기업명 또는 종목코드 1개

## 동작
1. `python lib/dart_client.py "<기업명>"`을 실행한다(또는 `get_company_filings(company_name)`을 직접 호출). `requirements.txt`의 패키지가 필요하다(`pip install -r requirements.txt`).
2. 내부적으로 corp_code 마스터 목록(`data/cache/dart_corp_codes.json`, 최초 1회 다운로드 후 캐싱)에서 기업명을 corp_code로 변환하고, 최근 사업보고서(연간)의 손익계산서(매출액/매출원가/매출총이익/영업이익/이자비용)와 재무상태표(자산총계/부채총계/자본총계/유동자산/유동부채) 핵심 계정을 당기·전기·전전기 금액으로, 그리고 최근 1년 공시 목록을 가져온다. 손익계산서와 재무상태표 모두 동일한 API 호출(`fnlttSinglAcntAll.json`) 응답 하나에서 추출하므로 추가 호출은 없다. 이자비용은 회사마다 "이자비용"/"금융원가" 등 계정명이 달라(K-IFRS는 계정명을 표준화하지 않음) `ACCOUNT_SYNONYMS`로 동의어를 함께 찾아 `income_statement.이자비용`으로 통일해 저장한다.
3. API 키는 `.env`의 `DART_API_KEY`를 사용한다.
4. 결과를 `data/cache/<기업명>/dart.json`에 저장한다.

## 출력
- `data/cache/<기업명>/dart.json` — `corp_code`, `income_statement`(계정별 당기/전기/전전기 금액), `balance_sheet`(동일 구조), `recent_disclosures`를 담은 JSON. 판단 스킬(judge-*)과 `screen-fundamentals`가 참조할 원자료.

## TODO
- [x] 이자비용 계정명 동의어 매칭(이자비용/금융원가 등) + IS/CIS 조회로 수정 (2026-08-12, 삼성전자·BGF리테일 회귀 테스트 완료)
- [x] 영업이익 계정명 동의어 매칭("영업이익(손실)" 등) 추가 (2026-08-12, 현대백화점 실행 중 결측 발견 후 수정, 재실행으로 확인 완료)
- [ ] 판매량/ASP처럼 재무제표에 직접 없는 지표는 사업보고서 본문(사업의 내용) 파싱이 추가로 필요 — 현재는 재무제표 계정과목만 구현됨
- [ ] 반기/분기 데이터가 필요하면 `lib/dart_client.py`의 `ANNUAL_REPORT_CODE`를 상황에 맞는 reprt_code로 교체
- [ ] 동의어 매칭에도 `이자비용`이 본문 계정에 아예 없는 기업이 있을 수 있다 — 필요하면 XBRL 상세 재무제표 API(`fnlttXbrl`) 등 대체 소스 검토
