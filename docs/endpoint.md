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
