import srsly
import typer

from hugie.models import EndpointConfig

app = typer.Typer()


@app.command()
def modify(
    path: str,
    accountId: str = typer.Option(
        None, help="ID of the account (for private endpoints)"
    ),
    name: str = typer.Option(None, help="Name of the endpoint"),
    type: str = typer.Option(
        None, help="Type of endpoint, one of ['public', 'protected', 'private']"
    ),
    accelerator: str = typer.Option(
        "None", help="Accelerator to use. One of ['CPU','GPU']"
    ),
    instanceType: str = typer.Option(None),
    instanceSize: str = typer.Option(None),
    minReplica: int = typer.Option(None, help="Minimum number of replicas"),
    maxReplica: int = typer.Option(None, help="Maximum number of replicas"),
    framework: str = typer.Option("huggingface", help="Framework to use"),
    image: str = typer.Option(
        None,
        help="Image to use when deploying model endppint. Must be string representing a valid JSON, e.g. '{'huggingface': {}}'",
    ),
    repository: str = typer.Option(None, help="Name of the hf model repository"),
    revision: str = typer.Option(None, help="Revision of the hf model repository"),
    task: str = typer.Option(None, help="Task of the model"),
    vendor: str = typer.Option(None, help="Vendor to use. One of ['aws','gcp']"),
    region: str = typer.Option(None, help="Vendor specific region, e.g. 'us-east-1'"),
    overwrite: bool = typer.Option(
        False, "--overwrite", "-o", help="Overwrite inpiut file with updated config"
    ),
):
    """
    Modify an existing endpoint config file
    """

    config = EndpointConfig.from_json(path)

    # Standard configs

    if name:
        config.name = name

    if type:
        config.type = type

    if accountId:
        config.accountId = accountId

    # Model config

    if repository:
        config.model.repository = repository

    if revision:
        config.model.revision = revision

    if framework:
        config.model.framework = framework

    if task:
        config.model.task = task

    if image:
        config.model.image = image

    # Compute config

    if instanceSize:
        config.compute.instanceSize = instanceSize

    if accelerator:
        config.compute.accelerator = accelerator

    if instanceType:
        config.compute.instanceType = instanceType

    # Scaling config

    if minReplica:
        config.scaling.minReplica = minReplica

    if maxReplica:
        config.scaling.maxReplica = maxReplica

    # Provider config

    if vendor:
        config.provider.vendor = vendor

    if region:
        config.provider.region = region

    if overwrite:
        try:
            srsly.write_json(path, config.dict())
            typer.secho(f"Updated config at {path}", fg=typer.colors.GREEN)
        except Exception:
            typer.secho(f"Failed to update config at {path}", fg=typer.colors.RED)

    else:
        typer.secho(srsly.json_dumps(config.dict()), fg=typer.colors.YELLOW)


if __name__ == "__main__":
    app()
