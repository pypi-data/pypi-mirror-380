from __future__ import annotations
import time, uuid, webbrowser, json
from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any
from urllib.parse import urljoin
import requests

# ----------------- 설정 -----------------
@dataclass
class DeviceAuthConfig:
    # Keycloak realm의 issuer나 realm base URL 아무거나 OK (예: https://auth.example.com/realms/myrealm)
    server_url: str
    client_id: str
    scope: str = "openid profile email"
    # 선택: Keycloak 대신 당신의 백엔드 프록시에서 토큰을 주고받고 싶을 때
    exchange_endpoint: Optional[str] = None
    # 폴링 주기/타임아웃
    poll_interval: int = 5
    poll_timeout: int = 300  # 초

@dataclass
class TokenSet:
    access_token: str
    refresh_token: Optional[str] = None
    id_token: Optional[str] = None
    token_type: Optional[str] = "Bearer"
    expires_in: Optional[int] = None
    expires_at: Optional[int] = None

# ----------------- 간단 스토리지 -----------------
class MemoryStorage:
    def __init__(self): self._d: Dict[str, str] = {}
    def get(self, k: str) -> Optional[str]: return self._d.get(k)
    def set(self, k: str, v: str) -> None: self._d[k] = v
    def remove(self, k: str) -> None: self._d.pop(k, None)

class FileStorage:
    def __init__(self, path: str = ".device_tokens.json"):
        self.path = path
    def _load(self) -> Dict[str, str]:
        try:
            with open(self.path, "r", encoding="utf-8") as f: return json.load(f)
        except Exception: return {}
    def _save(self, d: Dict[str, str]) -> None:
        tmp = self.path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f: json.dump(d, f)
        import os; os.replace(tmp, self.path)
    def get(self, k: str) -> Optional[str]: return self._load().get(k)
    def set(self, k: str, v: str) -> None:
        d = self._load(); d[k] = v; self._save(d)
    def remove(self, k: str) -> None:
        d = self._load(); d.pop(k, None); self._save(d)

