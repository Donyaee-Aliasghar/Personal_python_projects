from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from gcdms.schemas import Patient as sPatient, PatientCreate as sPatientCreate
from gcdms.crud import create_patient
from gcdms.dependencies import get_db

router = APIRouter(prefix="/patients", tags=["patients"])


@router.post("/", response_model=sPatient, status_code=status.HTTP_201_CREATED)
async def create_patient(patient: sPatientCreate, db: AsyncSession = Depends(get_db)):
    return await create_patient(db=db, patient=patient)
