---
name: judge-structural-vs-cyclical
description: "Structural vs Cyclical Misclassification" 기준(시장이 구조적 성장을 경기순환적으로 오분류하는가)으로 개별기업을 판단한다. judgment-rules.md의 기준②를 실행하는 스킬. chaemin의 thesis-tree.md(Source of truth)를 이 파이프라인 데이터로 근사한 축약판.
---

# judge-structural-vs-cyclical

## 입력
- `data/cache/<기업명>/dart.json`, `data/cache/<기업명>/fred.json`, `data/cache/<기업명>/web.json`, `data/cache/<기업명>/fnguide.json`(있는 경우)
- `judgment-rules.md`의 "2. Structural vs Cyclical Misclassification" 섹션
- Source of truth: `.claude/skills/structural-cyclical-misclassification-memo/references/thesis-tree.md` (chaemin) — Layer/Factor 전체 정의, 재가중 테이블, Gate 조건은 이 문서를 따른다.

## 동작

1. **Layer 1 구조적 신호 (dart.json + web.json)**:
   - `dart.json`에서 확보 가능한 최근 3개년(당기/전기/전전기) `매출액`으로 변동계수를 계산한다.
     ```
     CV = stdev(매출액_3개년) / mean(매출액_3개년)
     ```
     업종 평균 CV를 비교할 데이터가 없으면 "자사 히스토리 기준"임을 명시하고 절대 수준(0.15 미만이면 낮은 변동성)으로 판단한다.
   - `web.json`에서 이 기업의 성장 동인이 기술/제도 변화처럼 영구적인 성격인지, 유행성(SNS 트렌드 등)에 가까운지 확인한다.
2. **Layer 2 경기 오염 테스트 (dart.json + fred.json)**: `fred.json`의 `series`(CPIAUCSL/FEDFUNDS/RSAFS/UNRATE)와 매출액 YoY 추이가 같이 움직이는 구간이 많은지(동행=cyclical 신호) 정성적으로 비교한다. thesis-tree.md의 원칙대로 — 반증을 실제로 시도할 것(Bear case를 Bull case와 동등하게 조사), 상장 이력이 짧아 경기 하방 데이터가 없으면 "Insufficient Data"로 표기하고 낙관적으로 채점하지 않는다.
3. **Layer 3 시장의 프레이밍 (web.json + fnguide.json)**: "이 기업이 구조적 성장이냐 경기순환이냐" 논쟁이 이미 언론·실적콜에서 활발히 다뤄지는지 검색한다. 이미 반복적으로 논의되는 논쟁이면 진짜 Variant View가 아니라 이미 컨센서스에 편입된 논쟁일 가능성이 높다(thesis-tree.md 3-2절, Consensus Gate 위험).
4. `judgment-rules.md` "2. Structural vs Cyclical Misclassification"의 판단 기준을 적용한다:
   - 매출 변동성 낮음 **AND** 매크로 동행성 약함 **AND** 시장 논쟁이 아직 활발하지 않음 → **부합**
   - 매출 변동성은 낮으나 시장 논쟁이 이미 활발함(Consensus Gate 발동 우려) → **부분부합**
   - 매크로와 강한 동행 **AND** 변동성 큼 → **미부합**

## 출력
- 판단 결과(부합/부분부합/미부합) + 사용한 CV·매크로 비교·Consensus Gate 점검 근거 + 데이터 제한 여부 + 적용한 `judgment-rules.md` 조항 — investment-desk 에이전트가 최종 보고서에 통합. 이 문서와 thesis-tree.md에 없는 별도 기준으로 판단하지 않는다.

## 데이터 부족 시 처리
3개년 매출액이 모두 확보되지 않으면 CV를 계산하지 않고 "판단 보류(데이터 부족)"로 명시한다.