# ----------------- 클라이언트 -----------------
class DeviceFlowAuth:
    KEY_TOKEN = "token_set"

    def __init__(self, cfg: DeviceAuthConfig, storage=None, http=None, now=None):
        self.cfg = cfg
        self.storage = storage or MemoryStorage()
        self.http = http or requests.Session()
        self.now = now or (lambda: int(time.time()))
        self._well_known = self._discover()

    # OIDC discovery
    def _discover(self) -> Dict[str, Any]:
        # server_url 이 issuer(…/realms/myrealm)라면 그대로, base 라면 join
        base = self.cfg.server_url.rstrip("/") + "/"
        # 둘 다 지원: …/.well-known/openid-configuration 또는 realm base에 상대 경로
        # Keycloak은 realm 루트에 well-known가 있음
        well_known_url = urljoin(base, ".well-known/openid-configuration")
        r = self.http.get(well_known_url, timeout=15)
        r.raise_for_status()
        return r.json()

    # 한 번에 로그인(+ 브라우저 열기 + 폴링 + (선택)교환)까지
    def login(self, open_browser: bool = True) -> TokenSet:
        device_data = self._start_device_authorization()
        verify_url = device_data.get("verification_uri_complete") or device_data["verification_uri"]
        user_code = device_data.get("user_code")
        if open_browser:
            try: webbrowser.open(verify_url)
            except Exception: pass

        print("=== Device Login ===")
        if user_code: print("User Code:", user_code)
        print("Open and approve:", verify_url)

        token = self._poll_token(device_data)
        # (선택) 백엔드 교환: 당신의 프록시가 refresh_token 기반 교환을 지원한다고 가정
        if self.cfg.exchange_endpoint:
            token = self._exchange_via_backend(token)
        self._save_token(token)
        return token

    # 최신 access_token 얻기(만료 시 자동 refresh; 교환 엔드포인트가 있으면 거기로)
    def get_access_token(self) -> Optional[str]:
        ts = self.refresh_if_needed()
        return ts.access_token if ts else None

    # 세션 상태
    def get_session(self) -> Dict[str, Any]:
        ts = self._load_token()
        return {"status": "authenticated", "tokenSet": asdict(ts)} if ts else {"status": "unauthenticated", "tokenSet": None}

    def logout(self) -> None:
        self.storage.remove(self.KEY_TOKEN)

    # ----- 내부 구현 -----
    def _start_device_authorization(self) -> Dict[str, Any]:
        device_ep = self._well_known.get("device_authorization_endpoint") or urljoin(
            self.cfg.server_url.rstrip("/") + "/", "protocol/openid-connect/auth/device"
        )
        r = self.http.post(device_ep, data={
            "client_id": self.cfg.client_id,
            "scope": self.cfg.scope,
        }, timeout=15)
        if not r.ok:
            raise RuntimeError(f"Device authorization failed: {r.status_code} {r.text}")
        return r.json()

    def _poll_token(self, device_data: Dict[str, Any]) -> TokenSet:
        token_ep = self._well_known["token_endpoint"]
        interval = int(device_data.get("interval", self.cfg.poll_interval))
        deadline = self.now() + self.cfg.poll_timeout

        while True:
            if self.now() > deadline:
                raise TimeoutError("Timed out waiting for user authorization.")

            r = self.http.post(token_ep, data={
                "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
                "device_code": device_data["device_code"],
                "client_id": self.cfg.client_id,
            }, timeout=15)

            if r.status_code == 200:
                payload = r.json()
                ts = TokenSet(**payload)
                if ts.expires_in:
                    ts.expires_at = self.now() + ts.expires_in - 30
                return ts

            # 표준 에러 처리
            try:
                err = r.json().get("error")
            except Exception:
                err = None

            if err in ("authorization_pending", "slow_down"):
                # slow_down이면 폴링 간격을 늘려도 됨
                time.sleep(interval + (2 if err == "slow_down" else 0))
                continue
            elif err in ("access_denied", "expired_token"):
                raise RuntimeError(f"Device flow halted: {err}")
            else:
                # 기타 에러
                raise RuntimeError(f"Token polling failed: {r.status_code} {r.text}")

    def _exchange_via_backend(self, ts: TokenSet) -> TokenSet:
        """백엔드 프록시로 교환.
        - 초기 교환: Keycloak에서 받은 refresh_token을 넘겨 '우리 백엔드 토큰'을 발급받는 패턴(당신 JS 코드의 refresh 흐름과 동일).
        - 백엔드 구현이 'subject_token' 기반(token-exchange)이라면 여길 수정해 주세요.
        """
        if not ts.refresh_token:
            # refresh_token이 없다면 backend가 access_token 기반 교환을 지원해야 함(필드 이름은 조직 구현에 맞춰 수정)
            data = {"access_token": ts.access_token}
        else:
            data = {
                "grant_type": "refresh_token",
                "client_id": self.cfg.client_id,      # 필요 없으면 제거
                "refresh_token": ts.refresh_token,
            }
        r = self.http.post(self.cfg.exchange_endpoint, data=data,
                           headers={"Content-Type": "application/x-www-form-urlencoded"},
                           timeout=15)
        if not r.ok:
            raise RuntimeError(f"Backend exchange failed: {r.status_code} {r.text}")
        out = TokenSet(**r.json())
        if out.expires_in:
            out.expires_at = self.now() + out.expires_in - 30
        return out

    def refresh_if_needed(self) -> Optional[TokenSet]:
        ts = self._load_token()
        if not ts: return None
        if ts.expires_at and ts.expires_at > self.now():
            return ts

        # 만료됨 → 리프레시
        if not ts.refresh_token:
            self.logout(); return None

        if self.cfg.exchange_endpoint:
            # 백엔드 경유 리프레시
            r = self.http.post(self.cfg.exchange_endpoint, data={
                "grant_type": "refresh_token",
                "client_id": self.cfg.client_id,          # 필요 없으면 제거
                "refresh_token": ts.refresh_token,
            }, headers={"Content-Type": "application/x-www-form-urlencoded"}, timeout=15)
            if not r.ok:
                self.logout(); return None
            nts = TokenSet(**r.json())
        else:
            # Keycloak 직접 리프레시
            token_ep = self._well_known["token_endpoint"]
            r = self.http.post(token_ep, data={
                "grant_type": "refresh_token",
                "client_id": self.cfg.client_id,
                "refresh_token": ts.refresh_token,
            }, headers={"Content-Type": "application/x-www-form-urlencoded"}, timeout=15)
            if not r.ok:
                self.logout(); return None
            nts = TokenSet(**r.json())

        if nts.expires_in:
            nts.expires_at = self.now() + nts.expires_in - 30
        self._save_token(nts)
        return nts

    # 저장/로드
    def _save_token(self, ts: TokenSet) -> None:
        self.storage.set(self.KEY_TOKEN, json.dumps(asdict(ts)))
    def _load_token(self) -> Optional[TokenSet]:
        raw = self.storage.get(self.KEY_TOKEN)
        return TokenSet(**json.loads(raw)) if raw else None
