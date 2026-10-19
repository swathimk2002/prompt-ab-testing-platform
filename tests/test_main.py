"""Test the main FastAPI application."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    """Check that the health endpoint returns the expected response."""
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}