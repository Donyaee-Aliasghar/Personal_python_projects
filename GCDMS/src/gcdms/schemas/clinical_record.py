from pydantic import BaseModel
from typing import Optional

class ClinicalRecordBase(BaseModel):
    patient_id: int
    diagnosis: str
    treatment: Optional[str] = None

class ClinicalRecordCreate(ClinicalRecordBase):
    pass

class ClinicalRecordOut(ClinicalRecordBase):
    id: int

    model_config = {
        "from_attributes": True
    }
