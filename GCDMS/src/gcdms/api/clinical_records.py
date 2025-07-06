from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from ..schemas.clinical_record import ClinicalRecordCreate, ClinicalRecordOut
from ..crud.clinical_record import create_record, get_record, get_records
from ..dependencies import get_db

router = APIRouter(prefix="/clinical-records", tags=["Clinical records"])


@router.post("/", response_model=ClinicalRecordOut)
def create_clinical_record(record: ClinicalRecordCreate, db: Session = Depends(get_db)):
    return create_record(db, record)


@router.get("/{record_id}", response_model=ClinicalRecordOut)
def read_clinical_record(record_id: int, db: Session = Depends(get_db)):
    return get_record(db, record_id)


@router.get("/", response_model=List[ClinicalRecordOut])
def read_clinical_records(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_records(db, skip=skip, limit=limit)
