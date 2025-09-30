# cloud/tests/test_contextvault_adapter.py
import os
import sys
import shutil
from io import BytesIO
from types import SimpleNamespace

import pytest

# import the adapter module
from cloud.app import contextvault_adapter as adapter

class DummyUpload:
    """Minimal object matching the subset of FastAPI UploadFile used by adapter.create_context"""
    def __init__(self, filename: str, data: bytes):
        self.filename = filename
        self.file = BytesIO(data)

    # adapter implementation reads from upload.file.read(), not awaitable.
    # provide convenience for some usage patterns
    def read(self):
        return self.file.read()


@pytest.fixture(autouse=True)
def clean_adapter_env(tmp_path, monkeypatch):
    """
    Ensure adapter uses a temporary STORAGE_ROOT and a clean in-memory _contexts map.
    """
    # override STORAGE_ROOT path used by the adapter
    monkeypatch.setattr(adapter, "STORAGE_ROOT", tmp_path, raising=False)
    # clear in-memory contexts
    adapter._contexts.clear()
    yield
    # cleanup dir
    if tmp_path.exists():
        shutil.rmtree(str(tmp_path), ignore_errors=True)


def test_fallback_create_zip_and_meta_creates_zip_and_metadata(tmp_path):
    # create a dummy upload and call create_context
    u = DummyUpload("sample.txt", b"hello world\nline two")
    meta = adapter.create_context([u])  # adapter returns {'id','sha256'} according to extraction

    assert isinstance(meta, dict)
    assert "id" in meta and "sha256" in meta
    ctx_id = meta["id"]
    # zip file should exist under STORAGE_ROOT
    zip_path = adapter._contexts[ctx_id]["zip_path"]
    assert os.path.exists(zip_path)
    # sha length 64 (sha256 hex)
    assert isinstance(meta["sha256"], str) and len(meta["sha256"]) == 64


def test_list_and_get_contexts_return_expected():
    # create two dummy contexts by calling create_context twice
    u1 = DummyUpload("a.txt", b"A")
    u2 = DummyUpload("b.txt", b"B")
    m1 = adapter.create_context([u1])
    m2 = adapter.create_context([u2])

    items = adapter.list_contexts()
    assert isinstance(items, list)
    ids = {it["id"] for it in items}
    assert m1["id"] in ids and m2["id"] in ids

    # get_context
    got = adapter.get_context(m1["id"])
    assert got is not None
    assert got["id"] == m1["id"]
    assert "zip_path" in got


def test_adapter_prefers_contextvault_when_available(monkeypatch, tmp_path):
    """
    If a real contextvault module is present with a create_context callable,
    adapter.create_context should call it and return its result (we mock it).
    """
    # Prepare fake contextvault module
    called = {}

    def fake_create_context(path, storage_root=None):
        # Record the path and whether it existed at the time of the call.
        called['path'] = path
        called['existed_at_call'] = os.path.exists(path)
        # Return mocked metadata (core lib would return similar mapping)
        return {"id": "fake-id-123", "sha256": "f" * 64, "zip_path": str(tmp_path / "fake.zip")}

    fake_module = SimpleNamespace(create_context=fake_create_context)
    # monkeypatch adapter's contextvault reference
    monkeypatch.setattr(adapter, "contextvault", fake_module, raising=False)

    u = DummyUpload("x.txt", b"data")
    meta = adapter.create_context([u])

    assert meta["id"] == "fake-id-123"
    assert meta["sha256"] == "f" * 64
    # ensure our fake_create_context was called with a temp file path and that file existed during the call
    assert "path" in called and isinstance(called["path"], str)
    assert called.get("existed_at_call", False) is True
