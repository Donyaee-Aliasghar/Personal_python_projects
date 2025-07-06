from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from ..schemas.genetic_variant import GeneticVariantCreate, GeneticVariantOut
from ..crud.genetic_variant import create_variant, get_variant, get_variants
from ..dependencies import get_db

router = APIRouter(prefix="/genetic-variants", tags=["Genetic variants"])


@router.post("/", response_model=GeneticVariantOut)
def create_variant_endpoint(variant: GeneticVariantCreate, db: Session = Depends(get_db)):
    return create_variant(db, variant)


@router.get("/{variant_id}", response_model=GeneticVariantOut)
def read_variant(variant_id: int, db: Session = Depends(get_db)):
    return get_variant(db, variant_id)


@router.get("/", response_model=List[GeneticVariantOut])
def read_variants(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_variants(db, skip=skip, limit=limit)
