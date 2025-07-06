from sqlalchemy import Column, Integer, Date, Float, String, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from ..database import Base
import datetime


class AnalysisResult(Base):
    __tablename__ = "analysis_results"
    id = Column(Integer, primary_key=True, index=True)
    sample_id = Column(Integer, ForeignKey("genetic_samples.id"), nullable=False)
    sample_date = Column(Date, nullable=False)
    analysis_type = Column(String(100), nullable=False)
    confidence = Column(Float, nullable=True)
    result_json = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    sample = relationship("GeneticSample", back_populates="analysis_results")
