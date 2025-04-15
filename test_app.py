import pytest
from app import app
import json

@pytest.fixture
def client():
    # Utworzenie testowego klienta Flask
    app.config["TESTING"] = True
    client = app.test_client()
    yield client

def test_home(client):
    """ Testuje główny endpoint """
    response = client.get("/")
    assert response.status_code == 200
    assert b"student" in response.data

def test_predict(client):
    """ Testuje endpoint /predict """
    response = client.post("/predict", json={"input": 2.5}, content_type="application/json")
    assert response.status_code == 200
    data = response.get_json()
    assert "prediction" in data
    assert isinstance(data["prediction"], list)


def test_last_prediction(client):
    """ Testuje endpoint /last """
    response = client.get("/last")
    assert response.status_code == 500  # W przypadku wyłączenia Redis
    assert b"Redis not enabled" in response.data

def test_api_key(client):
    """ Testuje endpoint /api_key """
    response = client.get("/api_key")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "api_key" in data
    assert data["api_key"] == "dummy_key_for_testing"  # Używa domyślnego klucza API
