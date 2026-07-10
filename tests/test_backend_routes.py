from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_home_page_renders():
    response = client.get("/")
    assert response.status_code == 200
    assert "Multi-Agent SOC" in response.text


def test_analyze_page_renders():
    response = client.post("/", data={"security_log": "Suspicious login"})
    assert response.status_code == 200
    assert "Multi-Agent SOC" in response.text
