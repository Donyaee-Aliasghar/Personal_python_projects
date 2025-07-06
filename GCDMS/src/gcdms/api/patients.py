from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from ..schemas.patient import PatientCreate, PatientOut
from ..crud.patient import create_patient, get_patient, get_patients
from ..dependencies import get_db

router = APIRouter(prefix="/patients", tags=["Patients"])


@router.post("/", response_model=PatientOut)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    return create_patient(db, patient)


@router.get("/{patient_id}", response_model=PatientOut)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    return get_patient(db, patient_id)


@router.get("/", response_model=List[PatientOut])
def read_patients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_patients(db, skip=skip, limit=limit)
