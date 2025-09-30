# E:\Surya__AI_Apps\cloudvault\cloud\app\contextvault_adapter.py
"""
Adapter module that exposes create_context, list_contexts, get_context and
prefers delegating to the `contextvault` core lib when available.

Extended: adds delete_context(ctx_id) and rename_context(ctx_id, new_name),
with safe fallbacks if the core lib is absent.
"""

from pathlib import Path
import hashlib
import uuid
import zipfile
import os
import tempfile
from typing import List, Dict, Any, Optional
from datetime import datetime

# Optional core lib (tests monkeypatch adapter.contextvault)
try:
    import contextvault  # type: ignore
except Exception:
    contextvault = None  # tests may set this attribute dynamically

# Config via env (module-level)
STORAGE_ROOT = Path(os.getenv("STORAGE_ROOT", "./storage")).resolve()
STORAGE_ROOT.mkdir(parents=True, exist_ok=True)

# in-memory metadata store (fallback)
# meta shape (fallback):
# {
#   "id": <str>,
#   "sha256": <str>,
#   "zip_path": <str>,
#   "name": <str>,            # optional (defaulted on create)
#   "created_at": <iso8601>,  # optional (defaulted on create)
#   "extracted_path": <str>,  # optional
# }
_contexts: Dict[str, Dict[str, Any]] = {}


def _sha256_of_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def _fallback_create_from_bytes_list(file_bytes_list: List[bytes], filename_list: List[str]) -> Dict[str, Any]:
    """
    Create a single context from bytes (fallback implementation).
    Returns metadata dict with id, sha256, zip_path, name, created_at.
    """
    ctx_id = str(uuid.uuid4())
    zip_path = STORAGE_ROOT / f"{ctx_id}.zip"

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for b, fn in zip(file_bytes_list, filename_list):
            zf.writestr(fn or "file", b)

    sha = _sha256_of_file(zip_path)
    # choose the first non-empty filename as display name
    display_name = next((fn for fn in filename_list if fn), ctx_id)
    meta = {
        "id": ctx_id,
        "sha256": sha,
        "zip_path": str(zip_path),
        "name": display_name,
        "created_at": datetime.utcnow().isoformat() + "Z",
    }
    _contexts[ctx_id] = meta
    return meta


def create_context(files: List) -> Dict[str, Any]:
    """
    Create context(s) from a list of UploadFile-like objects.
    - If contextvault core lib is available, prefer calling its create/ingest API.
    - Returns a single metadata dict for the (first) context created.
    """
    if not files:
        raise ValueError("no files provided")

    # Read bytes & filenames for fallback possibility (but prefer core lib)
    file_bytes_list = []
    filename_list = []
    for upload in files:
        # many UploadFile-like objects expose .file (a file-like) or an async read() method.
        # For our adapter we handle the common sync .file.read() and fallback to upload.read() if present.
        data = None
        if hasattr(upload, "file") and hasattr(upload.file, "read"):
            # ensure file pointer is at start
            try:
                upload.file.seek(0)
            except Exception:
                pass
            data = upload.file.read()
        elif hasattr(upload, "read"):
            # could be sync or async; support sync
            try:
                data = upload.read()
            except TypeError:
                # async read; not expected in our adapter tests
                raise RuntimeError("async UploadFile.read() not supported by adapter create_context")
        else:
            raise ValueError("upload object has no readable content")
        file_bytes_list.append(data)
        filename_list.append(getattr(upload, "filename", "file"))

    # If a core contextvault library is available, call it.
    if contextvault is not None:
        # We call the core library with the first file as a temp file path (many APIs accept a path)
        try:
            with tempfile.NamedTemporaryFile(delete=False) as tf:
                tf.write(file_bytes_list[0])
                tmp_path = tf.name
            # try common API names defensively
            if hasattr(contextvault, "create_context"):
                try:
                    meta = contextvault.create_context(tmp_path, storage_root=str(STORAGE_ROOT))
                    return meta
                except Exception:
                    pass
            if hasattr(contextvault, "ingest_file"):
                try:
                    meta = contextvault.ingest_file(tmp_path, storage_root=str(STORAGE_ROOT))
                    return meta
                except Exception:
                    pass
            # nested namespaces
            attr = getattr(contextvault, "api", None)
            if attr and hasattr(attr, "create_context"):
                try:
                    meta = attr.create_context(tmp_path, storage_root=str(STORAGE_ROOT))
                    return meta
                except Exception:
                    pass
            # If the core lib exists but none of the entrypoints succeeded, fall back to local zip.
        finally:
            try:
                os.remove(tmp_path)
            except Exception:
                pass

    # Fallback: use local zip creation
    return _fallback_create_from_bytes_list(file_bytes_list, filename_list)


def list_contexts() -> List[Dict[str, Any]]:
    """
    Return list of stored contexts (fallback) or call core lib if available.
    The returned items must include 'id' and 'sha256'.
    May include 'name' and 'created_at' if available.
    """
    if contextvault is not None and hasattr(contextvault, "list_contexts"):
        try:
            return contextvault.list_contexts()
        except Exception:
            pass
    # fallback
    out: List[Dict[str, Any]] = []
    for v in _contexts.values():
        item = {"id": v.get("id"), "sha256": v.get("sha256")}
        # include optional fields if present (non-breaking)
        if "name" in v:
            item["name"] = v["name"]
        if "created_at" in v:
            item["created_at"] = v["created_at"]
        out.append(item)
    return out


def get_context(ctx_id: str) -> Optional[Dict[str, Any]]:
    """
    Return stored context metadata (fallback) or None.
    """
    if contextvault is not None and hasattr(contextvault, "get_context"):
        try:
            return contextvault.get_context(ctx_id)
        except Exception:
            pass
    return _contexts.get(ctx_id)


# ---------------------------
# New: delete & rename APIs
# ---------------------------

def delete_context(ctx_id: str) -> bool:
    """
    Delete context metadata and associated files (zip and extracted folder).
    Returns True if deleted, False if not found.
    Delegates to core lib if available.
    """
    if contextvault is not None and hasattr(contextvault, "delete_context"):
        try:
            return bool(contextvault.delete_context(ctx_id))
        except Exception:
            # fall back if core lib errors out
            pass

    meta = _contexts.pop(ctx_id, None)
    if not meta:
        return False

    # Best-effort file cleanup
    try:
        zip_path = meta.get("zip_path")
        if zip_path and os.path.exists(zip_path):
            os.remove(zip_path)
        extracted = meta.get("extracted_path")
        if extracted and os.path.exists(extracted):
            # remove extracted directory recursively
            import shutil
            shutil.rmtree(extracted, ignore_errors=True)
    except Exception:
        # swallow exceptions — deletion is best-effort
        pass

    return True


def rename_context(ctx_id: str, new_name: str) -> Optional[Dict[str, Any]]:
    """
    Rename a context (display name). Returns updated metadata or None if not found.
    Delegates to core lib if available.
    """
    if not new_name:
        return None

    if contextvault is not None and hasattr(contextvault, "rename_context"):
        try:
            updated = contextvault.rename_context(ctx_id, new_name)
            # Expect the core lib to return updated metadata; if it returns True/False, we adapt
            if isinstance(updated, dict):
                return updated
            if updated:
                # Try to fetch fresh meta from core
                if hasattr(contextvault, "get_context"):
                    try:
                        return contextvault.get_context(ctx_id)
                    except Exception:
                        pass
                return {"id": ctx_id, "name": new_name}
            return None
        except Exception:
            # fall back if core lib errors out
            pass

    meta = _contexts.get(ctx_id)
    if not meta:
        return None
    meta["name"] = new_name
    return meta
