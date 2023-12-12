from fastapi.testclient import TestClient


def test_health_check(client_mock: TestClient) -> None:
    """
    Tests whether the API is running and is reachable.
    """
    response = client_mock.get("/health_check")
    assert response.status_code == 200
    assert response.json() == {"msg": "healthy"}
