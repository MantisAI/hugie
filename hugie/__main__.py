import importlib.metadata
import webbrowser

import typer

from hugie.config import app as config_app
from hugie.endpoint import app as endpoint_app

app = typer.Typer()


@app.command()
def version():
    """Print hugie version"""
    typer.echo(importlib.metadata.version("hugie"))
    typer.Exit(0)


@app.command("ui")
def open_ui():
    """
    Open the Hugging Face Endpoints UI in a browser
    """
    url = "https://ui.endpoints.huggingface.co/"
    typed_url = typer.style(url, fg=typer.colors.BLUE, bold=True)
    typer.echo(f"Opening {typed_url} in your browser...")
    webbrowser.open(url)
    typer.Exit(0)


app.add_typer(endpoint_app, name="endpoint")
app.add_typer(config_app, name="config")

if __name__ == "__main__":
    app()
