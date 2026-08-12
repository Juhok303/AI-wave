---
name: judge-underpriced-customer-love
description: "Underpriced Customer Love (ULRS)" 기준(진짜 애착 + 재무 전환 능력 + 시장 미인식 Gap)으로 개별기업을 판단한다. judgment-rules.md의 기준③을 실행하는 스킬. 상세 방법론은 docs/underpriced-customer-love-framework.md 참조.
---

# judge-underpriced-customer-love

## 입력
- `data/cache/<기업명>/dart.json`, `data/cache/<기업명>/fnguide.json`
- `judgment-rules.md`의 "3. Underpriced Customer Love (ULRS)" 섹션
- `docs/underpriced-customer-love-framework.md` (Layer별 지표 정의, Red Flag 10종, Sector Fit)

## 동작
1. Love%ile — 재구매율, 리뷰 볼륨 증가율, DAU/MAU, 브랜드 검색점유율 변화를 수집한다(대부분 DART/FnGuide 밖의 리뷰·검색량·앱 데이터이므로 Proxy로 표시하고 신뢰도에 따라 0.6~1.0x 할인).
2. Durability%ile — Retention Decay Rate, Switching Cost, 신규 진입자 침투 속도를 판단한다.
3. Conversion_Readiness_Gap — DART/FnGuide 원자료로 Financial Conversion Capacity(LTV/CAC, FCF Conversion 등)와 Market Recognition(Estimate Revision, EV/Sales Percentile)을 각각 산출해 Gap을 계산한다.
4. `docs/underpriced-customer-love-framework.md`의 H절 Red Flag 10종을 점검해 Risk_Penalty%를 산출한다. Red Flag 2개 이상이면 즉시 Avoid로 판정하고 나머지 계산은 생략해도 된다.
5. `ULRS = √(Love%ile × Durability%ile) × Conversion_Readiness_Gap × (1 − Risk_Penalty%)`를 계산한다.
6. 데이터가 없는 지표는 중립(50점)으로 채우지 말고, 해당 weight를 제외한 뒤 나머지 weight로 재정규화한다.

## 출력
- ULRS 값 + 해석(ULRS>0 매수 구간 / ≈0 Watchlist / <0 Avoid) + 핵심 근거(Love/Durability/Gap/Red Flag 요약).

## TODO
- [ ] 리뷰·검색량·앱 데이터 등 데이터 키트(DART/FnGuide/FRED) 밖의 Proxy 데이터 소스 확정
- [ ] Peer Group 정의(동일 GICS Sub-industry + 매출 0.3~3x + 유통채널 유사성) 구현
