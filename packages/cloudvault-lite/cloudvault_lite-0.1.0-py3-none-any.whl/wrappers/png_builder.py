# CLOUDVAULT/wrappers/png_builder.py
from io import BytesIO
from typing import Dict
import json
import zlib
from PIL import Image
import qrcode

TEXT_CHUNK_KEY = "contextvault-wrapper"


def _add_itxt_chunk(png_bytes: bytes, key: str, text: str) -> bytes:
    """
    Insert an iTXt chunk containing UTF-8 text before IEND.
    Follows PNG iTXt structure exactly.
    """
    keyword = key.encode("latin1", errors="ignore")
    compression_flag = b"\x00"       # 1 byte: 0 = uncompressed
    compression_method = b"\x00"     # 1 byte: must be present
    lang_tag = b""
    translated_keyword = b""
    text_bytes = text.encode("utf-8")

    # Build iTXt data. Note the separators per spec.
    data = (
        keyword + b"\x00" +
        compression_flag +
        compression_method +
        b"\x00" +                # separator after compression_method
        lang_tag + b"\x00" +
        translated_keyword + b"\x00" +
        text_bytes
    )

    chunk_type = b"iTXt"
    length = len(data).to_bytes(4, "big")
    crc_val = zlib.crc32(chunk_type + data) & 0xFFFFFFFF
    crc = crc_val.to_bytes(4, "big")

    idx = png_bytes.rfind(b"IEND")
    if idx == -1:
        raise ValueError("Invalid PNG: IEND not found")
    iend_pos = idx - 4
    before = png_bytes[:iend_pos]
    after = png_bytes[iend_pos:]
    return before + length + chunk_type + data + crc + after


def build_wrapper_png(preview_bytes: bytes, locator_json: Dict, qr_size: int = 200) -> bytes:
    """
    Compose preview image and overlay a QR encoding locator_json (compact).
    Embed the same compact JSON in an iTXt chunk with key TEXT_CHUNK_KEY.
    Returns PNG bytes.
    """
    preview = Image.open(BytesIO(preview_bytes)).convert("RGBA")
    w, h = preview.size

    locator_compact = json.dumps(locator_json, separators=(",", ":"))

    # QR
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M)
    qr.add_data(locator_compact)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")
    qr_img = qr_img.resize((qr_size, qr_size))

    # paste QR bottom-right
    margin = 8
    x = max(w - qr_size - margin, margin)
    y = max(h - qr_size - margin, margin)
    composed = Image.new("RGBA", (w, h), (255, 255, 255, 255))
    composed.paste(preview, (0, 0))
    composed.paste(qr_img, (x, y), qr_img)

    buf = BytesIO()
    composed.save(buf, format="PNG")
    png_bytes = buf.getvalue()

    # embed locator JSON in iTXt
    return _add_itxt_chunk(png_bytes, TEXT_CHUNK_KEY, locator_compact)


def extract_locator_from_png(png_bytes: bytes) -> Dict:
    """
    Extract locator JSON from iTXt chunk key TEXT_CHUNK_KEY.
    Returns parsed dict or raises ValueError if not found/parse error.
    """
    n = len(png_bytes)
    if n < 8:
        raise ValueError("Invalid PNG")

    i = 8  # skip PNG header
    while i + 8 <= n:
        length = int.from_bytes(png_bytes[i:i+4], "big")
        ctype = png_bytes[i+4:i+8]
        i += 8
        if i + length + 4 > n:
            break
        data = png_bytes[i:i+length]
        i += length
        crc = png_bytes[i:i+4]
        i += 4

        if ctype == b"iTXt":
            # parts: keyword\x00 compressionflag (1 byte) compressionmethod (1 byte) \x00 langtag \x00 translatedkeyword \x00 text
            # We'll split at nulls - get up to 6 parts (keyword, compflag+compmethod? etc.)
            parts = data.split(b"\x00", 5)
            if len(parts) >= 6:
                keyword = parts[0].decode("latin1", errors="ignore")
                text_bytes = parts[5]
                if keyword == TEXT_CHUNK_KEY:
                    raw = text_bytes.decode("utf-8", errors="ignore")
                    # Defensive: strip leading null if present
                    if raw.startswith("\x00"):
                        raw = raw[1:]
                    return json.loads(raw)

    raise ValueError("locator iTXt chunk not found")
