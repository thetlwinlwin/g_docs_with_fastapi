from fastapi import Response
from fastapi.testclient import TestClient
from fetch_note.main import app


client :TestClient = TestClient(app=app)

def test_main():
    res:Response = client.get('/')
    assert res.status_code == 200
