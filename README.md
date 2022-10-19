# HF Endpoints

A CLI interface for working with the HuggingFace Inference API.

See API docs: https://huggingface.co/docs/inference-endpoints/api_reference

# Getting started

The package is pip installable and can be installed directly from github with:

```
pip install git+https://github.com/MantisAI/hfie.git
```

# Usage

See the demo for a sense of what it can do:

[![asciicast](https://asciinema.org/a/m2MyTRsJ1H6kaW2ygwr37qbh2.svg)](https://asciinema.org/a/m2MyTRsJ1H6kaW2ygwr37qbh2)

```
hfie endpoint --help
>>>
Usage: hfie endpoint [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  create  Create an endpoint
  delete  Delete an endpoint
  info    Get info about an endpoint
  list    List all the deployed endpoints
  logs    Get logs about an endpoint
  test    Test and endpoint
  update  Update an endpoint

```

# JSON format

The `endpoint create` and `endpoint update` commands both require JSONs of the fomat:

```json
{
  "accountId": null,
  "compute": {
    "accelerator": "cpu",
    "instanceSize": "large",
    "instanceType": "c6i",
    "scaling": {
      "maxReplica": 1,
      "minReplica": 1
    }
  },
  "model": {
    "framework": "custom",
    "image": {
      "huggingface": {}
    },
    "repository": "mantisnlp/oms_nlu",
    "revision": "db5af7357469e6d31e909d18faeeeff5efb40ec5",
    "task": "text-classification"
  },
  "name": "aws-oms-nlu-dev",
  "provider": {
    "region": "us-east-1",
    "vendor": "aws"
  },
  "type": "protected"
}
```

# For development

Create a virtual environment and install the package

```
make virtualenv
```

