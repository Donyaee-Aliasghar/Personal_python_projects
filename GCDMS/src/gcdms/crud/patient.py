from sqlalchemy.orm import Session
from ..models.patient import Patient
from ..schemas.patient import PatientCreate


def create_patient(db: Session, patient: PatientCreate):
    db_patient = Patient(**patient.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


def get_patient(db: Session, patient_id: int):
    return db.query(Patient).filter(Patient.id == patient_id).first()


def get_patients(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Patient).offset(skip).limit(limit).all()
