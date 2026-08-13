# 리포트 디자인 시스템 사용 가이드

레포 어디에 넣을지: `report-assets/design-system.css` (이 파일 옆의
`design-system.css`를 그대로 이 경로에 커밋)

## 왜 이렇게 하나

리포트 HTML은 매번 Claude(스킬)가 새로 작성한다. 스타일까지 매번
새로 작성하게 두면 리포트마다 톤이 미묘하게 달라진다. 대신 **CSS는
고정 파일 하나로 박아두고, 스킬에게는 "이 파일을 링크하고 정해진
클래스만 써라"라고만 지시**한다. 그러면:

- 어떤 기업/프레임워크든 같은 톤으로 나온다
- 디자인을 바꾸고 싶으면 `design-system.css` 한 곳만 고치면 전체 리포트에
  소급 적용된다 (HTML은 그대로 두고 CSS만 교체해도 됨)
- LLM이 매번 색상/폰트를 창작하지 않아도 되니 토큰도 아낀다

## 스킬에 추가해야 할 지시문

`investment-desk` 오케스트레이터(또는 각 `judge-*` 스킬의 리포트 출력
단계)의 시스템 프롬프트/SKILL.md에 아래 문단을 그대로 추가한다:

```
최종 HTML 리포트를 작성할 때는 반드시 아래를 지킨다:

1. <head>에 다음을 정확히 이 순서로 삽입한다:
   <link rel="preconnect" href="https://fonts.googleapis.com">
   <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
   <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css">
   <link rel="stylesheet" href="report-assets/design-system.css">

2. report-assets/design-system.css에 이미 정의된 클래스만 사용한다.
   새로운 색상 hex 값이나 폰트를 <style> 블록에 직접 추가하지 않는다.
   (report-assets/REPORT_DESIGN_GUIDE.md의 컴포넌트 목록을 참고할 것)

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

## 배포 방법 (레포가 private이라 여기서 직접 push는 못 함)

1. 이 폴더의 `design-system.css`를 레포의 `report-assets/design-system.css`로 커밋
2. 위 "스킬에 추가해야 할 지시문" 문단을 `investment-desk` 오케스트레이터
   프롬프트(또는 공통 리포트 생성 단계)에 삽입
3. 기존 삼성전자/Costco 리포트도 `<style>` 전체를 지우고
   `<link rel="stylesheet" href="report-assets/design-system.css">`
   한 줄로 교체 — 지금 두 파일의 `<style>` 내용은 이 CSS 파일과
   완전히 동일하므로 바로 교체 가능하다
4. 다음 리포트부터는 스킬이 이 CSS를 링크만 하면 자동으로 같은 톤 적용
