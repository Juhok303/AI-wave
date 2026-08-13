# Catalyst → Entry → Valuation → Return → Holding Period → Exit

## Catalyst Map

Gap이 아무리 커도 시장이 알아챌 계기가 없으면 투자 아이디어로 완성되지 않는다.

```
Leading Indicator(Love) → Catalyst Event → Estimate Revision → Market Recognition → Re-rating
```

후보 Catalyst: 재구매율/코호트 데이터 최초 공개, 가격 인상 성공(다음 분기 판매량 유지 확인),
마진 개선 첫 분기 실적발표, 신규 채널 성숙(Cohort 3), 애널리스트 커버리지 개시/상향.

각 Catalyst마다: 예상 시점 / 확인해야 할 데이터 / Earnings Impact를 표로 남긴다.

메모 표: `| Catalyst | Leading Indicator | 예상 시점 | Earnings Impact |`

## Entry Timing (4-category — 다른 두 기준 스킬과 동일 체계)

Never output a bare BUY/WATCH. 아래 중 정확히 하나를 고른다:

- **BUY NOW** — Conversion-Readiness Gap이 이미 크고(≥25%p) 축소 중이며, Catalyst가 가까움. 문서
  F절의 "3. Main Entry"(첫 분기 Consensus 상회 + Margin Beat, Revision 방향전환)에 해당.
- **BUY ON CONFIRMATION** — Thesis는 유효하나 핵심 데이터 1~2개(마진 전환의 지속성 등) 확인이 더
  필요함. F절의 "2. Early Entry"(2개 분기 연속 GM/ARPU YoY 개선 시작)에 해당.
- **BUY ON WEAKNESS** — Thesis는 강하지만 Market Recognition%ile이 이미 상당히 올라 밸류에이션
  부담이 있어 조정을 기다림. F절의 "4. Late Entry"(2개 분기 연속 Beat, 커버리지 증가, Multiple
  이미 상승)에 해당.
- **WAIT** — Gap이 아직 형성되지 않았거나(F절 "1. Watchlist") 이미 닫혔음(F절 "5. Fully Priced,
  EV/Sales %ile ≥ 75, Implied Growth ≈ 우리 추정, Gap ≈ 0").

무엇이 확인되면 진입할 것인지 구체적으로 명시한다.

## Valuation

가능하면 EV/Sales, EV/EBITDA 등 업종에 맞는 Multiple로: 현재 Multiple / 역사적 Range / Peer
Multiple을 비교한다. 시가총액은 `fetch-web`이 `data/cache/<기업명>/web.json`의 `market_data`
필드에 채워둔다(공식 API 아닌 웹 검색 기반 Medium Confidence — KRX 공식 API 승인 전까지의
잠정 소스). 그래도 확인이 안 되는 항목은 "Insufficient Data"로 명시한다.

핵심 질문: 우리가 찾은 Love→Conversion 전환이 현재 가격에 이미 반영돼 있는가?

## Expected Return

가능한 범위에서 분해: Fundamental Return(재무 전환에 따른) + Re-rating Return(Multiple 확장) =
Total. Bull/Base/Bear 시나리오로 제시하고, 데이터 부족 시 숫자를 지어내지 말고 "Insufficient
Data"라고 쓴다.

메모 표: `| Scenario | Financial Conversion 개선 가정 | Multiple 가정 | Expected Return |`

## Holding Period

기본 1~2년, Catalyst 예상 시차(위 Catalyst Map)의 합으로 기업별 개별 산정한다. 명시할 것:
Expected Holding Period / 첫 번째 Thesis Checkpoint / 두 번째 Thesis Checkpoint / 예상 Market
Recognition Window.

## Exit Rule (Thesis Break / Sell Discipline)

주가 하락만으로는 Thesis Break가 아니다 — Thesis를 구성하는 선행지표(Love·Durability) 자체의
손상 여부로만 판단한다.

| Exit 유형 | 정량 조건 |
| --- | --- |
| Successful Exit | Market Recognition Gap이 5%p 이내로 수렴 & EV/Sales %ile ≥ 65 |
| Thesis-break Exit | Layer1(Love) 또는 Layer2(Durability) %ile이 2개 분기 연속 20%p↑ 하락 |
| Time-stop Exit | Entry 후 6개 분기 경과해도 Operating Monetization Gap 미축소(오히려 확대) |

- **Confirmation Signal** — 예: Conversion-Readiness Gap 지속 축소, Durability 지표 유지
- **Weakening Signal** — 예: Love 지표 정체, 마진 전환 지연
- **Break Signal** — 예: Retention Decay Rate 급등, Red Flag 신규 발동
- **Sell Trigger** — Break Signal이 1회성이 아니라 2개 분기 연속 확인되는 경우
