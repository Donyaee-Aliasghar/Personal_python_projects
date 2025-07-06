from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from ..schemas.genetic_sample import GeneticSampleCreate, GeneticSampleOut
from ..crud.genetic_sample import create_sample, get_sample, get_samples
from ..dependencies import get_db

router = APIRouter(prefix="/genetic-samples", tags=["Genetic samples"])


@router.post("/", response_model=GeneticSampleOut)
def create_sample_endpoint(sample: GeneticSampleCreate, db: Session = Depends(get_db)):
    return create_sample(db, sample)


@router.get("/{sample_id}", response_model=GeneticSampleOut)
def read_sample(sample_id: int, db: Session = Depends(get_db)):
    return get_sample(db, sample_id)


@router.get("/", response_model=List[GeneticSampleOut])
def read_samples(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_samples(db, skip=skip, limit=limit)
