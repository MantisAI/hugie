import importlib.metadata

import typer

from hugie.config import app as config_app
from hugie.endpoint import app as endpoint_app

app = typer.Typer()


@app.command()
def version():
    """Show version."""
    typer.echo(importlib.metadata.version("hugie"))
    typer.Exit(0)


app.add_typer(endpoint_app, name="endpoint")
app.add_typer(config_app, name="config")

if __name__ == "__main__":
    app()
