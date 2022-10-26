import requests
import typer

from hfie.utils import format_table, load_json


def call(url, headers: dict, data: dict, call: str):

    calls = {
        "get": requests.get,
        "post": requests.post,
        "put": requests.put,
        "delete": requests.delete,
    }
    try:
        r = calls[call](url, headers=headers, json=data)
        r.raise_for_status()

        return r
    except KeyError:
        typer.secho(
            f"Invalid call type. Must be one of {list(calls.keys())}",
            fg=typer.colors.RED,
        )
    except requests.exceptions.HTTPError as e:
        if r.json().get("error"):
            typer.secho(
                f"Error creating endpoint: {r.json()['error']}", fg=typer.colors.RED
            )
        else:
            typer.secho("Error creating endpoint", fg=typer.colors.RED)
        raise SystemExit(e)
    except requests.exceptions.RequestException as e:
        typer.secho("Error making API call", fg=typer.colors.RED)
        raise SystemExit(e)
