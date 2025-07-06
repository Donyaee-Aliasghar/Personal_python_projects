from pydantic import BaseModel
from typing import Optional


class GeneticSampleBase(BaseModel):
    patient_id: int
    sample_type: Optional[str] = None
    collected_at: Optional[str] = None


class GeneticSampleCreate(GeneticSampleBase):
    pass


class GeneticSampleOut(GeneticSampleBase):
    id: int

    model_config = {"from_attributes": True}
