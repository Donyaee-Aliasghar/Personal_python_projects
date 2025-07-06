from pydantic import BaseModel
from typing import Optional

class AnalysisResultBase(BaseModel):
    variant_id: int
    result: str
    confidence: Optional[float] = None

class AnalysisResultCreate(AnalysisResultBase):
    pass

class AnalysisResultOut(AnalysisResultBase):
    id: int

    model_config = {
        "from_attributes": True
    }
