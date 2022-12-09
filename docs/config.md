# Config

This page details the usage of the config command

```
 Usage: hugie config [OPTIONS] COMMAND [ARGS]...

╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                  │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ modify       Modify an existing endpoint config file                         │
╰──────────────────────────────────────────────────────────────────────────────╯
```

## Modify

Modify an existing config file.

Command referene:
```
 Usage: hugie config modify [OPTIONS] PATH

 Modify an existing endpoint config file

╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    path      TEXT  [default: None] [required]                              │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --accountid             TEXT     ID of the account (for private endpoints)   │
│                                  [default: None]                             │
│ --name                  TEXT     Name of the endpoint [default: None]        │
│ --type                  TEXT     Type of endpoint, one of ['public',         │
│                                  'protected', 'private']                     │
│                                  [default: None]                             │
│ --accelerator           TEXT     Accelerator to use. One of ['CPU','GPU']    │
│                                  [default: None]                             │
│ --instancetype          TEXT     [default: None]                             │
│ --instancesize          TEXT     [default: None]                             │
│ --minreplica            INTEGER  Minimum number of replicas [default: None]  │
│ --maxreplica            INTEGER  Maximum number of replicas [default: None]  │
│ --framework             TEXT     Framework to use [default: huggingface]     │
│ --image                 TEXT     Image to use when deploying model endppint. │
│                                  Must be string representing a valid JSON,   │
│                                  e.g. '{'huggingface': {}}'                  │
│                                  [default: None]                             │
│ --repository            TEXT     Name of the hf model repository             │
│                                  [default: None]                             │
│ --revision              TEXT     Revision of the hf model repository         │
│                                  [default: None]                             │
│ --task                  TEXT     Task of the model [default: None]           │
│ --vendor                TEXT     Vendor to use. One of ['aws','gcp']         │
│                                  [default: None]                             │
│ --region                TEXT     Vendor specific region, e.g. 'us-east-1'    │
│                                  [default: None]                             │
│ --overwrite     -o               Overwrite inpiut file with updated config   │
│ --help                           Show this message and exit.                 │
╰──────────────────────────────────────────────────────────────────────────────╯
```
