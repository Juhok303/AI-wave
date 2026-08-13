"""FRED(Federal Reserve Economic Data) API 클라이언트.

fetch-fred 스킬이 호출한다. FRED_API_KEY는 .env에서 읽는다.
"""

from __future__ import annotations

import os
from datetime import datetime, timezone

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.stlouisfed.org/fred/series/observations"

# B2C 소비 관련 판단(Structural vs Cyclical 등)에 쓰이는 기본 매크로 지표.
DEFAULT_SERIES = [
    "CPIAUCSL",  # Consumer Price Index (소비자물가지수)
    "FEDFUNDS",  # Federal Funds Rate (기준금리)
    "RSAFS",  # Advance Retail Sales (소매판매)
    "UNRATE",  # Unemployment Rate (실업률)
]


def _fetch_series(series_id: str, api_key: str, limit: int) -> list[dict]:
    resp = requests.get(
        BASE_URL,
        params={
            "series_id": series_id,
            "api_key": api_key,
            "file_type": "json",
            "sort_order": "desc",
            "limit": limit,
        },
        timeout=15,
    )
    resp.raise_for_status()
    payload = resp.json()
    if "error_message" in payload:
        raise RuntimeError(f"FRED API 오류 ({series_id}): {payload['error_message']}")

    observations = []
    for obs in reversed(payload.get("observations", [])):
        value = obs["value"]
        observations.append(
            {
                "date": obs["date"],
                "value": None if value == "." else float(value),
            }
        )
    return observations


def get_macro_series(series_ids: list[str] | None = None, limit: int = 24) -> dict:
    """지정한 매크로 지표 시계열을 가져온다. 지정하지 않으면 DEFAULT_SERIES를 사용한다.

    Returns: {"fetched_at": ISO timestamp, "series": {series_id: [{"date", "value"}, ...]}}
    """
    api_key = os.environ.get("FRED_API_KEY")
    if not api_key:
        raise RuntimeError("FRED_API_KEY가 설정되지 않았습니다. .env를 확인하세요.")

    ids = series_ids or DEFAULT_SERIES
    series = {series_id: _fetch_series(series_id, api_key, limit) for series_id in ids}

    return {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "series": series,
    }


if __name__ == "__main__":
    import json
    import sys

    result = get_macro_series(sys.argv[1:] or None)
    print(json.dumps(result, ensure_ascii=False, indent=2))
