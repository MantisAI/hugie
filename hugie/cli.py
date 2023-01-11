import typer

from hugie.endpoint import app as endpoint_app
from hugie.config import app as config_app

app = typer.Typer()

app.add_typer(endpoint_app, name="endpoint")
app.add_typer(config_app, name="config")

if __name__ == "__main__":
    app()
