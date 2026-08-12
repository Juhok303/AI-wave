"""DART(전자공시시스템) Open API 클라이언트.

fetch-dart 스킬이 호출한다. DART_API_KEY는 .env에서 읽는다.
"""

import io
import json
import os
import zipfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from xml.etree import ElementTree

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://opendart.fss.or.kr/api"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CORP_CODE_CACHE = PROJECT_ROOT / "data" / "cache" / "dart_corp_codes.json"

# 판단 스킬(judge-*)이 참조하는 손익계산서 핵심 계정.
INCOME_STATEMENT_ACCOUNTS = ["매출액", "매출원가", "매출총이익", "영업이익"]

# 사업보고서(연간). 반기/분기가 필요하면 11012(반기)/11013(1분기)/11014(3분기)로 교체.
ANNUAL_REPORT_CODE = "11011"


def _load_corp_codes(api_key: str, force_refresh: bool = False) -> list[dict]:
    """전체 기업의 corp_code 마스터 목록을 가져온다 (상장사만 필터링). 로컬에 캐싱한다."""
    if not force_refresh and CORP_CODE_CACHE.exists():
        return json.loads(CORP_CODE_CACHE.read_text(encoding="utf-8"))

    resp = requests.get(BASE_URL + "/corpCode.xml", params={"crtfc_key": api_key}, timeout=30)
    resp.raise_for_status()
    with zipfile.ZipFile(io.BytesIO(resp.content)) as zf:
        xml_bytes = zf.read("CORPCODE.xml")

    root = ElementTree.fromstring(xml_bytes)
    companies = []
    for node in root.findall("list"):
        stock_code = (node.findtext("stock_code") or "").strip()
        if not stock_code:
            continue  # 비상장사 제외
        companies.append(
            {
                "corp_code": node.findtext("corp_code").strip(),
                "corp_name": node.findtext("corp_name").strip(),
                "stock_code": stock_code,
            }
        )

    CORP_CODE_CACHE.parent.mkdir(parents=True, exist_ok=True)
    CORP_CODE_CACHE.write_text(json.dumps(companies, ensure_ascii=False), encoding="utf-8")
    return companies


def resolve_corp_code(company_name: str, api_key: str) -> dict:
    """기업명(또는 종목코드)으로 DART corp_code를 찾는다."""
    companies = _load_corp_codes(api_key)
    name = company_name.strip()

    if name.isdigit():
        matches = [c for c in companies if c["stock_code"] == name]
        if matches:
            return matches[0]

    exact = [c for c in companies if c["corp_name"] == name]
    if len(exact) == 1:
        return exact[0]
    if len(exact) > 1:
        return exact[0]

    partial = [c for c in companies if name in c["corp_name"]]
    if len(partial) == 1:
        return partial[0]
    if len(partial) > 1:
        raise ValueError(
            f"'{company_name}'에 대해 후보가 여러 개입니다: "
            + ", ".join(f"{c['corp_name']}({c['stock_code']})" for c in partial[:10])
        )

    raise ValueError(f"'{company_name}'에 해당하는 상장기업을 DART corp_code 목록에서 찾지 못했습니다.")


def _parse_amount(raw: str | None) -> int | None:
    if not raw:
        return None
    cleaned = raw.replace(",", "").strip()
    if not cleaned:
        return None
    try:
        return int(cleaned)
    except ValueError:
        return None


def _fetch_financial_statements(corp_code: str, api_key: str, bsns_year: str, reprt_code: str) -> list[dict]:
    for fs_div in ("CFS", "OFS"):  # 연결재무제표 우선, 없으면 개별재무제표
        resp = requests.get(
            BASE_URL + "/fnlttSinglAcntAll.json",
            params={
                "crtfc_key": api_key,
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
                "fs_div": fs_div,
            },
            timeout=15,
        )
        resp.raise_for_status()
        payload = resp.json()
        if payload.get("status") == "000":
            return payload["list"]
    return []


def _extract_income_statement(raw_list: list[dict]) -> dict:
    """손익계산서 핵심 계정만 당기/전기/전전기 금액으로 추린다."""
    result = {}
    for row in raw_list:
        if row.get("sj_div") != "IS":
            continue
        account_nm = row.get("account_nm", "").strip()
        if account_nm not in INCOME_STATEMENT_ACCOUNTS:
            continue
        result[account_nm] = {
            "당기": {"기간": row.get("thstrm_nm"), "금액": _parse_amount(row.get("thstrm_amount"))},
            "전기": {"기간": row.get("frmtrm_nm"), "금액": _parse_amount(row.get("frmtrm_amount"))},
            "전전기": {"기간": row.get("bfefrmtrm_nm"), "금액": _parse_amount(row.get("bfefrmtrm_amount"))},
        }
    return result


def _fetch_recent_disclosures(corp_code: str, api_key: str, days: int = 365) -> list[dict]:
    end_de = datetime.now().strftime("%Y%m%d")
    bgn_de = (datetime.now() - timedelta(days=days)).strftime("%Y%m%d")
    resp = requests.get(
        BASE_URL + "/list.json",
        params={
            "crtfc_key": api_key,
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
            "page_count": 50,
        },
        timeout=15,
    )
    resp.raise_for_status()
    payload = resp.json()
    if payload.get("status") != "000":
        return []
    return [
        {
            "report_nm": item.get("report_nm"),
            "rcept_dt": item.get("rcept_dt"),
            "rcept_no": item.get("rcept_no"),
        }
        for item in payload.get("list", [])
    ]


def get_company_filings(company_name: str, bsns_year: str | None = None) -> dict:
    """개별기업의 최근 사업보고서 손익계산서 + 최근 1년 공시 목록을 가져온다.

    Returns: 매출, 원가, 영업이익 등 judgment-rules.md의 대체지표 계산에 필요한 원자료.
    """
    api_key = os.environ.get("DART_API_KEY")
    if not api_key:
        raise RuntimeError("DART_API_KEY가 설정되지 않았습니다. .env를 확인하세요.")

    company = resolve_corp_code(company_name, api_key)
    corp_code = company["corp_code"]

    # 사업보고서는 회계연도 종료 후 통상 90일 내 제출되므로, 아직 미제출일 수 있는
    # 최근 연도부터 최대 3개 연도까지 거슬러 올라가며 조회한다.
    years_to_try = [bsns_year] if bsns_year else [str(datetime.now().year - i) for i in (1, 2, 3)]

    income_statement = {}
    used_year = None
    for year in years_to_try:
        raw_list = _fetch_financial_statements(corp_code, api_key, year, ANNUAL_REPORT_CODE)
        if raw_list:
            income_statement = _extract_income_statement(raw_list)
            used_year = year
            break

    return {
        "corp_code": corp_code,
        "corp_name": company["corp_name"],
        "stock_code": company["stock_code"],
        "bsns_year": used_year,
        "income_statement": income_statement,
        "recent_disclosures": _fetch_recent_disclosures(corp_code, api_key),
        "fetched_at": datetime.now(timezone.utc).isoformat(),
    }


if __name__ == "__main__":
    import sys

    result = get_company_filings(sys.argv[1] if len(sys.argv) > 1 else "삼성전자")
    print(json.dumps(result, ensure_ascii=False, indent=2))
