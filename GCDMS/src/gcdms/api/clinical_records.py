from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from gcdms.schemas import ClinicalRecord as sClinicalRecord, ClinicalRecordCreate as sClinicalRecordCreate
from gcdms.crud import create_clinical_records
from gcdms.dependencies import get_db

router = APIRouter(prefix="/clinical_records", tags=["clinical_records"])


@router.post("/", response_model=sClinicalRecord, status_code=status.HTTP_201_CREATED)
async def create_clinical_records(clinical_records: sClinicalRecordCreate, db: AsyncSession = Depends(get_db)):
    return await create_clinical_records(db=db, clinical_records=clinical_records)
