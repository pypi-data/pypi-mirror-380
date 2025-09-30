from fastapi import FastAPI, File, UploadFile, Depends, HTTPException, Header
from fastapi.responses import FileResponse, JSONResponse
from typing import List, Optional
import uuid
from fastapi import Path, Body
from wrappers.routes_wrapper import router as wrappers_router

from cloud.app.contextvault_adapter import (
    create_context,
    list_contexts,
    get_context,
    delete_context,
    rename_context,
)

app = FastAPI(title="ContextVault - Minimal Test API (CI)")

app.include_router(wrappers_router)

from fastapi.middleware.cors import CORSMiddleware

# allow the Vite dev server origin and localhost (Electron loads remote too)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",   # optional if you change ports
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

_users = {}
_tokens = {}

def require_auth(authorization: Optional[str] = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")
    parts = authorization.split()
    if len(parts) != 2 or parts[0].lower() != "bearer":
        raise HTTPException(status_code=401, detail="Invalid Authorization header")
    token = parts[1]
    if token not in _tokens:
        raise HTTPException(status_code=401, detail="Invalid token")
    return _tokens[token]

@app.post("/auth/signup")
async def signup(payload: dict):
    email = payload.get("email")
    password = payload.get("password")
    if not email or not password:
        raise HTTPException(status_code=400, detail="email and password required")
    token = str(uuid.uuid4())
    _users[email] = {"password": password, "token": token}
    _tokens[token] = email
    return {"access_token": token}

@app.post("/api/contexts")
async def api_create_context(files: List[UploadFile] = File(...), current_user: str = Depends(require_auth)):
    return create_context(files)

@app.get("/api/contexts")
async def api_list_contexts(current_user: str = Depends(require_auth)):
    return list_contexts()

@app.get("/api/contexts/{ctx_id}/download")
async def api_download_context(ctx_id: str, current_user: str = Depends(require_auth)):
    meta = get_context(ctx_id)
    if not meta:
        raise HTTPException(status_code=404, detail="Context not found")
    return FileResponse(path=meta["zip_path"], filename=f"{ctx_id}.zip", media_type="application/zip")

@app.get("/")
async def root():
    return JSONResponse({"status": "ok", "message": "ContextVault minimal API (for CI/tests)"})

@app.delete("/api/contexts/{ctx_id}", status_code=204)
async def api_delete_context(
    ctx_id: str = Path(...),
    current_user: str = Depends(require_auth),
):
    deleted = delete_context(ctx_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Context not found")
    # 204 No Content
    return JSONResponse(status_code=204, content=None)

@app.patch("/api/contexts/{ctx_id}/rename")
async def api_rename_context(
    ctx_id: str = Path(...),
    payload: dict = Body(...),
    current_user: str = Depends(require_auth),
):
    new_name = payload.get("name")
    if not new_name:
        raise HTTPException(status_code=400, detail="Missing 'name' in payload")
    updated = rename_context(ctx_id, new_name)
    if not updated:
        raise HTTPException(status_code=404, detail="Context not found")
    return updated

# ---- add to cloud/app/main.py ----
from fastapi import Query

@app.get("/api/contexts/search")
async def api_search_contexts(q: str = Query("", description="Search query"), limit: int = 50, current_user: str = Depends(require_auth)):
    """
    Simple search endpoint that filters contexts by id or name (case-insensitive substring).
    Returns up to `limit` results.
    """
    all_contexts = list_contexts() or []
    if not q:
        return all_contexts[:limit]
    ql = q.lower()
    def matches(c):
        # support both shapes: c.id or c.get("id") and c.name
        name = c.get("name") if isinstance(c, dict) else getattr(c, "name", "")
        cid = c.get("id") if isinstance(c, dict) else getattr(c, "id", "")
        return (cid and ql in str(cid).lower()) or (name and ql in str(name).lower())
    filtered = [c for c in all_contexts if matches(c)]
    return filtered[:limit]
# ----------------------------------
