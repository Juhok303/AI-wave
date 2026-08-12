---
name: judge-structural-vs-cyclical
description: "Structural vs Cyclical Misclassification" 기준(시장이 구조적 성장을 경기순환적으로 오분류하는가)으로 개별기업을 판단한다. judgment-rules.md의 기준②를 실행하는 스킬.
---

# judge-structural-vs-cyclical

## 입력
- `data/cache/<기업명>/dart.json`, `data/cache/<기업명>/fnguide.json`, `data/cache/<기업명>/fred.json`
- `judgment-rules.md`의 "2. Structural vs Cyclical Misclassification" 섹션

## 동작

1. **실적 변동성 계산**: `dart.json`에서 확보 가능한 최근 3개년(당기/전기/전전기) `매출액`으로 변동계수를 계산한다.
   ```
   CV = stdev(매출액_3개년) / mean(매출액_3개년)
   ```
   업종 평균 CV를 구할 수 있는 데이터(fnguide.json의 업종 비교 등)가 있으면 함께 비교하고, 없으면 "자사 히스토리 기준"임을 명시하고 CV 절대 수준(예: 0.15 미만이면 낮은 변동성)으로만 판단한다.
2. **매크로 동행성 확인**: `fred.json`의 `series`(CPIAUCSL/FEDFUNDS/RSAFS/UNRATE)와 기업 매출액 YoY 추이를 나란히 놓고, 방향이 같이 움직이는 구간이 많은지(동행=cyclical 신호) 정성적으로 비교한다. 정량 상관계수 계산이 가능하면 계산하되, 표본이 적으면(연간 3개 포인트 등) 방향성 비교로 충분하다.
3. **컨센서스 방향성 오차 (fnguide.json 있는 경우만)**: 최근 분기 실적 vs 컨센서스의 상회/하회 방향과, 목표주가·투자의견 멀티플이 그 방향을 따라잡고 있는지 비교한다. fnguide.json이 없으면 이 단계는 생략하고 3번 없이 판단한다는 사실을 근거에 명시한다.
4. `judgment-rules.md` "2. Structural vs Cyclical Misclassification"의 판단 기준을 적용한다:
   - 매출 변동성 낮음 **AND** 매크로와의 동행성 약함 → 구조적 성장을 시장이 오분류 중일 가능성, **부합**
   - 매크로와 강한 동행 **AND** 변동성 큼 → 실제로 경기순환적, **미부합**
   - fnguide.json 부재 등으로 컨센서스 오차 확인 불가 → 실적 변동성·매크로 동행성만으로 잠정 판단하고 **부분부합**(데이터 제한을 근거에 명시)

## 출력
- 판단 결과(부합/부분부합/미부합) + 사용한 CV·매크로 비교 근거 + 데이터 제한 여부 + 적용한 `judgment-rules.md` 조항(기준② 판단 기준 중 어느 문장에 해당하는지) — investment-desk 에이전트가 최종 보고서에 통합. 이 문서에 없는 별도 기준으로 판단하지 않는다.

## 데이터 부족 시 처리
3개년 매출액이 모두 확보되지 않으면 CV를 계산하지 않고 "판단 보류(데이터 부족)"로 명시한다.
