from fastapi.testclient import TestClient
from main import app
client = TestClient(app)
def test_notes_required_login():
    response = client.get("/notes")
    assert response.status_code == 401