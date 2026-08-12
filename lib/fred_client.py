"""FRED(Federal Reserve Economic Data) API 클라이언트.

fetch-fred 스킬이 호출한다. FRED_API_KEY는 .env에서 읽는다.
"""

import os

DEFAULT_SERIES = [
    # TODO: 기본으로 가져올 매크로 지표 시리즈 ID 확정 (예: CPI, 기준금리, 소매판매지수)
]


def get_macro_series(series_ids: list[str] | None = None) -> dict:
    """지정한 매크로 지표 시계열을 가져온다. 지정하지 않으면 DEFAULT_SERIES를 사용한다."""
    api_key = os.environ.get("FRED_API_KEY")
    if not api_key:
        raise RuntimeError("FRED_API_KEY가 설정되지 않았습니다. .env를 확인하세요.")
    # TODO: FRED API 호출 구현 (https://fred.stlouisfed.org/docs/api/)
    raise NotImplementedError
