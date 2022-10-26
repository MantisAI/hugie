import json

import typer
import wasabi


def get_column_widths(columns):
    """Get the width of each column in a list of lists."""
    widths = []

    for column in columns:
        widths.append(max([len(str(i)) for i in column]))

    return widths


def format_table(headers: list, *args):
    """
    Formats a wasabi table ready for printing

    Args:
        column_names (list): List of column names
        *args (list): List of lists containing the data for each column

    """

    data = list(map(tuple, zip(*args)))
    widths = get_column_widths(args)

    table = wasabi.table(data, header=headers, divider=True, widths=widths)

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
