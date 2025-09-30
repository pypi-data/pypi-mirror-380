# E:\Surya__AI_Apps\cloudvault\tests\test_api_contexts.py
import pytest
from fastapi.testclient import TestClient
from cloud.app.main import app
import os

client = TestClient(app)

def test_signup_upload_list_rename_delete(tmp_path):
    # signup
    r = client.post("/auth/signup", json={"email": "t@t.com", "password": "p"})
    assert r.status_code == 200
    token = r.json().get("access_token")
    assert token

    headers = {"Authorization": f"Bearer {token}"}

    # list contexts (should be list)
    r = client.get("/api/contexts", headers=headers)
    assert r.status_code == 200
    assert isinstance(r.json(), list)

    # upload a small file
    f = tmp_path / "x.txt"
    f.write_text("hello")
    with open(f, "rb") as fh:
        r = client.post("/api/contexts", headers=headers, files={"files": ("x.txt", fh, "text/plain")})
    assert r.status_code in (200, 201)

    # list again, get an id
    r = client.get("/api/contexts", headers=headers)
    assert r.status_code == 200
    res_list = r.json()
    assert isinstance(res_list, list) and len(res_list) >= 1
    ctx_id = res_list[0]["id"]

    # rename
    r = client.patch(f"/api/contexts/{ctx_id}/rename", headers=headers, json={"name": "newname"})
    assert r.status_code == 200
    assert r.json().get("name") == "newname"

    # delete
    r = client.delete(f"/api/contexts/{ctx_id}", headers=headers)
    assert r.status_code == 204
