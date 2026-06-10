from fastapi.testclient import TestClient
from main import app
client = TestClient(app)
def delete_note():
    response = client.delete("/notes/5")
    assert response.status_code == 404