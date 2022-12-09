from fastapi.testclient import TestClient
from main import app
import json

client = TestClient(app)


def test_scramble_input():
	data = {"key": "abc123"}
	response = client.post("/jumble-api/", json=json.dumps(data))
	assert response.status_code == 200
	assert response.content != data["key"]
	assert len(response.content) == len(data["key"])


def test_empty_input():
	data = {"key": ""}
	response = client.post("/jumble-api/", json=json.dumps(data))
	assert response.status_code == 200
	assert len(response.content) == len(data["key"])


def test_audit_api_with_scramble_words():
	data = {"key": "abc123"}
	client.post("/jumble-api", json=json.dumps(data))
	response = client.get("/audit-api")
	assert len(response.content) == 1


def test_audit_api_without_scramble_words():
	response = client.get("/audit-api")
	assert len(response.content) == 0
