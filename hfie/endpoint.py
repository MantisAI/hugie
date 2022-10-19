import json

import requests
import typer

from hfie.settings import Settings
from hfie.utils import format_table

settings = Settings()

app = typer.Typer()

headers = {
    "Authorization": f"Bearer {settings.token}",
    "Content-Type": "application/json",
}


@app.command()
def list(json: bool = typer.Option(False, help="Prints the full output in JSON.")):
    """
    List all the deployed endpoints
    """
    r = requests.get(f"{settings.endpoint_url}", headers=headers)

    if json:
        typer.echo(r.json())

    else:
        data = r.json()

        names = []
        types = []
        states = []
        models = []
        revs = []

        for item in data["items"]:
            names.append(item["name"])
            types.append(item["type"])
            states.append(item["status"]["state"])
            models.append(item["model"]["repository"])
            revs.append(item["model"]["revision"])

        table = format_table(
            ["Name", "Type", "State", "Model", "Revision"],
            names,
            types,
            states,
            models,
            revs,
        )

        typer.secho(table)


@app.command()
def create(
    data: str = typer.Argument(..., help="Path JSON data to create the endpoint")
):
    """
    Create an endpoint
    """
    with open(data) as f:
        data = json.load(f)
    r = requests.post(f"{settings.endpoint_url}", headers=headers, json=data)
    typer.echo(r.json())


@app.command()
def update(
    name: str = typer.Argument(..., help="Endpoint name"),
    data: str = typer.Argument(..., help="Path to JSON data to update the endpoint"),
):
    """
    Update an endpoint
    """
    r = requests.put(f"{settings.endpoint_url}/{name}", headers=headers, json=data)
    typer.echo(r.json())


@app.command()
def delete(name: str = typer.Argument(..., help="Endpoint name")):
    """
    Delete an endpoint
    """
    r = requests.delete(f"{settings.endpoint_url}/{name}", headers=headers)
    typer.echo(r.json())


@app.command()
def info(
    name: str = typer.Argument(..., help="Endpoint name"),
    json: bool = typer.Option(False, help="Prints the full output in JSON."),
):
    """
    Get info about an endpoint
    """
    r = requests.get(f"{settings.endpoint_url}/{name}", headers=headers)

    if json:
        typer.echo(r.json())

    else:
        data = r.json()
        print(data)

        names = []
        types = []
        states = []
        models = []
        revs = []

        names.append(data["name"])
        types.append(data["type"])
        states.append(data["status"]["state"])
        models.append(data["model"]["repository"])
        revs.append(data["model"]["revision"])

        table = format_table(
            ["Name", "Type", "State", "Model", "Revision"],
            names,
            types,
            states,
            models,
            revs,
        )

        typer.secho(table)


@app.command()
def logs(name: str = typer.Argument(..., help="Endpoint name")):
    """
    Get logs about an endpoint
    """
    r = requests.get(f"{settings.endpoint_url}/{name}/logs", headers=headers)
    typer.echo(r.content)
