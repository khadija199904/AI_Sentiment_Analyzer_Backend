from fastapi.testclient import TestClient
from api_app.main import app

client = TestClient(app)

def test_login():
    response = client.post("/login", json={"username": "test", "password": "KELA"})
    assert response.status_code == 200
    # assert "access_token" in response.json()
