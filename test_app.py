from app import app


def test_system_health_route():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"EC2 System Health" in response.data
