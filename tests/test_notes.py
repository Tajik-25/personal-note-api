from fastapi.testclient import TestClient
from main import app
client = TestClient(app)
def create_notes():
    response = client.post("/notes",json={"title":"pytest","content":"learning pytest"})
    assert response.status_code == 401