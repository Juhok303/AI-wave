---
name: fetch-web
description: 뉴스 기사·회사 홈페이지 등 웹 데이터를 개별기업 기준으로 수집해 data/cache/에 저장한다. DART/FnGuide/FRED 데이터 키트 밖에 있는 리뷰·ESG·경쟁사 동향 등 Proxy 지표용 원자료를 채우는 스킬.
---

# fetch-web

## 입력
- 기업명 1개

## 왜 필요한가
`judgment-rules.md`의 여러 대체지표(Underpriced Customer Love의 리뷰·검색 트렌드, 스크리닝 체크리스트의 ESG·신규 경쟁 브랜드 동향)는 DART/FnGuide/FRED 데이터 키트 밖의 정보다. 이 스킬은 다른 fetch-* 스킬과 달리 API 키/`lib/` 클라이언트를 쓰지 않고, Claude Code의 `WebSearch`/`WebFetch` 툴을 직접 사용해 수집한다.

## 동작
1. `WebSearch`로 아래 쿼리들을 실행한다 (기업명은 실제 대상으로 치환):
   - `"<기업명>" 리뷰 후기` — Expressed Love(리뷰) 및 가격탄력성 관련 신호
   - `"<기업명>" 신제품 OR 가격 인상` — WTP(가격결정력) Catalyst 확인
   - `"<기업명>" 경쟁사 OR 신규 브랜드` — 경쟁력/Moat 침식 신호
   - `"<기업명>" ESG OR 소송 OR 제재` — 스크리닝 체크리스트 ESG 항목
2. 검색 결과 중 관련성 높은 기사 상위 몇 건은 `WebFetch`로 본문을 확인해 핵심 내용을 요약한다.
3. 기업 공식 홈페이지가 확인되면 IR/뉴스룸 페이지를 `WebFetch`로 확인한다(가격 정책, 신규 채널·매장 발표 등).
4. 결과를 `data/cache/<기업명>/web.json`에 저장한다. 각 항목에는 반드시 출처 URL, 제목, 수집일자, 1~2문장 요약을 포함한다.

## 출력
- `data/cache/<기업명>/web.json` — `judge-underpriced-customer-love`, `screen-fundamentals` 스킬이 참조할 Proxy 원자료.

## 원칙
- 이 스킬로 얻는 데이터는 전부 **Proxy(Low~Medium Confidence)**로 취급한다 — `docs/underpriced-customer-love-framework.md` K절의 데이터 신뢰도 처리 원칙(Medium 0.8x, Low 0.6x 할인)을 그대로 적용한다.
- 검색 결과가 없거나 확인이 안 되는 항목은 "데이터 없음"으로 명시한다. 추측이나 일반 상식으로 채우지 않는다.
- 출처가 불분명한 커뮤니티 글/광고성 콘텐츠는 제외하고 언론사·공식 채널 위주로 수집한다.

## TODO
- [ ] 반복 실행 시 검색 쿼리 템플릿을 업종별(Beauty/Subscription/Software 등, `docs/underpriced-customer-love-framework.md` J절)로 세분화할지 검토
