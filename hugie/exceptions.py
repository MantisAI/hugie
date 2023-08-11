import requests
import typer


class TokenNotSetError(Exception):
    def __str__(self):
        return "You need to define a token using the environment variable HUGGINGFACE_READ_TOKEN"


def handle_requests_error(exception, data):
    """
    Generic HTTP error handling function. Takes an HTTPError or RequestException
    instance as input and handles the error by printing an appropriate message
    and exiting the program.

    Args:
        exception (requests.exceptions.HTTPError): HTTPError or RequestException instance
        data (dict): Hugging Face Inference Endpoint configuration
    """
    # Print a general API error message
    typer.secho("An error occurred with the API request.", fg=typer.colors.RED)

    # If the exception is an HTTPError, provide more specific error messages
    # based on the status code

    if isinstance(exception, requests.exceptions.HTTPError):
        status_code = exception.response.status_code

        if status_code == 400:
            typer.secho(f"Malformed data in request: {data}", fg=typer.colors.YELLOW)
        elif status_code == 401:
            typer.secho("Invalid API token.", fg=typer.colors.YELLOW)
        elif status_code == 404:
            typer.secho("Endpoint with this name not found", fg=typer.colors.YELLOW)
        elif status_code == 409:
            typer.secho(
                "Conflict: An endpoint with this name already exists.",
                fg=typer.colors.YELLOW,
            )
        elif status_code == 500:
            typer.secho("Internal Server Error", fg=typer.colors.YELLOW)
        elif status_code == 501:
            typer.secho("Not Implemented", fg=typer.colors.YELLOW)
        elif status_code == 502:
            typer.secho("Bad Gateway", fg=typer.colors.YELLOW)
        elif status_code == 503:
            typer.secho("Service Unavailable", fg=typer.colors.YELLOW)
        elif status_code == 504:
            typer.secho("Gateway Timeout", fg=typer.colors.YELLOW)
        elif status_code == 509:
            typer.secho("Bandwidth Limit Exceeded", fg=typer.colors.YELLOW)
        elif status_code == 511:
            typer.secho("Network Authentication Required", fg=typer.colors.YELLOW)
        else:
            typer.secho("An HTTP error occurred.", fg=typer.colors.RED)

    elif isinstance(exception, requests.exceptions.ConnectionError):
        typer.secho("A network problem occurred.", fg=typer.colors.RED)
    elif isinstance(exception, requests.exceptions.Timeout):
        typer.secho("The request timed out.", fg=typer.colors.RED)
    elif isinstance(exception, requests.exceptions.TooManyRedirects):
        typer.secho(
            "The request exceeded the configured number of maximum redirections.",
            fg=typer.colors.RED,
        )
    elif isinstance(exception, requests.exceptions.RequestException):
        typer.secho(
            "An error occurred while handling the request.", fg=typer.colors.RED
        )

    # Exit the program with an error code

    raise SystemExit(exception)
