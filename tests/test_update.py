from fastapi.testclient import TestClient
from main import app
client = app
def update_note():
    response = client.put("/notes/1",json={"title":"updated title","content":"updated content"})
    assert response.status_code == 200