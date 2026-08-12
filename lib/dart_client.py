"""DART(전자공시시스템) Open API 클라이언트.

fetch-dart 스킬이 호출한다. DART_API_KEY는 .env에서 읽는다.
"""

import os


def get_company_filings(company_name: str) -> dict:
    """개별기업의 최근 사업보고서/분기보고서 공시 데이터를 가져온다.

    Returns: 매출, 원가, 판매량 등 judgment-rules.md의 대체지표 계산에 필요한 원자료.
    """
    api_key = os.environ.get("DART_API_KEY")
    if not api_key:
        raise RuntimeError("DART_API_KEY가 설정되지 않았습니다. .env를 확인하세요.")
    # TODO: DART Open API 호출 구현 (https://opendart.fss.or.kr)
    raise NotImplementedError
