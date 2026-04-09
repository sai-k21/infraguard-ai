from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] == True
    assert data["message"] == "InfraGuard AI is running"

def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] == True
    assert data["data"]["service"] == "infraguard-ai"

def test_analyze_missing_body():
    response = client.post("/analyze")
    assert response.status_code == 422

def test_analyze_with_logs():
    response = client.post("/analyze", json={
        "logs": "ERROR Database connection timeout",
        "service_name": "test-service",
        "environment": "test"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["success"] == True
    assert data["data"]["service_name"] == "test-service"
    assert "severity" in data["data"]
    assert "probable_cause" in data["data"]