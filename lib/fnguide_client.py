"""FnGuide 컨센서스 데이터 클라이언트.

fetch-fnguide 스킬이 호출한다. API 키가 아니라 로그인 계정(FNGUIDE_ID/FNGUIDE_PW)을
.env에서 읽는다.
"""

import os


def get_consensus(company_name: str) -> dict:
    """개별기업의 컨센서스 추정치(매출/이익 추정, 추정 ASP 등)를 가져온다.

    Returns: judgment-rules.md의 대체지표 계산에 필요한 컨센서스 원자료.
    """
    fnguide_id = os.environ.get("FNGUIDE_ID")
    fnguide_pw = os.environ.get("FNGUIDE_PW")
    if not fnguide_id or not fnguide_pw:
        raise RuntimeError("FNGUIDE_ID/FNGUIDE_PW가 설정되지 않았습니다. .env를 확인하세요.")
    # TODO: 로그인 대상 FnGuide 서비스/URL 확정 후 세션 로그인 + 페이지 파싱 구현
    raise NotImplementedError
