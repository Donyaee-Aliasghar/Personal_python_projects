from pydantic import BaseModel
from typing import Optional
from datetime import date


class ClinicalRecordBase(BaseModel):
    patient_id: int
    diagnosis: str
    visit_date: date
    treatment: Optional[str] = None


class ClinicalRecordCreate(ClinicalRecordBase):
    pass


class ClinicalRecordOut(ClinicalRecordBase):
    id: int

    model_config = {"from_attributes": True}
