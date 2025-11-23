from fastapi.testclient import TestClient
from api_app.main import app

client = TestClient(app)

def test_login():
    response = client.post("/login", json={"username": "khadija", "password": "Elabbioui99"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_predict_token():
    response = client.post("/predict", json={"text":"i'm happy"})
    assert response.status_code == 200
    assert "Token valid" 

