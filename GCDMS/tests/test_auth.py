import pytest


@pytest.mark.asyncio
async def test_signup_and_login(client):
    signup_data = {"username": "testuser", "email": "testuser@example.com", "password": "testpassword123"}

    # تست signup
    response = await client.post("/auth/signup", json=signup_data)
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "testuser@example.com"
    assert "password" not in data  # چون نباید پسورد در پاسخ باشه

    # تست login
    login_data = {"username": "testuser", "password": "testpassword123"}
    response = await client.post("/auth/login", json=login_data)
    assert response.status_code == 200
    token_data = response.json()
    assert "access_token" in token_data
    assert token_data["token_type"] == "bearer"
