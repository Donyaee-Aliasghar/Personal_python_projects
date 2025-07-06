from sqlalchemy.orm import Session
from ..models.analysis_result import AnalysisResult
from ..schemas.analysis_result import AnalysisResultCreate


def create_result(db: Session, result: AnalysisResultCreate):
    db_result = AnalysisResult(**result.model_dump())
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result


def get_result(db: Session, result_id: int):
    return db.query(AnalysisResult).filter(AnalysisResult.id == result_id).first()


def get_results(db: Session, skip: int = 0, limit: int = 10):
    return db.query(AnalysisResult).offset(skip).limit(limit).all()
