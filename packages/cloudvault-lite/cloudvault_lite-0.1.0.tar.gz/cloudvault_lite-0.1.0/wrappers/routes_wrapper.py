# CLOUDVAULT/wrappers/routes_wrapper.py
from fastapi import APIRouter, File, UploadFile, Body, HTTPException, Response, status, Request
from fastapi.responses import JSONResponse
from typing import Optional
import os
import io
import json
import urllib.parse
import base64

from .tokens import generate_wrapper_token, validate_wrapper_token
from .png_builder import build_wrapper_png, extract_locator_from_png

router = APIRouter()

# Optional small persist file support - disabled by default
WRAPPER_PERSIST_FILE = os.environ.get("WRAPPER_PERSIST_FILE", "")  # path to JSON file if you want persist
CONTEXTVAULT_CANONICAL_BASE = os.environ.get("CONTEXTVAULT_CANONICAL_BASE", "")


def _load_persist_rows():
    if not WRAPPER_PERSIST_FILE:
        return []
    try:
        import json as _json
        if os.path.exists(WRAPPER_PERSIST_FILE):
            with open(WRAPPER_PERSIST_FILE, "r", encoding="utf-8") as f:
                return _json.load(f) or []
    except Exception:
        pass
    return []


def _append_persist_row(row: dict):
    if not WRAPPER_PERSIST_FILE:
        return
    import json as _json
    rows = _load_persist_rows()
    rows.append(row)
    tmp = WRAPPER_PERSIST_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        _json.dump(rows, f)
    os.replace(tmp, WRAPPER_PERSIST_FILE)


def datetime_now_iso():
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


@router.get("/wrappers/api/contexts/{context_id}/wrapper")
def get_wrapper(context_id: str):
    """
    Generate wrapper PNG bytes for a context id and return image/png.
    Stateless token issued and embedded in PNG.
    """
    # issuer default
    issuer = os.environ.get("WRAPPER_ISSUER", "cloudvault.local")

    locator = generate_wrapper_token(context_id, issuer=issuer, ttl_seconds=int(os.environ.get("WRAPPER_TTL", "3600")))

    # choose preview if provided
    preview_path = os.environ.get("WRAPPER_PREVIEW_PATH", "")
    if preview_path and os.path.exists(preview_path):
        preview_bytes = open(preview_path, "rb").read()
    else:
        # create simple white preview image
        from PIL import Image, ImageDraw, ImageFont
        img = Image.new("RGBA", (800, 600), (255, 255, 255, 255))
        draw = ImageDraw.Draw(img)
        label = f"Context: {context_id}"
        try:
            font = ImageFont.truetype("arial.ttf", 20)
        except Exception:
            font = None
        draw.text((16, 16), label, fill=(0, 0, 0, 255), font=font)
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        preview_bytes = buf.getvalue()

    png_bytes = build_wrapper_png(preview_bytes, locator, qr_size=200)

    # optional: persist issued token record
    if WRAPPER_PERSIST_FILE:
        _append_persist_row({
            "token": locator["token"],
            "context_id": locator["context_id"],
            "nonce": locator["nonce"],
            "expires_at": locator["expires_at"],
            "issuer": locator["issuer"],
            "issued_at": datetime_now_iso()
        })

    return Response(content=png_bytes, media_type="image/png")


# Server-side QR decode helper
def _decode_qr_from_image_bytes(image_bytes: bytes) -> Optional[str]:
    """
    Try decode QR from image bytes. Returns the decoded text or None.
    Uses pyzbar if available; otherwise returns None.
    """
    try:
        from pyzbar.pyzbar import decode as zbar_decode
        from PIL import Image
    except Exception:
        return None

    try:
        img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        decoded = zbar_decode(img)
        if not decoded:
            return None
        # return first result's data as text
        return decoded[0].data.decode("utf-8")
    except Exception:
        return None


def _base64url_decode_to_text(s: str) -> Optional[str]:
    """
    Decode base64url-encoded string to UTF-8 text. Returns None on error.
    """
    if not s:
        return None
    try:
        padding = "=" * ((4 - len(s) % 4) % 4)
        b = base64.urlsafe_b64decode(s + padding)
        return b.decode("utf-8")
    except Exception:
        return None


