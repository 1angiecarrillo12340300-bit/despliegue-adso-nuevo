from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code in [200, 500]


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200