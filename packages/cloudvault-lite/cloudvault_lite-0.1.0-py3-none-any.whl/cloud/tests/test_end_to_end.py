# cloud/tests/test_end_to_end.py
import os
import shutil
import pytest
from fastapi.testclient import TestClient

# Import the FastAPI app
from cloud.app.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def clean_env(tmp_path, monkeypatch):
    """
    Setup clean environment for each test:
    - Use a temporary SQLite file
    - Use a temporary storage root
    """
    db_file = tmp_path / "metadata_test.db"
    storage_dir = tmp_path / "storage_test"
    storage_dir.mkdir()
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{db_file}")
    monkeypatch.setenv("STORAGE_ROOT", str(storage_dir))
    data_dir = tmp_path / "cloud" / "app" / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    yield
    if storage_dir.exists():
        shutil.rmtree(storage_dir, ignore_errors=True)


def signup_and_get_token(email="test@ci.local", password="pass"):
    resp = client.post("/auth/signup", json={"email": email, "password": password})
    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert "access_token" in body
    return body["access_token"]


def test_upload_list_download_roundtrip():
    token = signup_and_get_token()
    fixture_path = os.path.join(
        os.path.dirname(__file__), "..", "..", "spec", "test_fixtures", "sample.txt"
    )
    assert os.path.exists(fixture_path), "Missing fixture: spec/test_fixtures/sample.txt"

    with open(fixture_path, "rb") as fh:
        files = {"files": ("sample.txt", fh, "text/plain")}
        headers = {"Authorization": f"Bearer {token}"}
        resp = client.post("/api/contexts", files=files, headers=headers)
    assert resp.status_code == 200, resp.text
    meta = resp.json()
    assert "id" in meta and "sha256" in meta

    resp2 = client.get("/api/contexts", headers=headers)
    assert resp2.status_code == 200, resp2.text
    items = resp2.json()
    assert isinstance(items, list)
    assert len(items) >= 1

    ctx_id = meta["id"]
    dl = client.get(f"/api/contexts/{ctx_id}/download", headers=headers)
    assert dl.status_code == 200
    content_type = dl.headers.get("content-type", "")
    assert "application/zip" in content_type or dl.content[:2] == b"PK"
