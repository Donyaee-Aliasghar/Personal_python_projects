from pydantic import BaseModel
from typing import Optional


class GeneticVariantBase(BaseModel):
    sample_id: int
    chromosome: str
    position: Optional[int] = None
    ref_allele: Optional[str] = None
    alt_allele: Optional[str] = None
    impact: Optional[str] = None
    annotation: Optional[str] = None


class GeneticVariantCreate(GeneticVariantBase):
    pass


class GeneticVariantOut(GeneticVariantBase):
    id: int

    model_config = {"from_attributes": True}
