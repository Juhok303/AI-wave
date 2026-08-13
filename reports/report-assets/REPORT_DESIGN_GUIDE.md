# 리포트 디자인 시스템 사용 가이드

레포에서의 위치: `reports/report-assets/design-system.css` (이 파일 옆의
`design-system.css`).

**2026-08-13 수정**: 처음 버전은 모든 리포트가 이 CSS를 `<link>`로
외부 참조하고 Google Fonts/jsdelivr CDN에서 폰트를 받아오는 구조였다.
`judgment-rules.md`의 "HTML 단일 파일" 원칙(배포된 리포트는 그 자체로
완전해야 한다 — 외부 CSS 파일이나 인터넷 연결에 의존하면 안 됨)과
충돌해서, **리포트 생성 시점에 이 CSS 전체를 각 리포트의 `<style>`
블록에 인라인으로 복사해 넣는 방식**으로 바꿨다. 폰트도 CDN 대신 OS
기본 폰트 스택(`design-system.css` 상단 주석 참고)으로 바꿨다.

## 왜 이렇게 하나

리포트 HTML은 매번 Claude(스킬)가 새로 작성한다. 스타일까지 매번
새로 작성하게 두면 리포트마다 톤이 미묘하게 달라진다. 대신 **CSS는
정본 파일 하나(`reports/report-assets/design-system.css`)로 박아두고,
스킬에게는 "리포트를 생성할 때 이 파일 내용을 그대로 `<style>`에
복사해넣고, 정해진 클래스만 써라"라고 지시**한다. 그러면:

- 어떤 기업/프레임워크든 같은 톤으로 나온다
- 디자인을 바꾸고 싶으면 정본 `design-system.css` 한 곳만 고치면 된다
  (단, **소급 적용은 안 된다** — 이미 생성된 리포트는 이미 자기 복사본을
  갖고 있어 그대로 남는다. 그 리포트만 다시 생성해야 갱신됨)
- LLM이 매번 색상/폰트를 창작하지 않아도 되니 토큰도 아낀다
- 그러면서도 리포트 파일 하나하나는 여전히 외부 의존성 없는 단일 파일이다

## 스킬에 추가해야 할 지시문

`investment-desk` 오케스트레이터의 SKILL.md/시스템 프롬프트에 아래
문단을 그대로 추가한다(`.claude/agents/investment-desk.md`의 "UI/UX"
절에 이미 반영돼 있음):

```
최종 HTML 리포트를 작성할 때는 반드시 아래를 지킨다:

1. `reports/report-assets/design-system.css` 파일 전체를 읽어, 그 내용을
   리포트 HTML의 <style> 블록 안에 그대로(수정 없이) 복사해 넣는다.
   외부 <link rel="stylesheet">나 Google Fonts/jsdelivr 같은 CDN은
   추가하지 않는다 — 리포트는 인터넷 연결 없이도 그 자체로 완전해야
   한다(judgment-rules.md "HTML 단일 파일" 원칙).

2. design-system.css에 이미 정의된 클래스만 사용한다.
   새로운 색상 hex 값이나 폰트를 직접 추가하지 않는다.
   (이 문서의 "컴포넌트 카탈로그" 참고)

3. 판정/상태 표시는 항상 buy(초록,긍정)/watch(호박,관찰·부분)/
   avoid(빨강,부정)/na(회색,해당없음) 4색 의미체계를 따른다.

4. 구조는 항상: <div class="sheet"> 안에
   .hero (좌: 텍스트, 우: .term 스냅샷 패널) →
   .stat-strip (핵심 지표 4개) →
   <section> 반복 (판단기준/스크리닝/재무/최종의견 등, 프레임워크에 맞게 구성) →
   footer
   순서를 따른다. 상단 네비게이션 바는 넣지 않는다.

5. 히어로의 .term 패널은 .term-kv 포맷(라벨-값, 문법기호 없음)만 쓴다.
   JSON 문법({}, "", : ,)을 그대로 노출하지 않는다.

6. 근거가 되는 세부 표(Test/Layer 분석처럼 밀도 높은 표)는 <details>로
   기본적으로 접어두고, 결론 문장과 배지만 먼저 보이게 한다.
```

## 컴포넌트 카탈로그 (design-system.css에 이미 정의됨)

| 용도 | 클래스 |
|---|---|
| 히어로 전체 | `.hero`, `.eyebrow`, `.headline`, `.chips` / `.chip`, `.verdict-pill` |
| 다크 코드 패널 | `.term`, `.term-bar`, `.term-dot`, `.term-label`, `.term-body`, `.term-kv` |
| 근거용 다크 표 | `.term-table` |
| 핵심 지표 4칸 | `.stat-strip`, `.stat-cell` |
| 섹션 공통 | `section`, `.sec-eyebrow` / `.sec-head` + `.sec-num`, `h2`, `.card` |
| 넘버링 판단 카드 | `.gate`, `.gate-head`, `.gate-num`, `.gate-body` |
| 판정 배지 | `.badge` (카드용), `.flag` (체크리스트용), `.tag` (표 셀용), `.status` |
| 스크리닝 체크리스트 | `.screen-card`, `.screen-row` |
| Variant Perception류 4카드 | `.vp-grid`, `.vp-card` |
| Q&A / 최종 판단 | `.qa`, `.verdict-box`, `.final` |
| 표 | `table` (기본), `.fin-table` (재무제표 카드형) |
| 접기/펼치기 | `details` / `summary` |
| 출처/푸터 | `.sources`, `footer` |

새 프레임워크(예: 4번째 judge-* 스킬)를 추가할 때 기존 컴포넌트로
표현이 안 되는 구조가 나오면, **design-system.css에 새 컴포넌트를
추가**하고 이 표에도 한 줄 추가한다 — 개별 리포트의 `<style>`에
임시로 박아넣지 않는다.

## 현재 상태 (2026-08-13)

- `reports/report-assets/design-system.css`가 정본이다. `investment-desk.md`의
  "UI/UX" 절이 이 파일을 읽어 `<style>`에 인라인하도록 이미 지시하고 있다.
- `reports/preview-check/`의 삼성전자/Costco 예시는 원래 `<link>` 참조 방식으로
  만들어진 초기 프로토타입이라 그대로 남아있다(상대경로만 `../report-assets/...`로
  보정) — 실제 파이프라인 산출물 규격은 아니고 디자인 참고용이다.
- 다음 리포트부터는 스킬이 이 CSS 전체를 복사해 넣으므로 자동으로 같은 톤이
  적용된다. 디자인을 바꾸려면 이 파일만 고치면 되지만, **이미 생성된 리포트에는
  소급 적용되지 않는다**(각자 자기 시점의 복사본을 갖고 있음).
