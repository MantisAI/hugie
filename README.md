# Huggingface Inference Endpoints helper

A Command Line Interface (CLI) for working with the Huggingface Inference Endpoints API.

See API docs: https://huggingface.co/docs/inference-endpoints/api_reference

# Getting started

The package is pip installable and can be installed directly from github with:

```
pip install git+https://github.com/MantisAI/hfie.git
```

# ENV vars

To get started, you must set your individual or organisation Huggingface token into an env var called `HUGGINGFACE_READ_TOKEN`.

# Usage

tldr; watch the video:

[![asciicast](https://asciinema.org/a/m2MyTRsJ1H6kaW2ygwr37qbh2.svg)](https: // asciinema.org/a/m2MyTRsJ1H6kaW2ygwr37qbh2)

# Getting help

```
hfie endpoint --help
>>>
Usage: hfie endpoint[OPTIONS] COMMAND[ARGS]...

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

To create an endpoint:

```
hfie endpoint create examples/development.json
```

To list all your endpoints:

```
hfie endpoint list

# Use --json option to view all content

hfie endpoint list --json
```

To update an endpoint, edit `examples/development.json`

```
hfie endpoint update development examples/development.json
```

To see the logs:

```
hfie endpoint logs development
```

To delete the endpoint

```
hfie endpoint delete development
```

# JSON format

The `endpoint create` and `endpoint update` commands both require JSONs of the fomat:

```json
{
  "accountId": null,
  "compute":
    "accelerator": "cpu",
    "instanceSize": "small",
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
    "repository": "t5-small",
    "revision": "main",
    "task": "text-classification"
  },
  "name": "aws-dev",
  "provider": {
    "region": "us-east-1",
    "vendor": "aws"
  },
  "type": "protected"
}
```

See `examples/development.json` for an example.

# For development

Create a virtual environment and install the package

```
make virtualenv
```
