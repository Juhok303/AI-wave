---
name: fetch-fred
description: FRED 매크로 지표(금리, 소비자물가, 소매판매 등)를 수집해 data/cache/에 저장한다. 투자 판단 파이프라인의 데이터 수집 단계 중 하나.
---

# fetch-fred

## 입력
- (선택) 기업의 섹터/업종에 관련된 매크로 지표 목록. 없으면 기본 지표 세트를 사용.

## 동작
1. `lib/fred_client.py`의 함수를 호출해 FRED API에서 관련 매크로 시계열을 가져온다.
2. API 키는 `.env`의 `FRED_API_KEY`를 사용한다.
3. 결과를 `data/cache/<기업명>/fred.json`에 저장한다.

## 출력
- `data/cache/<기업명>/fred.json` — structural-vs-cyclical 판단 스킬이 참조할 원자료.

## TODO
- [ ] `lib/fred_client.py`의 실제 API 호출 구현
- [ ] 기본으로 가져올 매크로 지표 목록 확정 (예: CPI, 기준금리, 소매판매지수)
