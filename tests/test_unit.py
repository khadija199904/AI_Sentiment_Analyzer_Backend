import pytest
from api_app.auth import create_token, verify_token
from api_app.schema import User


def test_create_token_success():
    user = User(username="khadija", password="Elabbioui99")
    token = create_token(user)
    assert token is not None
    assert isinstance(token, str)


def test_verify_token_():
    user = User(username="khadija", password="Elabbioui99")
    token = create_token(user)
    decoded = verify_token(token)
    assert isinstance(decoded, dict)