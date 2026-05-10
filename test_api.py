import requests
from pygments.lexers import data

headers = {"x-api-key": "free_user_34FbvlKNAwcnyunhMtw1UdCPXxt"}

def test_get_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/2")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 2
    assert data["name"] == "Ervin Howell"
    assert "email" in data
    print("Get user passed ✓")

def test_user_not_found():
    response = requests.get("https://jsonplaceholder.typicode.com/users/999")
    assert response.status_code == 404
    print("Status Code is 404")

def test_create_user():
    response = requests.post("https://jsonplaceholder.typicode.com/users",headers=headers,
                             json={"name": "Nimesha", "job": "QA Engineer"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Nimesha"
    assert data["job"] == "QA Engineer"
    assert "id" in data
    print("User created 201 ✓")

def test_get_all_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200
    data = response.json()
    assert len(data)== 10
    assert data[0] ["id"]== 1
    print("All users returned ✓")
