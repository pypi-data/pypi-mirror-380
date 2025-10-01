from __future__ import annotations
import base64, hashlib, os, time, uuid
from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any
from urllib.parse import urlencode, urlparse, parse_qs
import requests

# ---- 타입 정의 ----
@dataclass
class AuthConfig:
    base_url: str           # 예) https://auth.example.com/realms/myrealm
    client_id: str
    redirect_uri: str       # 예) http://127.0.0.1:8787/callback (로컬 서버를 띄울 경우)
    scope: str = "openid profile email"
    auth_endpoint: str = "/protocol/openid-connect/auth"
    token_endpoint: str = "/protocol/openid-connect/token"
    exchange_endpoint: Optional[str] = None  # 예) https://api.example.com/api/auth/exchange-token

@dataclass
class TokenSet:
    access_token: str
    refresh_token: Optional[str] = None
    id_token: Optional[str] = None
    token_type: Optional[str] = "Bearer"
    expires_in: Optional[int] = None
    expires_at: Optional[int] = None  # epoch seconds

# ---- 간단 스토리지(메모리/파일 선택) ----
class MemoryStorage:
    def __init__(self): self._d: Dict[str, str] = {}
    def get(self, k: str) -> Optional[str]: return self._d.get(k)
    def set(self, k: str, v: str) -> None: self._d[k] = v
    def remove(self, k: str) -> None: self._d.pop(k, None)

class FileStorage:
    def __init__(self, path: str = ".token_store.json"):
        self.path = path
    def _load(self) -> Dict[str, str]:
        try:
            import json; 
            with open(self.path, "r", encoding="utf-8") as f: return json.load(f)
        except Exception: return {}
    def _save(self, d: Dict[str, str]) -> None:
        import json, tempfile, os
        tmp = self.path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f: json.dump(d, f)
        os.replace(tmp, self.path)
    def get(self, k: str) -> Optional[str]: return self._load().get(k)
    def set(self, k: str, v: str) -> None:
        d = self._load(); d[k] = v; self._save(d)
    def remove(self, k: str) -> None:
        d = self._load(); d.pop(k, None); self._save(d)

# ---- 유틸 ----
def _b64url_no_pad(b: bytes) -> str:
    return base64.urlsafe_b64encode(b).decode().rstrip("=")

def _rand_verifier(n: int = 64) -> str:
    # RFC 7636 허용 문자 집합 사용
    cs = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~"
    return "".join(chr(cs[x % len(cs)]) for x in os.urandom(n))

def _sha256(s: str) -> str:
    return _b64url_no_pad(hashlib.sha256(s.encode()).digest())

# ---- PKCE 클라이언트 ----
class KeycloakPKCE:
    KEY_VERIFIER = "pkce_verifier"
    KEY_STATE = "pkce_state"
    KEY_TOKEN = "token_set"

    def __init__(self, cfg: AuthConfig, storage=None, now=None, http=None):
        self.cfg = cfg
        self.storage = storage or MemoryStorage()
        self.now = now or (lambda: int(time.time()))
        self.http = http or requests.Session()

    # 1) 로그인 URL 만들기 (state, verifier 저장)
    def get_auth_url(self) -> str:
        verifier = _rand_verifier(64)
        challenge = _sha256(verifier)
        state = str(uuid.uuid4())

        self.storage.set(self.KEY_VERIFIER, verifier)
        self.storage.set(self.KEY_STATE, state)

        url = f"{self.cfg.base_url.rstrip('/')}{self.cfg.auth_endpoint}"
        params = {
            "client_id": self.cfg.client_id,
            "response_type": "code",
            "scope": self.cfg.scope,
            "redirect_uri": self.cfg.redirect_uri,
            "code_challenge": challenge,
            "code_challenge_method": "S256",
            "state": state,
        }
        return f"{url}?{urlencode(params)}"

    # 2) 콜백 URL(혹은 code/state 문자열) 처리 → 토큰 교환
    def handle_redirect(self, full_callback_url: str) -> TokenSet:
        qs = parse_qs(urlparse(full_callback_url).query)
        code = (qs.get("code") or [None])[0]
        state = (qs.get("state") or [None])[0]
        if not code or not state:
            raise RuntimeError("Missing code/state in callback URL")

        saved_state = self.storage.get(self.KEY_STATE)
        if not saved_state or state != saved_state:
            raise RuntimeError("State mismatch")

        return self.exchange_code_for_token(code)

    def exchange_code_for_token(self, code: str) -> TokenSet:
        verifier = self.storage.get(self.KEY_VERIFIER)
        if not verifier:
            raise RuntimeError("Missing PKCE verifier")

        body = {
            "grant_type": "authorization_code",
            "client_id": self.cfg.client_id,
            "code": code,
            "redirect_uri": self.cfg.redirect_uri,
            "code_verifier": verifier,
        }
        endpoint = self.cfg.exchange_endpoint or f"{self.cfg.base_url.rstrip('/')}{self.cfg.token_endpoint}"

        r = self.http.post(endpoint, data=body, headers={"Content-Type": "application/x-www-form-urlencoded"}, timeout=30)
        if not r.ok:
            raise RuntimeError(f"Token exchange failed: {r.status_code} {r.text}")

        ts = TokenSet(**r.json())
        if ts.expires_in:
            ts.expires_at = self.now() + ts.expires_in - 30  # 30s 버퍼
        self._save_token(ts)
        return ts

    # 3) 리프레시
    def refresh_if_needed(self) -> Optional[TokenSet]:
        ts = self._load_token()
        if not ts: return None
        if ts.expires_at and ts.expires_at > self.now():  # 아직 유효
            return ts
        if not ts.refresh_token:
            self.logout(); return None

        body = {
            "grant_type": "refresh_token",
            "client_id": self.cfg.client_id,
            "refresh_token": ts.refresh_token,
        }
        endpoint = self.cfg.exchange_endpoint or f"{self.cfg.base_url.rstrip('/')}{self.cfg.token_endpoint}"
        r = self.http.post(endpoint, data=body, headers={"Content-Type": "application/x-www-form-urlencoded"}, timeout=30)
        if not r.ok:
            self.logout()
            return None
        new_ts = TokenSet(**r.json())
        if new_ts.expires_in:
            new_ts.expires_at = self.now() + new_ts.expires_in - 30
        self._save_token(new_ts)
        return new_ts

    def get_access_token(self) -> Optional[str]:
        ts = self.refresh_if_needed()
        return ts.access_token if ts else None

    def get_session(self) -> Dict[str, Any]:
        ts = self._load_token()
        return {"status": "authenticated", "tokenSet": asdict(ts)} if ts else {"status": "unauthenticated", "tokenSet": None}

    def logout(self) -> None:
        self.storage.remove(self.KEY_TOKEN)

    # ---- 내부 저장/로드 ----
    def _save_token(self, ts: TokenSet) -> None:
        import json
        self.storage.set(self.KEY_TOKEN, json.dumps(asdict(ts)))
    def _load_token(self) -> Optional[TokenSet]:
        import json
        raw = self.storage.get(self.KEY_TOKEN)
        return TokenSet(**json.loads(raw)) if raw else None
