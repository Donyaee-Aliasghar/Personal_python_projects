from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from ..database import Base
import datetime


class GeneticVariant(Base):
    __tablename__ = "genetic_variants"
    id = Column(Integer, primary_key=True, index=True)
    sample_id = Column(Integer, ForeignKey("genetic_samples.id"), nullable=False)
    chromosome = Column(String(5), nullable=False)
    position = Column(Integer, nullable=False)
    ref_allele = Column(String(50), nullable=True)
    alt_allele = Column(String(50), nullable=True)
    impact = Column(String(50), nullable=True)
    annotation = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    sample = relationship("GeneticSample", back_populates="genetic_variants")
