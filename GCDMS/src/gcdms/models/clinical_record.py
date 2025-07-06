from sqlalchemy import Column, Integer, Date, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from ..database import Base
import datetime


class ClinicalRecord(Base):
    __tablename__ = "clinical_records"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    visit_date = Column(Date, nullable=False)
    diagnosis = Column(Text, nullable=True)
    treatment = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    patient = relationship("Patient", back_populates="clinical_records")
