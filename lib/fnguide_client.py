"""FnGuide 컨센서스 데이터 클라이언트.

fetch-fnguide 스킬이 호출한다. FNGUIDE_API_KEY는 .env에서 읽는다.
"""

import os


def get_consensus(company_name: str) -> dict:
    """개별기업의 컨센서스 추정치(매출/이익 추정, 추정 ASP 등)를 가져온다.

    Returns: judgment-rules.md의 대체지표 계산에 필요한 컨센서스 원자료.
    """
    api_key = os.environ.get("FNGUIDE_API_KEY")
    if not api_key:
        raise RuntimeError("FNGUIDE_API_KEY가 설정되지 않았습니다. .env를 확인하세요.")
    # TODO: FnGuide 접근 방식(API/스크래핑) 확정 후 구현
    raise NotImplementedError
