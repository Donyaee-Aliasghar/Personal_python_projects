# Definition of Pydantic Schemas

from pydantic import BaseModel, EmailStr
from typing import Optional, List
import datetime


class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    created_at: datetime.datetime

    class Config:
        model_config = {"from_attributes": True}


class PatientBase(BaseModel):
    name: str
    birthdate: Optional[datetime.date] = None
    gender: Optional[str] = None
    user_id: Optional[int] = None


class PatientCreate(PatientBase):
    pass


class Patient(PatientBase):
    id: int
    created_at: datetime.datetime
    clinical_records: List["ClinicalRecord"] = []
    genetic_samples: List["GeneticSample"] = []

    class Config:
        model_config = {"from_attributes": True}


class ClinicalRecordBase(BaseModel):
    visit_date: datetime.date
    diagnosis: Optional[str] = None
    treatment: Optional[str] = None
    notes: Optional[str] = None
    patient_id: int


class ClinicalRecordCreate(ClinicalRecordBase):
    pass


class ClinicalRecord(ClinicalRecordBase):
    id: int
    created_at: datetime.datetime

    class Config:
        model_config = {"from_attributes": True}


class GeneticSampleBase(BaseModel):
    sample_date: datetime.date
    sample_type: Optional[str] = None
    description: Optional[str] = None
    patient_id: int


class GeneticSampleCreate(GeneticSampleBase):
    pass


class GeneticSample(GeneticSampleBase):
    id: int
    created_at: datetime.datetime
    genetic_variants: List["GeneticVariant"] = []
    analysis_results: List["AnalysisResult"] = []

    class Config:
        model_config = {"from_attributes": True}


class GeneticVariantBase(BaseModel):
    chromosome: str
    position: int
    ref_allele: Optional[str] = None
    alt_allele: Optional[str] = None
    impact: Optional[str] = None
    annotation: Optional[str] = None
    sample_id: int


class GeneticVariantCreate(GeneticVariantBase):
    pass


class GeneticVariant(GeneticVariantBase):
    id: int
    created_at: datetime.datetime

    class Config:
        model_config = {"from_attributes": True}


class AnalysisResultBase(BaseModel):
    analysis_type: str
    result_json: dict
    sample_id: int


class AnalysisResultCreate(AnalysisResultBase):
    pass


class AnalysisResult(AnalysisResultBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        model_config = {"from_attributes": True}
