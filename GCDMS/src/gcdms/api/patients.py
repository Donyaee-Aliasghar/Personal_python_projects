from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas import Patient as sPatient, PatientCreate as sPatientCreate
from ..crud import create_patient
from ..dependencies import get_db

router = APIRouter(prefix="/patients", tags=["patients"])


@router.post("/", response_model=sPatient, status_code=status.HTTP_201_CREATED)
async def create_patient(patient: sPatientCreate, db: AsyncSession = Depends(get_db)):
    return await create_patient(db=db, patient=patient)
