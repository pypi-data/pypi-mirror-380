# device_auth.py
from __future__ import annotations
import sys, os, subprocess, time, webbrowser, json, requests
from dataclasses import dataclass
from typing import Optional, Dict, Any
from urllib.parse import urljoin
from IPython import get_ipython

def with_expires_at(payload: Dict[str, Any], skew: int = 30) -> Dict[str, Any]:
    d = dict(payload)  # 얕은 복사
    exp = d.get("expires_in")
    if isinstance(exp, (int, float)):
        d["expires_at"] = int(time.time()) + int(exp) - skew
    return d

# ----------------- 설정 -----------------
@dataclass
class DeviceAuthConfig:
    # 예: https://auth.example.com/realms/myrealm
    server_url: str
    client_id: str
    scope: str = "openid profile email"
    # (선택) 백엔드 프록시로 토큰 교환/리프레시를 하려면 지정
    exchange_endpoint: Optional[str] = None
    # 폴링 주기/타임아웃(초)
    poll_interval: int = 5
    poll_timeout: int = 300

# ----------------- 간단 스토리지 -----------------
class MemoryStorage:
    def __init__(self): self._d: Dict[str, str] = {}
    def get(self, k: str) -> Optional[str]: return self._d.get(k)
    def set(self, k: str, v: str) -> None: self._d[k] = v
    def remove(self, k: str) -> None: self._d.pop(k, None)

