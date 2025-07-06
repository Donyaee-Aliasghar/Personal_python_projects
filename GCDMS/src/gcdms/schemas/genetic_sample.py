from pydantic import BaseModel
from typing import Optional
from datetime import date

class GeneticSampleBase(BaseModel):
    patient_id: int
    sample_type: Optional[str] = None
    sample_date: Optional[date] = None


class GeneticSampleCreate(GeneticSampleBase):
    pass


class GeneticSampleOut(GeneticSampleBase):
    id: int

    model_config = {"from_attributes": True}
