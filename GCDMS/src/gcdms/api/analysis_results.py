from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from ..schemas.analysis_result import AnalysisResultCreate, AnalysisResultOut
from ..crud.analysis_result import create_result, get_result, get_results
from ..dependencies import get_db

router = APIRouter(prefix="/analysis-results", tags=["Analysis results"])


@router.post("/", response_model=AnalysisResultOut)
def create_result_endpoint(result: AnalysisResultCreate, db: Session = Depends(get_db)):
    return create_result(db, result)


@router.get("/{result_id}", response_model=AnalysisResultOut)
def read_result(result_id: int, db: Session = Depends(get_db)):
    return get_result(db, result_id)


@router.get("/", response_model=List[AnalysisResultOut])
def read_results(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_results(db, skip=skip, limit=limit)
