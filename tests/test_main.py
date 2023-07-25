from unittest.mock import Mock

from hugie.__main__ import app
from typer.testing import CliRunner

runner = CliRunner()


def test_ui_command(monkeypatch):
    mock_open = Mock(
        return_value="Opening https://ui.endpoints.huggingface.co/ in your browser..."
    )

    # Use monkeypatch to replace the ui function with the mock function
    monkeypatch.setattr("webbrowser.open", mock_open)

    runner = CliRunner()
    result = runner.invoke(app, ["ui"])

    assert result.exit_code == 0
    assert (
        "Opening https://ui.endpoints.huggingface.co/ in your browser..."
        in result.output
    )

    # Check that the mock was called
    mock_open.assert_called()
