# tests/test_app.py

from .app import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_hello(client):
    response = client.get('/')
    assert b'Hello, Azure DevOps!' in response.data
