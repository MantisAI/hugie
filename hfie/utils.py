import json

import typer
import wasabi


def format_table(headers: list, *args):
    """
    Formats a wasabi table ready for printing

    Args:
        column_names (list): List of column names
        *args (list): List of lists containing the data for each column

    """

    data = list(map(tuple, zip(*args)))

    table = wasabi.table(data, header=headers, divider=True)

    return table


def load_json(path: str):
    """
    Loads a JSON file
    """

    try:
        with open(path) as f:
            data = json.load(f)

        return data
    except FileNotFoundError:
        typer.secho(f"File {path} not found", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    except json.decoder.JSONDecodeError:
        typer.secho(f"File {path} is not a valid JSON", fg=typer.colors.RED)
        raise typer.Exit(code=1)
