from datetime import date


def create_patient(client):
    response = client.post("/patients/", json={"name": "Test Patient", "birthdate": "1990-01-01", "gender": "male"})
    assert response.status_code == 200
    return response.json()["id"]


def create_sample(client, patient_id):
    response = client.post(
        "/genetic-samples/", json={"patient_id": patient_id, "sample_type": "Blood", "sample_date": "2024-06-01"}
    )
    assert response.status_code == 200
    return response.json()["id"]


def test_create_genetic_variant(client):
    patient_id = create_patient(client)
    sample_id = create_sample(client, patient_id)

    response = client.post(
        "/genetic-variants/",
        json={
            "sample_id": sample_id,
            "chromosome": "1",
            "position": 12345,
            "ref_allele": "A",
            "alt_allele": "T",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["position"] == 12345
    assert data["sample_id"] == sample_id

    return data["id"]


def test_read_genetic_variant(client):
    variant_id = test_create_genetic_variant(client)

    response = client.get(f"/genetic-variants/{variant_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == variant_id


def test_read_genetic_variants(client):
    test_create_genetic_variant(client)

    response = client.get("/genetic-variants/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
