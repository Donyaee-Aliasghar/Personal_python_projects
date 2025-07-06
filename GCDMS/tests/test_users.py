def test_create_user(client):
    response = client.post("/users/", json={"username": "alice", "email": "alice@example.com", "password": "secret123"})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "alice"
    assert data["email"] == "alice@example.com"
    return data


def test_get_user_by_id(client):
    response = client.post(
        "/users/", json={"username": "charlie", "email": "charlie@example.com", "password": "secret123"}
    )
    assert response.status_code == 200
    user_data = response.json()
    user_id = user_data["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()

    assert data["id"] == user_id
    assert data["username"] == "charlie"
    assert data["email"] == "charlie@example.com"
    return data


def test_get_users(client):
    user = test_create_user(client)

    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    usernames = [u["username"] for u in data]
    assert user["username"] in usernames
