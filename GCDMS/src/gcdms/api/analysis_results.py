from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas import AnalysisResult as sAnalysisResult, AnalysisResultCreate as sAnalysisResultCreate
from ..crud import create_analysis_results
from ..dependencies import get_db

router = APIRouter(prefix="/analysis_results", tags=["analysis_results"])


@router.post("/", response_model=sAnalysisResult, status_code=status.HTTP_201_CREATED)
async def create_analysis_results(analysis_results: sAnalysisResultCreate, db: AsyncSession = Depends(get_db)):
    return await create_analysis_results(db=db, analysis_results=analysis_results)
