from pydantic import BaseModel
from typing import Optional

class GeneticVariantBase(BaseModel):
    sample_id: int
    variant_type: str
    position: Optional[int] = None

class GeneticVariantCreate(GeneticVariantBase):
    pass

class GeneticVariantOut(GeneticVariantBase):
    id: int

    model_config = {
        "from_attributes": True
    }
