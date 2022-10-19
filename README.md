# HF Endpoints

A CLI interface for working with the HuggingFace Inference API.

See API docs: https://huggingface.co/docs/inference-endpoints/api_reference

# Getting started

The package is pip installable and can be installed directly from github with:

```
pip install git+https://github.com/mantisnlp/hfie.git
```

# Usage

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
  update  Update an endpoint

```



# For development

Create a virtual environment and install the package

```
make virtualenv
```

