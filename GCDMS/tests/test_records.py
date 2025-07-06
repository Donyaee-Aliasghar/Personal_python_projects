def test_create_clinical_record(client, clear_tables):
    patient_data = {"name": "John Doe"}
    response = client.post("/patients/", json=patient_data)
    assert response.status_code == 200
    patient = response.json()

    clinical_record_data = {
        "patient_id": patient["id"],
        "visit_date": "2024-07-06",
        "diagnosis": "Flu",
        "treatment": "Rest and hydration",
    }
    response = client.post("/clinical-records/", json=clinical_record_data)
    assert response.status_code == 200
    data = response.json()
    assert data["patient_id"] == patient["id"]
    assert data["diagnosis"] == "Flu"


def test_read_clinical_record(client, clear_tables):
    patient_data = {"name": "John Doe"}
    response = client.post("/patients/", json=patient_data)
    assert response.status_code == 200
    patient = response.json()

    clinical_record_data = {
        "patient_id": patient["id"],
        "visit_date": "2024-07-06",
        "diagnosis": "Cold",
        "treatment": "Medicine",
    }
    response = client.post("/clinical-records/", json=clinical_record_data)
    assert response.status_code == 200
    record = response.json()

    response = client.get(f"/clinical-records/{record['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == record["id"]
    assert data["diagnosis"] == "Cold"


def test_read_clinical_records(client, clear_tables):
    patient_data = {"name": "Alice"}
    response = client.post("/patients/", json=patient_data)
    assert response.status_code == 200
    patient = response.json()

    records = [
        {"patient_id": patient["id"], "diagnosis": "Disease A", "visit_date": "2024-07-06"},
        {"patient_id": patient["id"], "diagnosis": "Disease B", "visit_date": "2024-07-06"},
    ]

    for rec in records:
        response = client.post("/clinical-records/", json=rec)
        assert response.status_code == 200

    response = client.get("/clinical-records/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 2
