import pysam
from Bio import SeqIO

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from .schemas import (
    UserCreate,
    PatientCreate,
    ClinicalRecordCreate,
    GeneticSampleCreate,
    GeneticVariantCreate,
    AnalysisResultCreate,
)
from .models import (
    User as mUser,
    Patient as mPatient,
    ClinicalRecord as mClinicalRecord,
    GeneticSample as mGeneticSample,
    GeneticVariant as mGeneticVariant,
    AnalysisResult as mAnalysisResult,
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


async def get_user_by_username(db: AsyncSession, username: str):
    result = await db.execute(select(mUser).where(mUser.username == username))
    return result.scalars().first()


async def create_user(db: AsyncSession, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = mUser(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        role=user.role,
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def get_patient(db: AsyncSession, patient_id: int):
    result = await db.execute(select(mPatient).where(mPatient.id == patient_id))
    return result.scalars().first()


async def create_patient(db: AsyncSession, patient: PatientCreate):
    db_patient = mPatient(**patient.dict())
    db.add(db_patient)
    await db.commit()
    await db.refresh(db_patient)
    return db_patient


async def get_genetic_variants(db: AsyncSession, geneticvariant_id: int):
    result = await db.execute(select(mGeneticVariant).where(mGeneticVariant.id == geneticvariant_id))
    return result.scalars().first()


async def create_genetic_variants(db: AsyncSession, geneticvariant: GeneticVariantCreate):
    db_geneticvariant = mGeneticVariant(**geneticvariant.dict())
    db.add(db_geneticvariant)
    await db.commit()
    await db.refresh(db_geneticvariant)
    return db_geneticvariant


async def get_genetic_samples(db: AsyncSession, geneticsample_id: int):
    result = await db.execute(select(mGeneticSample).where(mGeneticSample.id == geneticsample_id))
    return result.scalars().first()


async def create_genetic_samples(db: AsyncSession, geneticsample: GeneticSampleCreate):
    db_geneticsample = mGeneticSample(**geneticsample.dict())
    db.add(db_geneticsample)
    await db.commit()
    await db.refresh(db_geneticsample)
    return db_geneticsample


async def get_clinical_records(db: AsyncSession, clinicalrecords_id: int):
    result = await db.execute(select(mClinicalRecord).where(mClinicalRecord.id == clinicalrecords_id))
    return result.scalars().first()


async def create_clinical_records(db: AsyncSession, clinicalrecords: ClinicalRecordCreate):
    db_clinicalrecords = mClinicalRecord(**clinicalrecords.dict())
    db.add(db_clinicalrecords)
    await db.commit()
    await db.refresh(db_clinicalrecords)
    return db_clinicalrecords


async def create_analysis_results(db: AsyncSession, analysisresults_id: int):
    result = await db.execute(select(mAnalysisResult).where(mAnalysisResult.id == analysisresults_id))
    return result.scalars().first()


async def create_analysis_results(db: AsyncSession, analysisresults: AnalysisResultCreate):
    db_analysisresults = mAnalysisResult(**analysisresults.dict())
    db.add(db_analysisresults)
    await db.commit()
    await db.refresh(db_analysisresults)
    return db_analysisresults


async def process_vcf_file(filepath: str, db: AsyncSession):
    vcf_reader = pysam.VariantFile(filepath)

    variants_added = 0

    for record in vcf_reader:
        alt_alleles = [str(alt) for alt in record.alts] if record.alts else []

        variant = mGeneticVariant(
            sample_id=1,
            chromosome=str(record.contig),  # CHROM
            position=record.pos,  # POS
            ref_allele=record.ref,  # REF
            alt_allele=",".join(alt_alleles),  # ALT
            impact=None,
            annotation=None,
        )
        db.add(variant)
        variants_added += 1

    await db.commit()
    return f"{variants_added} variants added to database."


# async def process_fasta_file(filepath: str, db: AsyncSession):
#     fasta = pysam.FastaFile(filepath)
#     sequences_added = 0

#     for seq_name in fasta.references:
#         sequence = fasta.fetch(seq_name)

#         seq_record = GeneticSequence(
#             sample_id=1,
#             header=seq_name,
#             sequence=sequence,
#         )

#         db.add(seq_record)
#         sequences_added += 1

#     await db.commit()
#     return f"{sequences_added} sequences added to database."
