"""
This file contains class based tests for the health check endpoint of the FastAPI application.
"""
from datetime import datetime

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def test_client():
    """Fixture to provide a test client for the FastAPI application."""
    return TestClient(app)


class TestHealthCheck:
    """Class based tests for the health check endpoint."""

    def test_health_check(self, test_client):
        """Test the health check endpoint."""
        response = test_client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert "status" in data
        assert data["status"] == "healthy"
        assert "timestamp" in data
        # Check if timestamp is a valid ISO format
        datetime.fromisoformat(data["timestamp"])
        assert isinstance(data["timestamp"], str)

    def test_health_check_response_format(self, test_client):
        """Test the health check response format."""
        response = test_client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert "status" in data
        assert "timestamp" in data
        assert isinstance(data["status"], str)
        assert isinstance(data["timestamp"], str)

    def test_health_check_timestamp(self, test_client):
        """Test the health check timestamp format."""
        response = test_client.get("/health")
        assert response.status_code == 200
        data = response.json()
        # Check if timestamp is a valid ISO format
        try:
            datetime.fromisoformat(data["timestamp"])
        except ValueError:
            pytest.fail("Timestamp is not in valid ISO format")
        assert isinstance(data["timestamp"], str)

    def test_health_check_status(self, test_client):
        """Test the health check status."""
        response = test_client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert "status" in data
        assert data["status"] == "healthy"
        assert isinstance(data["status"], str)

    def test_health_check_status_type(self, test_client):
        """Test the health check status type."""
        response = test_client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert "status" in data
        assert isinstance(data["status"], str)
        assert data["status"] == "healthy"

    def test_health_check_timestamp_type(self, test_client):
        """Test the health check timestamp type."""
        response = test_client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert "timestamp" in data
        assert isinstance(data["timestamp"], str)
        # Check if timestamp is a valid ISO format
        try:
            datetime.fromisoformat(data["timestamp"])
        except ValueError:
            pytest.fail("Timestamp is not in valid ISO format")
        assert isinstance(data["timestamp"], str)

    def test_health_check_no_content(self, test_client):
        """Test the health check endpoint with no content."""
        response = test_client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data == {"status": "healthy", "timestamp": data["timestamp"]}
        assert isinstance(data["timestamp"], str)
        # Check if timestamp is a valid ISO format
        try:
            datetime.fromisoformat(data["timestamp"])
        except ValueError:
            pytest.fail("Timestamp is not in valid ISO format")
