"""FnGuide 컨센서스 데이터 클라이언트.

fetch-fnguide 스킬이 호출한다. FnSpace(fnspace.com, FnGuide 공식 API) API 키를
FNSPACE_API_KEY로 .env에서 읽는다.

FNGUIDE_ID/FNGUIDE_PW(www.fnguide.com 로그인)는 보유 계정에 컨센서스 이용권이
없어 사용할 수 없는 것으로 확인됨(2026-08-12) — check-requirements 참고.
"""

import os


def get_consensus(company_name: str) -> dict:
    """개별기업의 컨센서스 추정치(매출/이익 추정, 추정 ASP 등)를 가져온다.

    Returns: judgment-rules.md의 대체지표 계산에 필요한 컨센서스 원자료.
    """
    api_key = os.environ.get("FNSPACE_API_KEY")
    if not api_key:
        raise RuntimeError("FNSPACE_API_KEY가 설정되지 않았습니다. fnspace.com에서 발급 후 .env를 확인하세요.")
    # TODO: FnSpace API 엔드포인트/응답 구조 확인 후 구현 (fnspace.com 가입 필요)
    raise NotImplementedError
