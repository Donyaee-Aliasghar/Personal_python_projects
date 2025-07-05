from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.gcdms.schemas import AnalysisResult as sAnalysisResult, AnalysisResultCreate as sAnalysisResultCreate
from src.gcdms.crud import create_analysis_results
from src.gcdms.dependencies import get_db

router = APIRouter(prefix="/analysis_results", tags=["analysis_results"])


@router.post("/", response_model=sAnalysisResult, status_code=status.HTTP_201_CREATED)
async def create_analysis_results(analysis_results: sAnalysisResultCreate, db: AsyncSession = Depends(get_db)):
    return await create_analysis_results(db=db, analysis_results=analysis_results)
