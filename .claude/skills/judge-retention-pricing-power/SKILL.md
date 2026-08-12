---
name: judge-retention-pricing-power
description: "Retention-to-Pricing-Power" 기준(가격 인상에도 이탈하지 않는가 + 그 가격결정력이 재무 전환되고 있는가 + 시장이 이미 다 아는 스토리는 아닌가)으로 개별기업을 판단한다. judgment-rules.md의 기준①을 실행하는 스킬. 잠정 버전(pjueun 정식 설계문서 도착 전) — retention-pricing-power-memo/assets/example-memo-costco.html에서 역추출.
---

# judge-retention-pricing-power

## 입력
- `data/cache/<기업명>/dart.json`, `data/cache/<기업명>/web.json`, `data/cache/<기업명>/fnguide.json`(있는 경우)
- `judgment-rules.md`의 "1. Retention-to-Pricing-Power" 섹션
- 참고: `.claude/skills/retention-pricing-power-memo/assets/example-memo-costco.html` (pjueun, 이 판단 로직의 원본 예시)

## 동작

1. **가격 인상 이벤트 확인 (web.json)**: 최근 2~3년 내 가격 인상 발표가 있었는지 검색 결과에서 찾는다. 있으면 그 시점을 기록.
2. **Retention 방어 확인 (dart.json)**: 가격 인상 전후 매출액 YoY·매출총이익률 변화를 비교한다. 가격 인상 이벤트를 특정하지 못했으면 최근 2개년 매출액 YoY로 대체 판단(그 사실을 명시).
3. **재무 전환 여부 (dart.json)**: 매출총이익률·영업이익률의 YoY 추이를 본다. 마진이 유지·개선 중이면 가격결정력이 재무로 전환되고 있다는 신호, 아직 정체면 "전환 안 됨"으로 기록.
4. **Consensus Gate 점검 (web.json, Low Confidence)**: "가격결정력/충성도/멤버십" 관련 언급이 이미 여러 언론·리포트에서 반복되는 컨센서스 스토리인지 확인한다. 반복 언급이 많으면 Variant View 약화로 판단.
5. **밸류에이션 참고 (fnguide.json, 있는 경우)**: 현재 Multiple이 역사적 평균 대비 프리미엄인지 참고만 한다(판단 기준 자체는 아래 3단계 규칙만 사용).
6. `judgment-rules.md` "1. Retention-to-Pricing-Power"의 판단 기준을 그대로 적용한다:
   - Retention 방어 확인 **AND** 마진 전이가 아직 시장에 다 반영 안 된 개선 초기 신호 → **부합**
   - Retention 확인되나 이미 컨센서스에 충분히 반영(Consensus Gate 발동) 또는 마진 정체 → **부분부합**
   - 가격 인상 후 매출·판매량이 뚜렷이 이탈 → **미부합**

## 출력
- 판단 결과(부합/부분부합/미부합) + 사용한 수치(매출총이익률·영업이익률 YoY, 가격 인상 이벤트 유무)와 근거 + Consensus Gate 점검 결과 + 적용한 `judgment-rules.md` 조항 — investment-desk 에이전트가 최종 보고서에 통합. 이 문서에 없는 별도 기준으로 판단하지 않는다.

## 데이터 부족 시 처리
`dart.json`에 매출총이익률 계산에 필요한 계정이 없으면 그 사실을 명시하고 "판단 보류(데이터 부족)"로 표시한다. `web.json`에 가격 인상 이벤트 정보가 없으면 Retention 방어 판단은 "가격 인상 이벤트 특정 불가, 매출 YoY로 대체 판단"임을 근거에 명시한다. 임의로 부합/미부합을 추정하지 않는다.

## TODO
- [ ] pjueun의 정식 SKILL.md/설계문서가 도착하면 이 스킬과 `judgment-rules.md` 기준① 섹션을 함께 재검토
