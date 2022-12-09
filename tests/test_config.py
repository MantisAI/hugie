import os

import pytest
import srsly
from hugie.config import app
from hugie.models import InferenceEndpointConfig
from typer.testing import CliRunner

from common import INCOMPLETE_JSON

runner = CliRunner()


@pytest.fixture(scope="function")
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
    srsly.write_json(data_path, data)

    return data_path


def test_inference_endpoint_config_serialization(data_path):
    config = InferenceEndpointConfig.from_json(data_path)
    config = config.dict()
    assert isinstance(config, dict)
    assert config["compute"]["instanceSize"] == "small"
    assert config["model"]["framework"] == "custom"
    assert config["model"]["image"]["huggingface"] == {}
    assert config["name"] == "development"
    assert config["provider"]["region"] == "us-east-1"


def test_modify_writes_to_stdout(data_path):
    result = runner.invoke(app, [data_path, "--instancesize", "medium"])
    assert "medium" in result.stdout
    assert result.exit_code == 0


def test_modify_overwrite_input_json(data_path):
    result = runner.invoke(app, [data_path, "--instancesize", "medium", "--overwrite"])

    config = srsly.read_json(data_path)
    assert result.exit_code == 0
    assert os.path.exists(data_path)
    assert config["compute"]["instanceSize"] == "medium"


def test_fail_on_invalid_json(data_path):
    result = runner.invoke(app, [INCOMPLETE_JSON, "modify"])

    assert result.exit_code > 0
