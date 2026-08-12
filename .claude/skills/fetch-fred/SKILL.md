---
name: fetch-fred
description: FRED 매크로 지표(금리, 소비자물가, 소매판매 등)를 수집해 data/cache/에 저장한다. 투자 판단 파이프라인의 데이터 수집 단계 중 하나.
---

# fetch-fred

## 입력
- (선택) 시리즈 ID 목록. 없으면 기본 지표 세트(`lib/fred_client.py`의 `DEFAULT_SERIES`)를 사용.

## 동작
1. `python lib/fred_client.py [series_id ...]`를 실행한다(또는 `get_macro_series(series_ids=None)`을 직접 호출). `requirements.txt`의 패키지가 필요하다.
2. 기본 지표: `CPIAUCSL`(소비자물가지수), `FEDFUNDS`(기준금리), `RSAFS`(소매판매), `UNRATE`(실업률) — 최근 24개월 관측치.
3. API 키는 `.env`의 `FRED_API_KEY`를 사용한다.
4. 결과를 `data/cache/<기업명>/fred.json`에 저장한다.

## 출력
- `data/cache/<기업명>/fred.json` — `{series: {series_id: [{date, value}, ...]}}`. structural-vs-cyclical 판단 스킬이 참조할 원자료.

## TODO
- [ ] 업종별로 더 관련성 높은 시리즈(예: Beauty→개인소비지출, Consumer Subscription→가처분소득)를 기본 세트에 추가할지 검토
