---
name: judge-structural-vs-cyclical
description: "Structural vs Cyclical Misclassification" 기준(시장이 구조적 성장을 경기순환적으로 오분류하는가)으로 개별기업을 판단한다. judgment-rules.md의 기준②를 실행하는 스킬.
---

# judge-structural-vs-cyclical

## 입력
- `data/cache/<기업명>/dart.json`, `data/cache/<기업명>/fnguide.json`, `data/cache/<기업명>/fred.json`
- `judgment-rules.md`의 "2. Structural vs Cyclical Misclassification" 섹션

## 동작
1. 기업 실적 추이를 업종 평균/매크로 지표(FRED) 흐름과 비교한다.
2. 컨센서스(FnGuide) 추정치의 방향성이 실제와 얼마나 어긋나는지를 오분류 신호로 본다.
3. `judgment-rules.md`에 정의된 대체지표 기준으로 구조적/경기순환적 여부를 판단한다.

## 출력
- 판단 결과(구조적 성장으로 판단 / 경기순환으로 판단 / 판단 보류) + 근거 요약.

## TODO
- [ ] `judgment-rules.md`의 대체지표 정의가 확정되면 그에 맞춰 판단 로직 구체화
