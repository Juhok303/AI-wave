"""레포를 처음 받아 실행하기 전, 필요한 API 키/로그인 정보가 .env에 있고 실제로
동작하는지(라이브 체크) 확인한다. check-requirements 스킬이 호출한다.
"""

import os
import sys

import requests
from dotenv import load_dotenv

import fnguide_client

load_dotenv()

SAMSUNG_CORP_CODE = "00126380"  # 라이브 체크용 샘플 corp_code (삼성전자)


def check_dart() -> tuple[bool, str]:
    api_key = os.environ.get("DART_API_KEY")
    if not api_key:
        return False, "DART_API_KEY가 .env에 없습니다. https://opendart.fss.or.kr 에서 발급받아 채워주세요."
    try:
        resp = requests.get(
            "https://opendart.fss.or.kr/api/company.json",
            params={"crtfc_key": api_key, "corp_code": SAMSUNG_CORP_CODE},
            timeout=10,
        )
        payload = resp.json()
    except requests.RequestException as e:
        return False, f"DART API 호출 실패(네트워크 오류): {e}"

    if payload.get("status") == "000":
        return True, "정상 동작 확인"
    return False, f"DART API 키가 있지만 호출 실패 (status={payload.get('status')}, message={payload.get('message')})"


def check_fred() -> tuple[bool, str]:
    api_key = os.environ.get("FRED_API_KEY")
    if not api_key:
        return False, "FRED_API_KEY가 .env에 없습니다. https://fred.stlouisfed.org/docs/api/api_key.html 에서 발급받아 채워주세요."
    try:
        resp = requests.get(
            "https://api.stlouisfed.org/fred/series/observations",
            params={"series_id": "CPIAUCSL", "api_key": api_key, "file_type": "json", "limit": 1},
            timeout=10,
        )
        payload = resp.json()
    except requests.RequestException as e:
        return False, f"FRED API 호출 실패(네트워크 오류): {e}"

    if "error_message" in payload:
        return False, f"FRED API 키가 있지만 호출 실패: {payload['error_message']}"
    return True, "정상 동작 확인"


def check_fnguide() -> tuple[bool, str]:
    """FnGuide 접근 경로를 안내한다.

    ⚠️ 2026-08-13부터 실제 경로는 `fnspace-mcp` MCP 플러그인(mcp__fnspace__*)이다 —
    이건 Claude Code 세션 안에서만 연결되므로 이 독립 Python 스크립트에서는 라이브
    체크가 불가능하다(세션 밖에서 `claude mcp list`로 `plugin:fnspace:fnspace`가
    Connected인지 확인). 아래는 과거에 검증한 대체/폴백 경로에 대한 라이브 체크다.
    """
    fnguide_id = os.environ.get("FNGUIDE_ID")
    fnguide_pw = os.environ.get("FNGUIDE_PW")
    if fnguide_id and fnguide_pw:
        try:
            session = fnguide_client.login(fnguide_id, fnguide_pw)
        except requests.RequestException as e:
            return False, f"FnGuide 로그인 호출 실패(네트워크 오류): {e}"
        except RuntimeError as e:
            return False, f"FnGuide 로그인 실패: {e}"

        try:
            has_entitlement = fnguide_client.has_consensus_entitlement(session)
        except requests.RequestException as e:
            return False, f"로그인은 성공했지만 컨센서스 이용권 확인 중 오류: {e}"

        if not has_entitlement:
            return False, (
                "www.fnguide.com 로그인은 성공하지만 계정에 컨센서스 이용권이 없음(2026-08-12 확인, "
                "이 경로는 사용하지 않음). fnspace-mcp 플러그인(mcp__fnspace__*)이 실제 경로다 — "
                "`claude mcp list`로 연결 상태 확인, 세션 안에서 mcp__fnspace__quickstart 호출 권장."
            )

    return False, (
        "이 스크립트는 fnspace-mcp의 세션 내 연결 상태를 확인할 수 없다. "
        "`claude mcp list`에서 plugin:fnspace:fnspace가 Connected인지, 세션 안에서 "
        "mcp__fnspace__quickstart 결과가 정상인지 확인할 것. 현재는 동봉된 임시 공유 키로 동작 중이며 "
        "2026-08-15 만료 — 그 이후엔 팀 자체 FNSPACE_API_KEY를 환경변수로 설정해야 한다."
    )


CHECKS = {
    "DART": check_dart,
    "FRED": check_fred,
    "FnGuide/FnSpace": check_fnguide,
}

# 없어도 나머지 파이프라인은 돌아가는 항목 (fetch-web은 API 키 자체가 필요 없음)
OPTIONAL = {"FnGuide/FnSpace"}


def run_all() -> dict[str, tuple[bool, str]]:
    return {name: fn() for name, fn in CHECKS.items()}


def main() -> int:
    results = run_all()
    print("=== 실행 전 요구사항 점검 ===")
    all_required_ok = True
    for name, (ok, message) in results.items():
        status = "OK" if ok else ("WARN" if name in OPTIONAL else "FAIL")
        print(f"[{status}] {name}: {message}")
        if not ok and name not in OPTIONAL:
            all_required_ok = False

    print()
    if all_required_ok:
        print("필수 항목(DART/FRED)은 모두 정상입니다. FnGuide/FnSpace는 선택 사항이며 위 안내를 참고하세요.")
    else:
        print("필수 항목 중 실패한 게 있습니다. 위 안내에 따라 .env를 채운 뒤 다시 실행해주세요.")

    return 0 if all_required_ok else 1


if __name__ == "__main__":
    sys.exit(main())
