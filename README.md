# Hugie 🐻

📖 Official [documentation](https://mantisai.github.io/hugie/)

Hugie is a Command Line Interface (CLI) for working with the Huggingface Inference Endpoints API ([API docs](https://huggingface.co/docs/inference-endpoints/api_reference))

# Getting started

The package is pip installable and can be installed from PyPI

```
pipx install hugie
```

⚠️  To get started, you must set your individual or organisation Huggingface token into an env var called `HUGGINGFACE_READ_TOKEN`.

# Usage 📺

tldr; watch the video:

[![asciicast](https://asciinema.org/a/BkNNlNE8jTLbBa5rI5hPpdbIW.svg)](https://asciinema.org/a/BkNNlNE8jTLbBa5rI5hPpdbIW)

# Commands ⌨️

```
hugie
>>>
Usage: hugie [OPTIONS] COMMAND [ARGS]...

Options:
  --help                          Show this message and exit.

Commands:
  Commands:
  config
  endpoint
  ui        Open the Hugging Face Endpoints UI in a browser
  version   Print hugie version
```

# Endpoint

```
hugie endpoint --help
>>>
Usage: hugie endpoint[OPTIONS] COMMAND[ARGS]...

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

## Create

To create an endpoint:

```
Usage: hugie endpoint create [OPTIONS] [DATA]

  Create an endpoint

  Args:     data (str): Path to JSON data to create the endpoint

Arguments:
  [DATA]  Path JSON data to create the endpoint

Options:
  --account-id TEXT      ID of the account (for private endpoints)
  --name TEXT            Name of the endpoint  [default: hf-endpoint]
  --type TEXT            Type of endpoint, one of ['public', 'protected',
                         'private']
  --accelerator TEXT     Accelerator to use. One of ['CPU','GPU']  [default:
                         cpu]
  --instance-type TEXT   [default: c6i]
  --instance-size TEXT   [default: small]
  --min-replica INTEGER  Minimum number of replicas  [default: 1]
  --max-replica INTEGER  Maximum number of replicas  [default: 1]
  --framework TEXT       Framework to use  [default: custom]
  --repository TEXT      Name of the hf model repository  [default: t5-small]
  --revision TEXT        Revision of the hf model repository  [default: main]
  --task TEXT            Task of the model  [default: text-generation]
  --image TEXT           Image to use from huggingface or tgi  [default:
                         huggingface]
  --vendor TEXT          Vendor to use. One of ['aws','gcp']  [default: aws]
  --region TEXT          Vendor specific region, e.g. 'us-east-1'  [default:
                         us-east-1]
  --json                 Prints the full output in JSON.
  --help                 Show this message and exit.
```

## List

To list all your endpoints:

```
hugie endpoint list

# Use --json option to view all content

hugie endpoint list --json
```

## Update

To update an endpoint, edit `examples/development.json`

```
hugie endpoint update development examples/development.json
```

## Logs

To see the logs:

```
hugie endpoint logs development
```

## Delete
To delete the endpoint

```
hugie endpoint delete development
```

this will ask you if you are sure you want to delete before moving forward. If
you want to force the deletion you can use `--force`

## JSON format

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

## For development

Read our CONTRIBUTING.md then

Create a virtual environment and install the package

```
poetry install
```

Run tests
```
pytest
```

To upload to PyPi run

``
poetry publish
```

you need the mantisnlp password to proceed. Ask Nick or Matt.
