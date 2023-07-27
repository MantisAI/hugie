import json
import os

import pytest
import requests
from hugie.endpoint import app
from typer.testing import CliRunner

runner = CliRunner()


@pytest.fixture
def data_path(tmp_path):
    data_path = os.path.join(tmp_path, "data.json")
    data = {
        "accountId": None,
        "compute": {
            "accelerator": "cpu",
            "instanceSize": "small",
            "instanceType": "c6i",
            "scaling": {"maxReplica": 1, "minReplica": 1},
        },
        "model": {
            "framework": "custom",
            "image": {"huggingface": {}},
            "repository": "t5-small",
            "revision": "main",
            "task": "translation",
        },
        "name": "development",
        "provider": {"region": "us-east-1", "vendor": "aws"},
        "type": "protected",
    }
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

        def raise_for_status():
            pass

        status_code = 200

    monkeypatch.setattr("requests.post", lambda url, **kwargs: MockCreateResponse)
    result = runner.invoke(app, ["create", data_path])
    assert result.exit_code == 0


def test_update(monkeypatch, data_path):
    class MockUpdateResponse:
        def json():
            pass

        def raise_for_status():
            pass

        status_code = 200

    monkeypatch.setattr("requests.put", lambda url, headers, json: MockUpdateResponse)
    result = runner.invoke(app, ["update", "test", data_path])
    assert result.exit_code == 0


def test_delete_force(monkeypatch):
    class MockDeleteResponse:
        def json():
            pass

        def raise_for_status():
            pass

    monkeypatch.setattr(
        "requests.delete", lambda url, headers, json: MockDeleteResponse
    )
    result = runner.invoke(app, ["delete", "test", "--force"])
    assert result.exit_code == 0


def test_delete_confirm(monkeypatch):
    class MockDeleteResponse:
        def json():
            pass

        def raise_for_status():
            pass

    monkeypatch.setattr(
        "requests.delete", lambda url, headers, json: MockDeleteResponse
    )
    result = runner.invoke(app, ["delete", "test"], input="y")
    assert result.exit_code == 0


def test_delete_no_confirm(monkeypatch):
    result = runner.invoke(app, ["delete", "test"], input="n")
    assert result.exit_code == 1


def test_delete_non_existing_endpoint(monkeypatch):
    class MockDeleteResponse:
        def json():
            pass

        def raise_for_status():
            raise requests.exceptions.RequestException

        status_code = 404

    monkeypatch.setattr(
        "requests.delete", lambda url, headers, json: MockDeleteResponse
    )
    result = runner.invoke(app, ["delete", "test"], input="y")
    assert result.exit_code == 0


def test_info(monkeypatch):
    class MockInfoResponse:
        def json():
            return {
                "name": "test",
                "status": {"state": "test", "url": "test"},
                "model": {"repository": "test", "revision": "test"},
            }

        def raise_for_status():
            pass

    monkeypatch.setattr("requests.get", lambda url, headers, json: MockInfoResponse)
    result = runner.invoke(app, ["info", "test"])
    assert result.exit_code == 0


def test_logs(monkeypatch, data_path):
    class MockLogsResponse:
        def content():
            pass

        def raise_for_status():
            pass

    monkeypatch.setattr("requests.get", lambda url, headers, json: MockLogsResponse)
    result = runner.invoke(app, ["logs", "test"])
    assert result.exit_code == 0


def test_test(monkeypatch):
    class MockInfoResponse:
        def json():
            return {"status": {"url": "test"}}

        def raise_for_status():
            pass

    class MockPredictResponse:
        def json():
            pass

        def raise_for_status():
            pass

    monkeypatch.setattr("requests.get", lambda url, headers, json: MockInfoResponse)
    monkeypatch.setattr("requests.post", lambda url, headers, json: MockPredictResponse)
    result = runner.invoke(app, ["test", "name", "inputs"])
    assert result.exit_code == 0
