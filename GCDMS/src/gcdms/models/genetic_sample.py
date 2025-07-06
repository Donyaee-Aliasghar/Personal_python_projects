from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from ..database import Base
import datetime


class GeneticSample(Base):
    __tablename__ = "genetic_samples"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    sample_date = Column(Date, nullable=False)
    sample_type = Column(String(50), nullable=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    patient = relationship("Patient", back_populates="genetic_samples")
    genetic_variants = relationship("GeneticVariant", back_populates="sample")
    analysis_results = relationship("AnalysisResult", back_populates="sample")
