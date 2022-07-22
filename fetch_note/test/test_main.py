from fastapi.testclient import TestClient
from requests import Response
from fetch_note.main import app


client :TestClient = TestClient(app=app)

def test_main():
    res:Response = client.get('/get_title')
    assert res.status_code == 200
    assert res.json() ==  {"Title": "Love Notes"}
