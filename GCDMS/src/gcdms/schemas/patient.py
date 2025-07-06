from pydantic import BaseModel
from typing import Optional
from datetime import date


class PatientBase(BaseModel):
    name: str
    birthdate: Optional[date] = None
    gender: Optional[str] = None


class PatientCreate(PatientBase):
    pass


class PatientOut(PatientBase):
    id: int

    model_config = {"from_attributes": True}
