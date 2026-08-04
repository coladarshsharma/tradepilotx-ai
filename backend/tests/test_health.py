from fastapi.testclient import TestClient

from app.main import app


def test_health_endpoint() -> None:
    response = TestClient(app).get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_openapi_documentation_is_enabled() -> None:
    response = TestClient(app).get("/api/v1/openapi.json")
    assert response.status_code == 200
    assert "authentication" in [tag["name"] for tag in response.json()["tags"]]