@router.post("/wrappers/api/contexts/resolve-from-wrapper")
async def resolve_from_wrapper(request: Request, uploaded_file: UploadFile = File(None), locator_json: str = Body(None)):
    """
    Accept uploaded wrapper PNG or direct locator JSON, verify HMAC+expiry, and return context_id + enc_url.
    Extended behavior:
      - If uploaded PNG contains iTXt locator chunk, extract it.
      - If iTXt absent, attempt to decode QR from image (pyzbar).
      - If decoded QR text is JSON, parse it as locator JSON.
      - If decoded QR text is a deeplink URL containing '?d=<base64url>', extract & decode that.
      - If decoded QR text is plain context_id, treat as resolved (no token validation).
      - If locator includes token fields, validate them.
    """
    locator = None

    if uploaded_file:
        data = await uploaded_file.read()

        # 1) Try PNG iTXt extraction first
        try:
            locator = extract_locator_from_png(data)
        except Exception:
            locator = None

        # 2) If not found, try server-side QR decoding
        if locator is None:
            decoded_text = _decode_qr_from_image_bytes(data)
            if decoded_text:
                # try parse as JSON
                try:
                    locator = json.loads(decoded_text)
                except Exception:
                    locator = None

                # If still None and decoded_text looks like URL, try to extract 'd' or 'data' query param (base64url)
                if locator is None:
                    try:
                        parsed = urllib.parse.urlparse(decoded_text)
                        if parsed.scheme and parsed.netloc:
                            q = urllib.parse.parse_qs(parsed.query)
                            # common param names we might use
                            for param in ("d", "data", "payload"):
                                if param in q and q[param]:
                                    possible = q[param][0]
                                    txt = _base64url_decode_to_text(possible)
                                    if txt:
                                        try:
                                            locator = json.loads(txt)
                                        except Exception:
                                            # if not JSON, maybe it's plain context id inside
                                            locator = {"context_id": txt}
                                        break
                            # also check fragment (after #) for bare payload
                            if locator is None and parsed.fragment:
                                frag = parsed.fragment
                                txt = _base64url_decode_to_text(frag)
                                if txt:
                                    try:
                                        locator = json.loads(txt)
                                    except Exception:
                                        locator = {"context_id": txt}
                    except Exception:
                        locator = None

                # If still not a JSON locator, treat decoded_text as a plain context id
                if locator is None:
                    locator = {"context_id": decoded_text}

    elif locator_json:
        try:
            locator = json.loads(locator_json)
        except Exception:
            raise HTTPException(status_code=400, detail="bad_locator_json")
    else:
        # try reading raw body
        body = await request.body()
        if body:
            try:
                locator = json.loads(body.decode("utf-8"))
            except Exception:
                pass

    if not locator:
        raise HTTPException(status_code=400, detail="no_locator_provided")

    # If locator contains token fields, validate cryptographically
    if locator.get("token"):
        ok, reason = validate_wrapper_token(locator.get("context_id"), locator.get("token"), locator.get("nonce"), locator.get("expires_at"), locator.get("issuer"))
        if not ok:
            if reason == "expired":
                raise HTTPException(status_code=status.HTTP_410_GONE, detail="token_expired")
            elif reason == "bad_expires_format":
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=reason)
            else:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="token_invalid")

    # If only context_id present, we consider that resolved (no token check)
    ctx_id = locator.get("context_id")
    if not ctx_id:
        raise HTTPException(status_code=400, detail="no_context_id_found")

    # build canonical enc_url
    if CONTEXTVAULT_CANONICAL_BASE:
        enc_url = f"{CONTEXTVAULT_CANONICAL_BASE.rstrip('/')}/contexts/{ctx_id}.png.enc"
    else:
        enc_url = f"/contexts/{ctx_id}.png.enc"

    return JSONResponse({"context_id": ctx_id, "enc_url": enc_url})
