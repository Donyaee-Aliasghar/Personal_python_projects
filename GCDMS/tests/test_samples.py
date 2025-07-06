def create_patient_for_sample(client):
    response = client.post("/patients/", json={"name": "Test Patient", "birthdate": "1990-01-01", "gender": "other"})
    assert response.status_code == 200
    return response.json()["id"]


def test_create_genetic_sample(client):
    patient_id = create_patient_for_sample(client)
    response = client.post(
        "/genetic-samples/",
        json={
            "patient_id": patient_id,
            "sample_date": "2024-01-01",
            "sample_type": "Blood",
            "description": "Routine test",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["patient_id"] == patient_id
    assert data["sample_type"] == "Blood"
    return data


def test_get_genetic_sample_by_id(client):
    sample = test_create_genetic_sample(client)
    sample_id = sample["id"]

    response = client.get(f"/genetic-samples/{sample_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == sample_id
    assert data["sample_type"] == "Blood"


def test_get_all_genetic_samples(client):
    sample = test_create_genetic_sample(client)

    response = client.get("/genetic-samples/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    sample_ids = [s["id"] for s in data]
    assert sample["id"] in sample_ids
