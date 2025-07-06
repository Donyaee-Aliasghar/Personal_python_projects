import shutil
import os

from fastapi import APIRouter, File, UploadFile, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..dependencies import get_db
from ..crud import process_vcf_file

router = APIRouter(prefix="/files", tags=["files"])

UPLOAD_DIR = "uploaded_files"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    # Save temporary file
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Processing the saved file
    try:
        result = await process_vcf_file(file_location, db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing file: {e}")

    return {"filename": file.filename, "processing_result": result}
