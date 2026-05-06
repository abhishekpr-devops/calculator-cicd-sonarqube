from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "Calculator API is running"


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_add():
    client = app.test_client()
    response = client.get("/calc?op=add&a=10&b=5")
    assert response.status_code == 200
    assert response.json["result"] == 15


def test_divide_by_zero():
    client = app.test_client()
    response = client.get("/calc?op=div&a=10&b=0")
    assert response.status_code == 400
    assert response.json["error"] == "Cannot divide by zero"
