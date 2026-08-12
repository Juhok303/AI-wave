---
name: judge-distribution-compounding
description: "Distribution Compounding" 기준(유통·채널 확장을 통한 복리적 성장인가)으로 개별기업을 판단한다. judgment-rules.md의 기준③을 실행하는 스킬.
---

# judge-distribution-compounding

## 입력
- `data/cache/<기업명>/dart.json`
- `judgment-rules.md`의 "3. Distribution Compounding" 섹션

## 동작
1. 사업보고서 공시에서 채널/매장/카테고리 확장 추이를 추출한다.
2. `judgment-rules.md`에 정의된 대체지표 기준으로 채널 확장이 복리적 성장으로 이어지는지 판단한다.

## 출력
- 판단 결과(부합/부분부합/미부합) + 근거 요약.

## TODO
- [ ] `judgment-rules.md`의 대체지표 정의가 확정되면 그에 맞춰 판단 로직 구체화
