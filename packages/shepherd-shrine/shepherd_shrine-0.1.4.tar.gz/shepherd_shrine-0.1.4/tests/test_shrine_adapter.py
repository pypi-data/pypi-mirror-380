import json
from shepherd_model import shrine_adapter


def test_shrine_adapter_mock_accepts_event(tmp_path, monkeypatch):
    monkeypatch.setenv("SHRINE_USE_MOCK", "1")
    event = {
        "id": "evt-1",
        "timestamp": "2025-09-29T12:00:00Z",
        "type": "register-event",
        "payload": {},
    }
    resp = shrine_adapter.shrine_submit(event)
    assert resp["status"] == "ok"
    assert resp["code"] == 0


def test_shrine_adapter_rejects_bad_input():
    # non-dict input should return 400
    resp = shrine_adapter.shrine_submit(None)  # type: ignore
    assert resp["status"] == "error"
    assert resp["code"] == 400


def test_shrine_adapter_http_mode(monkeypatch):
    class DummyResponse:
        def __init__(self, status_code, data):
            self.status_code = status_code
            self._data = data

        def json(self):
            return self._data

    def fake_post(url, json, timeout):
        assert url == "https://shrine.local/submit"
        return DummyResponse(
            200, {"status": "ok", "code": 0, "result": {"verdict": "ok"}}
        )

    monkeypatch.setenv("SHRINE_MODE", "http")
    monkeypatch.setenv("SHRINE_HTTP_URL", "https://shrine.local/submit")
    monkeypatch.setattr("shepherd_model.shrine_adapter.requests.post", fake_post)
    event = {
        "id": "evt-2",
        "timestamp": "2025-09-29T12:00:00Z",
        "type": "register-event",
        "payload": {},
    }
    resp = shrine_adapter.shrine_submit(event)
    assert resp["status"] == "ok"
    assert resp["code"] == 0


def test_shrine_adapter_module_mode_accepts_event(tmp_path, monkeypatch):
    # Create a minimal fake service-account file and point env to it
    sa = {"project_id": "test-project", "client_email": "svc@test.local"}
    p = tmp_path / "sa.json"
    p.write_text(json.dumps(sa), encoding="utf-8")
    monkeypatch.setenv("FIREBASE_SERVICE_ACCOUNT_PATH", str(p))
    monkeypatch.delenv("SHRINE_MODE", raising=False)
    event = {
        "id": "evt-3",
        "timestamp": "2025-09-29T12:00:00Z",
        "type": "register-event",
        "payload": {},
    }
    resp = shrine_adapter.shrine_submit(event)
    assert resp["status"] == "ok"
    assert resp["code"] == 0
    assert resp["result"]["verdict"] == "module-accepted"
