def test_create_analysis_result(client, clear_tables):
    patient_data = {"name": "Test Patient"}
    patient_resp = client.post("/patients/", json=patient_data)
    assert patient_resp.status_code == 200
    patient = patient_resp.json()

    sample_data = {"patient_id": patient["id"], "sample_type": "blood", "sample_date": "2025-07-06"}
    sample_resp = client.post("/genetic-samples/", json=sample_data)
    assert sample_resp.status_code == 200
    sample = sample_resp.json()

    result_data = {
        "sample_id": sample["id"],
        "analysis_type": "variant_calling",
        "result_json": {"variant_count": 5, "details": ["var1", "var2"]},
        "confidence": 0.95,
        "sample_date": "2024-07-06",
    }

    response = client.post("/analysis-results/", json=result_data)
    assert response.status_code == 200
    data = response.json()
    assert data["sample_id"] == sample["id"]
    assert data["analysis_type"] == "variant_calling"
    assert data["result_json"] == {"variant_count": 5, "details": ["var1", "var2"]}
    assert data["confidence"] == 0.95
    assert data["sample_date"] == "2024-07-06"

    return data


def test_read_analysis_result(client, clear_tables):
    created = test_create_analysis_result(client, clear_tables)

    response = client.get(f"/analysis-results/{created['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == created["id"]


def test_read_analysis_results(client, clear_tables):
    test_create_analysis_result(client, clear_tables)

    response = client.get("/analysis-results/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