class FileStorage:
    def __init__(self, path: str = ".device_tokens.json"):
        self.path = path
    def _load(self) -> Dict[str, Any]:
        try:
            with open(self.path, "r", encoding="utf-8") as f: return json.load(f)
        except Exception: return {}
    def _save(self, d: Dict[str, Any]) -> None:
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

    def _open_url(self, url: str) -> bool:
        # 1) Colab
        try:
            from google.colab import output  # type: ignore
            output.open_url(url)  # 새 탭
            return True
        except Exception:
            pass
        # 2) Jupyter/Notebook (팝업 차단 시 무시될 수 있음)
        try:
            ip = get_ipython()
            if ip and "IPKernelApp" in ip.config:  # 주피터 느낌만 확인
                from IPython.display import Javascript, display  # type: ignore
                display(Javascript(f'window.open("{url}", "_blank")'))
                return True
        except Exception:
            pass
        # 3) 기본 웹브라우저
        try:
            if webbrowser.open_new_tab(url):
                return True
        except Exception:
            pass
        # 4) OS 명령
        try:
            if sys.platform == "darwin":
                subprocess.Popen(["open", url]); return True
            if sys.platform.startswith("win"):
                os.startfile(url); return True  # noqa: E1101
            subprocess.Popen(["xdg-open", url]); return True
        except Exception:
            pass
        return False

    # OIDC discovery
    def _discover(self) -> Dict[str, Any]:
        base = self.cfg.server_url.rstrip("/") + "/"
        well_known_url = urljoin(base, ".well-known/openid-configuration")
        r = self.http.get(well_known_url, timeout=15)
        r.raise_for_status()
        return r.json()

    # 한 번에 로그인(+ 브라우저 열기 + 폴링 + (선택) 백엔드 교환)
    def login(self, open_browser: bool = True) -> Dict[str, Any]:
        device_data = self._start_device_authorization()
        verify_url = device_data.get("verification_uri_complete") or device_data["verification_uri"]
        user_code = device_data.get("user_code")

        if open_browser:
            opened = self._open_url(verify_url)
            if not opened:
                print("브라우저 자동 오픈이 제한된 환경입니다. 아래 URL을 클릭/복사해서 열어주세요.")

        print("=== Device Login ===")
        if user_code: print("User Code:", user_code)
        print("Open and approve:", verify_url)

        token = self._poll_token(device_data)

        if self.cfg.exchange_endpoint:
            token = self._exchange_via_backend(token)

        token = with_expires_at(token)
        self._save_token(token)
        return token

    def get_access_token(self) -> Optional[str]:
        ts = self.refresh_if_needed()
        return ts.get("access_token") if ts else None

    def get_session(self) -> Dict[str, Any]:
        ts = self._load_token()
        return {"status": "authenticated", "tokenSet": ts} if ts else {"status": "unauthenticated", "tokenSet": None}

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

    def _poll_token(self, device_data: Dict[str, Any]) -> Dict[str, Any]:
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
                return r.json()

            # 표준 에러 처리
            try:
                err = r.json().get("error")
            except Exception:
                err = None

            if err in ("authorization_pending", "slow_down"):
                time.sleep(interval + (2 if err == "slow_down" else 0))
                continue
            elif err in ("access_denied", "expired_token"):
                raise RuntimeError(f"Device flow halted: {err}")
            else:
                raise RuntimeError(f"Token polling failed: {r.status_code} {r.text}")

    def _exchange_via_backend(self, ts: Dict[str, Any]) -> Dict[str, Any]:
        """
        기존 Nest 백엔드의 exchangeToken에 그대로 요청을 보낸다.
        - PKCE(code) 대신, 디바이스플로우로 이미 받은 refresh_token을 사용.
        - grant_type=refresh_token + client_id + refresh_token
        - 백엔드가 TOKEN_URL로 그대로 포워딩 → Keycloak이 정상 처리 → app 토큰 발급
        """
        if not self.cfg.exchange_endpoint:
            return ts

        refresh = ts.get("refresh_token")
        if not refresh:
            raise RuntimeError("Device flow did not return a refresh_token; cannot exchange via backend.")

        # Nest 백엔드가 바디를 그대로 TOKEN_URL로 넘기므로,
        # Keycloak 표준 'refresh_token' 그랜트 파라미터로 맞춘다.
        form = {
            "grant_type": "refresh_token",
            "client_id": self.cfg.client_id,
            "refresh_token": refresh,
            # 아래 필드들은 무시되지만, 타입/로깅 때문에 필요하면 넣어도 무방:
            # "code": "", "redirect_uri": "", "code_verifier": ""
        }

        r = self.http.post(
            self.cfg.exchange_endpoint,
            data=form,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=15,
        )
        if not r.ok:
            raise RuntimeError(f"Backend exchange failed: {r.status_code} {r.text}")

        payload = r.json()
        # 당신의 Nest 예시에 따르면 { tokens: {...} } 형태일 가능성이 큼
        maybe = payload.get("tokens") if isinstance(payload, dict) else None
        out = maybe or payload

        # 백엔드가 snake_case 또는 camelCase로 줄 수 있으니 보정
        # 예: {accessToken, refreshToken, expiresIn} → 표준 키로 변환
        if "accessToken" in out or "expiresIn" in out:
            out = {
                "access_token": out.get("accessToken"),
                "refresh_token": out.get("refreshToken"),
                "id_token": out.get("idToken"),
                "token_type": out.get("tokenType", "Bearer"),
                "expires_in": out.get("expiresIn"),
            }

        # expires_at 추가
        out = with_expires_at(out)
        return out

    def refresh_if_needed(self) -> Optional[Dict[str, Any]]:
        ts = self._load_token()
        if not ts:
            return None
        if ts.get("expires_at", 0) > self.now():
            return ts

        # 만료됨 → 리프레시
        if not ts.get("refresh_token"):
            self.logout(); return None

        if self.cfg.exchange_endpoint:
            r = self.http.post(self.cfg.exchange_endpoint, data={
                "grant_type": "refresh_token",
                "client_id": self.cfg.client_id,  # 필요 없으면 제거
                "refresh_token": ts["refresh_token"],
            }, headers={"Content-Type": "application/x-www-form-urlencoded"}, timeout=15)
        else:
            token_ep = self._well_known["token_endpoint"]
            r = self.http.post(token_ep, data={
                "grant_type": "refresh_token",
                "client_id": self.cfg.client_id,
                "refresh_token": ts["refresh_token"],
            }, headers={"Content-Type": "application/x-www-form-urlencoded"}, timeout=15)

        if not r.ok:
            self.logout(); return None

        nts = with_expires_at(r.json())
        self._save_token(nts)
        return nts

    # 저장/로드
    def _save_token(self, ts: Dict[str, Any]) -> None:
        self.storage.set(self.KEY_TOKEN, json.dumps(ts))

    def _load_token(self) -> Optional[Dict[str, Any]]:
        raw = self.storage.get(self.KEY_TOKEN)
        return json.loads(raw) if raw else None
