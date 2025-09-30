# CLOUDVAULT/wrappers/tokens.py
import os
import hmac
import hashlib
import base64
import secrets
from datetime import datetime, timedelta, timezone
from typing import Dict, Tuple

# Config via env
SECRET = os.environ.get("CLOUDVAULT_WRAPPER_SECRET", "dev-secret-please-change")
ISSUER = os.environ.get("CLOUDVAULT_WRAPPER_ISSUER", "cloudvault.local")
DEFAULT_TTL = int(os.environ.get("CLOUDVAULT_WRAPPER_TTL", "3600"))  # seconds


def _base64url_encode(b: bytes) -> str:
    return base64.urlsafe_b64encode(b).decode("ascii").rstrip("=")


def _base64url_decode(s: str) -> bytes:
    padding = "=" * ((4 - len(s) % 4) % 4)
    return base64.urlsafe_b64decode(s + padding)


def _now_utc_iso_z(dt: datetime = None) -> str:
    if dt is None:
        dt = datetime.now(timezone.utc)
    return dt.replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _gen_nonce_hex8() -> str:
    # 4 bytes -> 8 hex chars
    return secrets.token_hex(4)


def _build_payload(context_id: str, expires_at: str, nonce: str, issuer: str) -> str:
    # exact spec: "{context_id}|{expires_at}|{nonce}|{issuer}"
    return f"{context_id}|{expires_at}|{nonce}|{issuer}"


def _compute_hmac(secret: str, payload: str) -> bytes:
    return hmac.new(secret.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256).digest()


def generate_wrapper_token(context_id: str, issuer: str = None, ttl_seconds: int = None) -> Dict:
    """
    Return a locator dict:
    { context_id, token (base64url), nonce, expires_at (ISO Z), issuer }
    """
    if issuer is None:
        issuer = ISSUER
    if ttl_seconds is None:
        ttl_seconds = DEFAULT_TTL

    expires = datetime.now(timezone.utc) + timedelta(seconds=ttl_seconds)
    expires_at = _now_utc_iso_z(expires)
    nonce = _gen_nonce_hex8()
    payload = _build_payload(context_id, expires_at, nonce, issuer)
    mac = _compute_hmac(SECRET, payload)
    token = _base64url_encode(mac)
    return {"context_id": context_id, "token": token, "nonce": nonce, "expires_at": expires_at, "issuer": issuer}


def validate_wrapper_token(context_id: str, token: str, nonce: str, expires_at: str, issuer: str) -> Tuple[bool, str]:
    """
    Validate the provided parts. Returns (ok, reason).
    reason is empty string on success or a short code: "expired","invalid_hmac","bad_expires_format"
    """
    # parse expiry
    try:
        exp = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
    except Exception:
        return False, "bad_expires_format"

    if datetime.now(timezone.utc) > exp:
        return False, "expired"

    payload = _build_payload(context_id, expires_at, nonce, issuer)
    expected_mac = _compute_hmac(SECRET, payload)
    try:
        provided = _base64url_decode(token)
    except Exception:
        return False, "invalid_hmac"

    if not hmac.compare_digest(expected_mac, provided):
        return False, "invalid_hmac"

    return True, ""
