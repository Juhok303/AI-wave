"""레포를 처음 받아 실행하기 전, 필요한 API 키/로그인 정보가 .env에 있고 실제로
동작하는지(라이브 체크) 확인한다. check-requirements 스킬이 호출한다.
"""

import os
import sys

import requests
from dotenv import load_dotenv

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
    fnspace_key = os.environ.get("FNSPACE_API_KEY")
    if fnspace_key:
        return False, "FNSPACE_API_KEY가 설정되어 있지만 아직 라이브 체크/구현이 연결되지 않았습니다 (TODO)."

    fnguide_id = os.environ.get("FNGUIDE_ID")
    fnguide_pw = os.environ.get("FNGUIDE_PW")
    if fnguide_id and fnguide_pw:
        return False, (
            "FNGUIDE_ID/PW는 설정되어 있지만, 해당 계정에 컨센서스 서비스 이용권이 없어 사용할 수 없는 것으로 확인됨"
            "(2026-08-12 점검). fnspace.com(FnGuide 공식 API, 유료)으로 전환하거나 이용권을 구매해야 합니다."
        )
    return False, (
        "FnGuide 컨센서스 데이터 접근 수단이 설정되어 있지 않습니다. "
        "fnspace.com에서 FNSPACE_API_KEY를 발급받아 .env에 채워주세요 (유료)."
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
