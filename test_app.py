import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    response = client.get('/hello/World')
    assert response.status_code == 200
    assert response.data.decode() == "Hello World"
