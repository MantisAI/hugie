# Endpoint

This page details the usage of the endpoint command

```
 Usage: hugie endpoint [OPTIONS] COMMAND [ARGS]...

╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                  │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ create         Create an endpoint                                            │
│ delete         Delete an endpoint                                            │
│ info           Get info about an endpoint                                    │
│ list           List all the deployed endpoints                               │
│ logs           Get logs about an endpoint                                    │
│ test           Test an endpoint                                              │
│ update         Update an endpoint                                            │
╰──────────────────────────────────────────────────────────────────────────────╯
```


## Create

To create an endpoint:

```
hugie endpoint create examples/development.json
```

Command reference:
```
 Usage: hugie endpoint create [OPTIONS] DATA

 Create an endpoint
 Args:     data (str): Path to JSON data to create the endpoint

╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    data      TEXT  Path JSON data to create the endpoint [default: None]   │
│                      [required]                                              │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --json          Prints the full output in JSON.                              │
│ --help          Show this message and exit.                                  │
╰──────────────────────────────────────────────────────────────────────────────╯

```

## list/ls

List all your endpoints.

Command reference:

```
 Usage: hugie endpoint list [OPTIONS]

 List all the deployed endpoints

╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --json          Prints the full output in JSON.                              │
│ --help          Show this message and exit.                                  │
╰──────────────────────────────────────────────────────────────────────────────╯
```


## update

To update an endpoint, edit the config file (e.g. `examples/development.json`), and run:

```
hugie endpoint update examples/development.json
```

Command reference:
```
 Usage: hugie endpoint update [OPTIONS] NAME DATA

 Update an endpoint

╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    name      TEXT  Endpoint name [default: None] [required]                │
│ *    data      TEXT  Path to JSON data to update the endpoint                │
│                      [default: None]                                         │
│                      [required]                                              │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --json          Prints the full output in JSON.                              │
│ --help          Show this message and exit.                                  │
╰──────────────────────────────────────────────────────────────────────────────╯

```

## Logs

See the endpoint logs.

Command reference:
```
 Usage: hugie endpoint logs [OPTIONS] NAME

 Get logs about an endpoint

╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    name      TEXT  Endpoint name [default: None] [required]                │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                  │
╰──────────────────────────────────────────────────────────────────────────────╯

```


## Delete

To delete the endpoint

```
hugie endpoint delete development
```

this will ask you if you are sure you want to delete before moving forward. If
you want to force the deletion you can use `--force`

Command reference:
```
 Usage: hugie endpoint delete [OPTIONS] NAME

 Delete an endpoint

╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    name      TEXT  Endpoint name [default: None] [required]                │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --force  -f        Force deletion without asking user confirmation           │
│ --help             Show this message and exit.                               │
╰──────────────────────────────────────────────────────────────────────────────╯
```

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
