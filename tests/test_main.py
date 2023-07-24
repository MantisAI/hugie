from hugie.__main__ import app
from typer.testing import CliRunner

runner = CliRunner()


def test_ui_command(monkeypatch):
    def mock_open(url):
        return "Opening https://ui.endpoints.huggingface.co/ in your browser..."

    # Use monkeypatch to replace the ui function with the mock function
    monkeypatch.setattr("webbrowser.open", mock_open)

    runner = CliRunner()
    result = runner.invoke(app, ["ui"])

    assert result.exit_code == 0
    assert (
        "Opening https://ui.endpoints.huggingface.co/ in your browser..."
        in result.output
    )
