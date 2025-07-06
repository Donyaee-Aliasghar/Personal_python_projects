from sqlalchemy.orm import Session
from ..models.genetic_variant import GeneticVariant
from ..schemas.genetic_variant import GeneticVariantCreate


def create_variant(db: Session, variant: GeneticVariantCreate):
    db_variant = GeneticVariant(**variant.model_dump())
    db.add(db_variant)
    db.commit()
    db.refresh(db_variant)
    return db_variant


def get_variant(db: Session, variant_id: int):
    return db.query(GeneticVariant).filter(GeneticVariant.id == variant_id).first()


def get_variants(db: Session, skip: int = 0, limit: int = 10):
    return db.query(GeneticVariant).offset(skip).limit(limit).all()
