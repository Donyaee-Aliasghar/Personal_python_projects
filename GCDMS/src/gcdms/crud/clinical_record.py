from sqlalchemy.orm import Session
from ..models.clinical_record import ClinicalRecord
from ..schemas.clinical_record import ClinicalRecordCreate


def create_record(db: Session, record: ClinicalRecordCreate):
    db_record = ClinicalRecord(**record.model_dump())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record


def get_record(db: Session, record_id: int):
    return db.query(ClinicalRecord).filter(ClinicalRecord.id == record_id).first()


def get_records(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ClinicalRecord).offset(skip).limit(limit).all()
