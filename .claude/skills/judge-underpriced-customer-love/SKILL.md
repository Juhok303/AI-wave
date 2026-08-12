---
name: judge-underpriced-customer-love
description: "Underpriced Customer Love (ULRS)" 기준(진짜 애착 + 재무 전환 능력 + 시장 미인식 Gap)으로 개별기업을 판단한다. judgment-rules.md의 기준③을 실행하는 스킬. 상세 방법론은 docs/underpriced-customer-love-framework.md 참조.
---

# judge-underpriced-customer-love

## 입력
- `data/cache/<기업명>/dart.json`, `data/cache/<기업명>/fnguide.json`, `data/cache/<기업명>/web.json`(리뷰·뉴스 등 Proxy 원자료)
- `judgment-rules.md`의 "3. Underpriced Customer Love (ULRS)" 섹션
- `docs/underpriced-customer-love-framework.md` (Layer별 지표 정의, Red Flag 10종, Sector Fit)

## 동작
1. Love%ile — 재구매율, 리뷰 볼륨 증가율, DAU/MAU, 브랜드 검색점유율 변화를 수집한다(`web.json`의 리뷰·검색량·앱 데이터는 DART/FnGuide 밖 Proxy이므로 신뢰도에 따라 0.6~1.0x 할인).
2. Durability%ile — Retention Decay Rate, Switching Cost, 신규 진입자 침투 속도를 판단한다.
3. Conversion_Readiness_Gap — DART/FnGuide 원자료로 Financial Conversion Capacity(LTV/CAC, FCF Conversion 등)와 Market Recognition(Estimate Revision, EV/Sales Percentile)을 각각 산출해 Gap을 계산한다.
4. `docs/underpriced-customer-love-framework.md`의 H절 Red Flag 10종을 점검해 Risk_Penalty%를 산출한다. Red Flag 2개 이상이면 즉시 Avoid로 판정하고 나머지 계산은 생략해도 된다.
5. `ULRS = √(Love%ile × Durability%ile) × Conversion_Readiness_Gap × (1 − Risk_Penalty%)`를 계산한다.
6. 데이터가 없는 지표는 중립(50점)으로 채우지 말고, 해당 weight를 제외한 뒤 나머지 weight로 재정규화한다.

## 출력
- ULRS 값 + 해석(ULRS>0 매수 구간 / ≈0 Watchlist / <0 Avoid) + 핵심 근거(Love/Durability/Gap/Red Flag 요약).

## Peer Group 정의 (실전 축소판)

이 레포는 GICS Sub-industry 분류 DB나 업종별 상장사 유니버스 조회 API를 갖고 있지 않다. 따라서 `docs/underpriced-customer-love-framework.md` E절의 3중 필터를 아래처럼 기존 스킬 조합으로 근사한다:

1. `fetch-web`의 "`<기업명>` 경쟁사 OR 신규 브랜드" 검색 결과에서 실제로 언급되는 동종업계 상장사 이름을 5~10개 추린다(비상장 언급은 제외).
2. 그 후보들 각각에 대해 `fetch-dart`(`get_company_filings`)를 호출해 매출액을 가져온다.
3. 대상 기업 매출액의 **0.3배~3배** 범위에 드는 회사만 최종 Peer Group으로 채택한다.
4. Peer Group이 5개 미만이면 Percentile Rank 대신 "Peer 대비 상/중/하" 3단계 정성 평가로 대체하고, 그 사실(표본 부족)을 근거에 명시한다. 5개 이상이면 Percentile Rank를 계산하고, 20개 미만이면 z-score를 보조로 병기한다(문서 E절 원칙).
5. Peer Group을 구성하지 못하면(경쟁사 정보 자체가 없음) 절대 기준(예: LTV/CAC 등 문서 K절의 Red Flag 임계값)만으로 판단하고 Percentile 기반 항목은 "판단 보류"로 표시한다.
