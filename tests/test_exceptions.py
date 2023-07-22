import pytest
from hugie.exceptions import TokenNotSetError, handle_requests_error
from requests.exceptions import (
    ConnectionError,
    HTTPError,
    RequestException,
    Timeout,
    TooManyRedirects,
)


def test_TokenNotSetError():
    exception = TokenNotSetError()
    assert (
        str(exception)
        == "You need to define a token using the environment variable HUGGINGFACE_READ_TOKEN"
    )


def test_handle_requests_error_HTTPError_400(mocker):
    mock_response = mocker.Mock(status_code=400)
    exception = HTTPError(response=mock_response)

    with pytest.raises(SystemExit) as e:
        handle_requests_error(exception, {"data": "test"})

    assert str(e.value) == str(exception)


def test_handle_requests_error_HTTPError_401(mocker):
    mock_response = mocker.Mock(status_code=401)
    exception = HTTPError(response=mock_response)

    with pytest.raises(SystemExit) as e:
        handle_requests_error(exception, {"data": "test"})

    assert str(e.value) == str(exception)


def test_handle_requests_error_HTTPError_409(mocker):
    mock_response = mocker.Mock(status_code=409)
    exception = HTTPError(response=mock_response)

    with pytest.raises(SystemExit) as e:
        handle_requests_error(exception, {"data": "test"})

    assert str(e.value) == str(exception)


def test_handle_requests_error_HTTPError_other(mocker):
    mock_response = mocker.Mock(status_code=500)
    exception = HTTPError(response=mock_response)

    with pytest.raises(SystemExit) as e:
        handle_requests_error(exception, {"data": "test"})

    assert str(e.value) == str(exception)


def test_handle_requests_error_ConnectionError(monkeypatch):
    exception = ConnectionError()

    with pytest.raises(SystemExit) as e:
        handle_requests_error(exception, {})

    assert str(e.value) == str(exception)


def test_handle_requests_error_Timeout(monkeypatch):
    exception = Timeout()

    with pytest.raises(SystemExit) as e:
        handle_requests_error(exception, {})

    assert str(e.value) == str(exception)


def test_handle_requests_error_TooManyRedirects(monkeypatch):
    exception = TooManyRedirects()

    with pytest.raises(SystemExit) as e:
        handle_requests_error(exception, {})

    assert str(e.value) == str(exception)


def test_handle_requests_error_RequestException(monkeypatch):
    exception = RequestException()

    with pytest.raises(SystemExit) as e:
        handle_requests_error(exception, {})

    assert str(e.value) == str(exception)
