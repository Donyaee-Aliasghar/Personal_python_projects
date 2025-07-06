from sqlalchemy.orm import Session
from ..models.genetic_sample import GeneticSample
from ..schemas.genetic_sample import GeneticSampleCreate


def create_sample(db: Session, sample: GeneticSampleCreate):
    db_sample = GeneticSample(**sample.model_dump())
    db.add(db_sample)
    db.commit()
    db.refresh(db_sample)
    return db_sample


def get_sample(db: Session, sample_id: int):
    return db.query(GeneticSample).filter(GeneticSample.id == sample_id).first()


def get_samples(db: Session, skip: int = 0, limit: int = 10):
    return db.query(GeneticSample).offset(skip).limit(limit).all()
