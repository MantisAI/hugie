import json
import os

from typer.testing import CliRunner
import pytest

from hfie.endpoint import app

runner = CliRunner()


@pytest.fixture
def data_path(tmp_path):
    data_path = os.path.join(tmp_path, "data.json")
    data = {}
    with open(data_path, "w") as f:
        f.write(json.dumps(data))
    return data_path


def test_list(monkeypatch):
    class MockListResponse:
        def json():
            return {
                "items": [
                    {
                        "name": "test",
                        "status": {"state": "test", "url": "test"},
                        "model": {"repository": "test", "revision": "test"},
                    }
                ]
            }

    monkeypatch.setattr("requests.get", lambda url, headers: MockListResponse)
    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0


def test_create(monkeypatch, data_path):
    class MockCreateResponse:
        def json():
            pass

    monkeypatch.setattr("requests.post", lambda url, headers, json: MockCreateResponse)
    result = runner.invoke(app, ["create", data_path])
    assert result.exit_code == 0


def test_update(monkeypatch, data_path):
    class MockUpdateResponse:
        def json():
            pass

    monkeypatch.setattr("requests.put", lambda url, headers, json: MockUpdateResponse)
    result = runner.invoke(app, ["update", "test", data_path])
    assert result.exit_code == 0


def test_delete_force(monkeypatch):
    class MockDeleteResponse:
        def json():
            pass

    monkeypatch.setattr("requests.delete", lambda url, headers: MockDeleteResponse)
    result = runner.invoke(app, ["delete", "test", "--force"])
    assert result.exit_code == 0


def test_delete_confirm(monkeypatch):
    class MockDeleteResponse:
        def json():
            pass

    monkeypatch.setattr("requests.delete", lambda url, headers: MockDeleteResponse)
    result = runner.invoke(app, ["delete", "test"], input="y")
    print(result.stdout)
    assert result.exit_code == 0


def test_delete_no_confirm(monkeypatch):
    class MockDeleteResponse:
        def json():
            pass

    monkeypatch.setattr("requests.delete", lambda url, headers: MockDeleteResponse)
    result = runner.invoke(app, ["delete", "test"], input="n")
    assert result.exit_code == 1


def test_info(monkeypatch):
    class MockInfoResponse:
        def json():
            return {
                "name": "test",
                "status": {"state": "test", "url": "test"},
                "model": {"repository": "test", "revision": "test"},
            }

    monkeypatch.setattr("requests.get", lambda url, headers: MockInfoResponse)
    result = runner.invoke(app, ["info", "test"])
    assert result.exit_code == 0


def test_logs(monkeypatch, data_path):
    class MockLogsResponse:
        def content():
            pass

    monkeypatch.setattr("requests.get", lambda url, headers: MockLogsResponse)
    result = runner.invoke(app, ["logs", "test"])
    assert result.exit_code == 0


def test_test(monkeypatch):
    class MockInfoResponse:
        def json():
            return {"status": {"url": "test"}}

    class MockPredictResponse:
        def json():
            pass

    monkeypatch.setattr("requests.get", lambda url, headers: MockInfoResponse)
    monkeypatch.setattr("requests.post", lambda url, headers, json: MockPredictResponse)
    result = runner.invoke(app, ["test", "name", "inputs"])
    assert result.exit_code == 0
