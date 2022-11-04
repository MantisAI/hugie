import typer

from hugie.endpoint import app as endpoint_app

app = typer.Typer()

app.add_typer(endpoint_app, name="endpoint")

if __name__ == "__main__":
    app()
