"""FnGuide 컨센서스 데이터 클라이언트 — 참고/보관용, 현재는 사용하지 않음.

⚠️ 2026-08-13부터 `fetch-fnguide`는 이 모듈 대신 `fnspace-mcp` MCP 플러그인
(mcp__fnspace__get_target_price 등)을 직접 호출한다 — `.claude/skills/
fetch-fnguide/SKILL.md` 참고. 이 파일은 아래 두 가지를 실측 확인한 기록으로
남겨둔다: (1) FNGUIDE_ID/FNGUIDE_PW 로그인은 브라우저 없이도 성공하지만
(2) 보유 계정에 컨센서스 이용권이 없어 데이터 조회는 여전히 불가능함
(2026-08-12, check-requirements가 지금도 이 라이브 체크를 수행함).

get_consensus()는 FNSPACE_API_KEY 기반 직접 REST 호출을 시도하는 미완성
스텁이며, fnspace-mcp로 대체됐으므로 더 구현하지 않는다.
"""

import base64
import os
import re

import requests
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

LOGIN_PAGE_URL = "https://www.fnguide.com/Users/Login"
LOGIN_API_URL = "https://www.fnguide.com/Users/UserLogin"

_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

_PUBLIC_KEY_RE = re.compile(
    r'const publicKey = "(-----BEGIN PUBLIC KEY-----.*?-----END PUBLIC KEY-----)"'
)


def _normalize_pem(raw_pem: str) -> str:
    """로그인 페이지에 한 줄로 박혀 있는 PEM을 64자 줄바꿈 형식으로 되돌린다."""
    body = raw_pem.replace("-----BEGIN PUBLIC KEY-----", "").replace("-----END PUBLIC KEY-----", "").strip()
    wrapped = "\n".join(body[i : i + 64] for i in range(0, len(body), 64))
    return f"-----BEGIN PUBLIC KEY-----\n{wrapped}\n-----END PUBLIC KEY-----\n"


def _rsa_encrypt_password(pem: str, password: str) -> str:
    """FnGuide 로그인 JS(rsaEncrypt)와 동일하게 RSA-OAEP(SHA-256/SHA-256) + base64로 암호화한다."""
    public_key = serialization.load_pem_public_key(_normalize_pem(pem).encode("ascii"))
    ciphertext = public_key.encrypt(
        password.encode("utf-8"),
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None),
    )
    return base64.b64encode(ciphertext).decode("ascii")


def login(user_id: str | None = None, user_pw: str | None = None) -> requests.Session:
    """브라우저를 열지 않고 requests 세션으로 www.fnguide.com에 로그인한다.

    /Users/Login 페이지 + 번들 JS(bundles/users/login)를 역공학해 확인한 동작을
    그대로 재현한다: 로그인 페이지에서 세션 쿠키와 RSA 공개키를 받고, 비밀번호를
    RSA-OAEP(SHA-256)로 암호화해 /Users/UserLogin에 multipart/form-data로 전송.

    Args:
        user_id: 미지정 시 FNGUIDE_ID 환경변수 사용.
        user_pw: 미지정 시 FNGUIDE_PW 환경변수 사용.

    Returns:
        로그인된 requests.Session (이후 요청에 재사용). 로그인 성공 여부와
        무관하게, 이 계정은 컨센서스 이용권이 없어 실제 데이터 조회는 별도 확인 필요.

    Raises:
        RuntimeError: 자격 증명 누락, 페이지 구조 변경(공개키 파싱 실패), 로그인 실패(ID/PW
            오류, IP/기기 제한 등 — FnGuide returnCode 메시지를 그대로 전달).
    """
    user_id = user_id or os.environ.get("FNGUIDE_ID")
    user_pw = user_pw or os.environ.get("FNGUIDE_PW")
    if not user_id or not user_pw:
        raise RuntimeError("FNGUIDE_ID/FNGUIDE_PW가 설정되지 않았습니다.")

    session = requests.Session()
    session.headers.update({"User-Agent": _USER_AGENT})

    page = session.get(LOGIN_PAGE_URL, timeout=15)
    page.raise_for_status()

    key_match = _PUBLIC_KEY_RE.search(page.text)
    if not key_match:
        raise RuntimeError("로그인 페이지에서 RSA 공개키를 찾을 수 없습니다 (사이트 구조가 바뀌었을 수 있음).")
    encrypted_pw = _rsa_encrypt_password(key_match.group(1), user_pw)

    def _post(login_type: str) -> dict:
        resp = session.post(
            LOGIN_API_URL,
            files={
                "loginType": (None, login_type),
                "userId": (None, user_id),
                "userPassword": (None, encrypted_pw),
            },
            headers={"Referer": LOGIN_PAGE_URL},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()

    data = _post("1")
    if str(data.get("returnCode")) in ("80115", "80116"):
        # 다른 기기/세션에서 이미 로그인 중 — 브라우저의 "계속 로그인" 확인창과 동일하게
        # loginType=2로 재전송하면 기존 세션을 로그아웃시키고 강제 로그인한다.
        data = _post("2")
    # 성공 시 returnCode는 int 0, 실패 시 문자열 코드("80111" 등)로 내려온다 — FnGuide API 응답이 혼용.
    if str(data.get("returnCode")) != "0":
        raise RuntimeError(
            f"FnGuide 로그인 실패 (returnCode={data.get('returnCode')}): {data.get('returnMessage')}"
        )
    return session


def has_consensus_entitlement(session: requests.Session) -> bool:
    """로그인된 세션에 컨센서스 서비스(/Consensus/*) 이용권이 있는지 확인한다.

    이용권이 없으면 FnGuide가 200 OK로 결제 유도 다이얼로그(HTML)를 내려준다
    (리다이렉트나 4xx가 아님) — 그 다이얼로그 문구("이용권이 필요한 서비스")로 판별한다.
    """
    resp = session.get("https://www.fnguide.com/Consensus/Stock", timeout=15)
    resp.raise_for_status()
    resp.encoding = "utf-8"  # FnGuide 페이지는 UTF-8이지만 Content-Type에 charset이 없어 requests가 오판단함
    return "이용권이 필요한 서비스" not in resp.text


def get_consensus(company_name: str) -> dict:
    """개별기업의 컨센서스 추정치(매출/이익 추정, 추정 ASP 등)를 가져온다.

    Returns: judgment-rules.md의 대체지표 계산에 필요한 컨센서스 원자료.
    """
    api_key = os.environ.get("FNSPACE_API_KEY")
    if not api_key:
        raise RuntimeError("FNSPACE_API_KEY가 설정되지 않았습니다. fnspace.com에서 발급 후 .env를 확인하세요.")
    # TODO: FnSpace API 엔드포인트/응답 구조 확인 후 구현 (fnspace.com 가입 필요)
    raise NotImplementedError
