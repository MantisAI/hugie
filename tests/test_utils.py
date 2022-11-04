import json
import os

import pytest

from hugie.utils import format_table, load_json


@pytest.fixture
def data_path(tmp_path):
    data_path = os.path.join(tmp_path, "data.json")
    with open(data_path, "w") as f:
        f.write(json.dumps({"data": "test"}))
    return data_path


def test_format_table():
    headers = ["name", "url"]
    names = ["google", "mantis"]
    urls = ["www.google.com", "www.mantisnlp.com"]
    format_table(headers, names, urls)


def test_load_json(data_path):
    load_json(data_path)
