from pydantic import BaseModel
from typing import Optional, Any
from datetime import date


class AnalysisResultBase(BaseModel):
    sample_id: int
    sample_date: date
    analysis_type: str
    result_json: Any
    confidence: Optional[float] = None


class AnalysisResultCreate(AnalysisResultBase):
    pass


class AnalysisResultOut(AnalysisResultBase):
    id: int

    model_config = {"from_attributes": True}
