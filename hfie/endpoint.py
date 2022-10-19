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
        return typer.echo(r.json())

    else:
        data = r.json()

        names = []
        states = []
        models = []
        revs = []
        url = []

        for item in data["items"]:
            names.append(item["name"])
            states.append(item["status"]["state"])
            models.append(item["model"]["repository"])
            revs.append(item["model"]["revision"])
            url.append(item["status"]["url"])

        table = format_table(
            ["Name", "State", "Model", "Revision", "Url"],
            names,
            states,
            models,
            revs,
            url,
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
    with open(data) as f:
        data = json.load(f)
    r = requests.put(f"{settings.endpoint_url}/{name}", headers=headers, json=data)
    typer.echo(r.json())


@app.command()
def delete(name: str = typer.Argument(..., help="Endpoint name")):
    """
    Delete an endpoint
    """
    r = requests.delete(f"{settings.endpoint_url}/{name}", headers=headers)
    typer.echo(r.json())


def get_info(name: str):
    r = requests.get(f"{settings.endpoint_url}/{name}", headers=headers)

    return r.json()


@app.command()
def info(
    name: str = typer.Argument(..., help="Endpoint name"),
    json: bool = typer.Option(False, help="Prints the full output in JSON."),
):
    """
    Get info about an endpoint
    """
    info = get_info(name)

    if json:
        typer.echo(info)

    else:
        names = []
        states = []
        models = []
        revs = []
        url = []

        names.append(info["name"])
        states.append(info["status"]["state"])
        models.append(info["model"]["repository"])
        revs.append(info["model"]["revision"])
        url.append(info["status"]["url"])

        table = format_table(
            ["Name", "State", "Model", "Revision", "Url"],
            names,
            states,
            models,
            revs,
            url,
        )

        typer.secho(table)


@app.command()
def logs(name: str = typer.Argument(..., help="Endpoint name")):
    """
    Get logs about an endpoint
    """
    r = requests.get(f"{settings.endpoint_url}/{name}/logs", headers=headers)
    typer.echo(r.content)


@app.command()
def test(
    name: str = typer.Argument(..., help="Endpoint name"),
    inputs: str = typer.Argument(..., help="Input to send the model."),
):
    """
    Test an endpoint
    """

    info = get_info(name)
    url = info["status"]["url"]
    data = {"inputs": inputs, "parameters": {"top_k": 10}}
    r = requests.post(url, headers=headers, json=data)
    typer.echo(r.json())
