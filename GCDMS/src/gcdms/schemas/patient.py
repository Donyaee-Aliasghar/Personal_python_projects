from pydantic import BaseModel
from typing import Optional


class PatientBase(BaseModel):
    name: str
    age: Optional[int] = None
    gender: Optional[str] = None


class PatientCreate(PatientBase):
    pass


class PatientOut(PatientBase):
    id: int

    model_config = {"from_attributes": True}
