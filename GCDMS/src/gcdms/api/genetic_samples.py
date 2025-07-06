from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas import GeneticSample as sGeneticSample, GeneticSampleCreate as sGeneticSampleCreate
from ..crud import create_genetic_samples
from ..dependencies import get_db

router = APIRouter(prefix="/genetic_samples", tags=["genetic_samples"])


@router.post("/", response_model=sGeneticSample, status_code=status.HTTP_201_CREATED)
async def create_genetic_samples(genetic_samples: sGeneticSampleCreate, db: AsyncSession = Depends(get_db)):
    return await create_genetic_samples(db=db, genetic_samples=genetic_samples)
