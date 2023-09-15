# Run with: pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_brand():
    """Test that a brand is created successfully"""
    data = {
        "name": "test_string",
        "cost_per_cup": 0
    }

    # Send a POST request to your FastAPI app
    response = client.post("/coffee/brand", json=data)

    assert response.status_code == 200

    assert response.json() == {
        "name": "test_string",
        "cost_per_cup": 0,
        "id": 1
    }

def test_get_brands():
    """Test that all brands are returned"""
    response = client.get("/coffee/brand")

    assert response.status_code == 200

    assert response.json() == [
        {
            "name": "test_string",
            "cost_per_cup": 0,
            "id": 1
        }
    ]

def test_get_brand():
    """Test that a brand is returned"""
    response = client.get("/coffee/brand/1")

    assert response.status_code == 200

    assert response.json() == {
        "name": "test_string",
        "cost_per_cup": 0,
        "id": 1
    }