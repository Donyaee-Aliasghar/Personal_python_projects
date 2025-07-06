def test_create_patient(client):
    response = client.post("/patients/", json={"name": "John Doe", "birthdate": "2001-12-24", "gender": "male"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["birthdate"] == "2001-12-24"
    assert data["gender"] == "male"
    return data


def test_get_patient_by_id(client):
    response = client.post("/patients/", json={"name": "John Doe", "birthdate": "2001-12-24", "gender": "male"})
    assert response.status_code == 200
    user_data = response.json()
    user_id = user_data["id"]

    response = client.get(f"/patients/{user_id}")
    assert response.status_code == 200
    data = response.json()

    assert data["id"] == user_id
    assert data["name"] == "John Doe"
    assert data["birthdate"] == "2001-12-24"
    assert data["gender"] == "male"


def test_get_patients(client):
    response = client.get("/patients/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
