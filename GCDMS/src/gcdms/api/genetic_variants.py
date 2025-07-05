from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.gcdms.schemas import GeneticVariant as sGeneticVariant, GeneticVariantCreate as sGeneticVariantCreate
from src.gcdms.crud import create_genetic_variants
from src.gcdms.dependencies import get_db

router = APIRouter(prefix="/genetic_variants", tags=["genetic_variants"])


@router.post("/", response_model=sGeneticVariant, status_code=status.HTTP_201_CREATED)
async def create_genetic_variants(genetic_variants: sGeneticVariantCreate, db: AsyncSession = Depends(get_db)):
    return await create_genetic_variants(db=db, genetic_variants=genetic_variants)
