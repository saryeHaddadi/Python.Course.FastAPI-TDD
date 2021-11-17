from starlette.testclient import TestClient


def test_get_ping_200(test_app: TestClient):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"environment": "dev", "ping": "pong!", "testing": True}


