# Defining models with SQLAlchemy

from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, Text, JSON
from sqlalchemy.orm import relationship
from .database import Base
import datetime


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    patient = relationship("Patient", back_populates="user", uselist=False)


class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    name = Column(String(100), nullable=False)
    birthdate = Column(Date, nullable=True)
    gender = Column(String(10), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    user = relationship("User", back_populates="patient")
    clinical_records = relationship("ClinicalRecord", back_populates="patient")
    genetic_samples = relationship("GeneticSample", back_populates="patient")


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


class AnalysisResult(Base):
    __tablename__ = "analysis_results"
    id = Column(Integer, primary_key=True, index=True)
    sample_id = Column(Integer, ForeignKey("genetic_samples.id"), nullable=False)
    analysis_type = Column(String(100), nullable=False)
    result_json = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    sample = relationship("GeneticSample", back_populates="analysis_results")
