# Endpoint

This page details the usage of the endpoint command

```
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

## Create

To create an endpoint:

```
hfie endpoint create examples/development.json
```

## List

To list all your endpoints:

```
hfie endpoint list

# Use --json option to view all content

hfie endpoint list --json
```

## Update

To update an endpoint, edit `examples/development.json`

```
hfie endpoint update development examples/development.json
```

## Logs

To see the logs:

```
hfie endpoint logs development
```

## Delete

To delete the endpoint

```
hfie endpoint delete development
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
