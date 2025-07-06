=================== Goal ====================
The goal is to design a robust and flexible relational database that can store and manage diverse genetic and clinical data in a systematic manner. The database should:

+.Maintain data integrity (foreign keys and constraints)
+.Be scalable and extensible
+.Provide flexibility to store structured data (e.g. JSONB)
+.Store data securely and in a standardized manner

=================== Entities ====================
1.User:
System user, including various roles such as admin, researcher, doctor, patient
Login information and accesses are stored here.

2.Patient:
Patient who may or may not have a user account
Including personal information and basic medical details.

3.ClinicalRecord:
Patients' clinical records including visits, diagnoses, treatments and notes.

4.GeneticSample:
Genetic samples taken from patients
Including sampling date, sample type and description.

5.GeneticVariant:
Genetic variants identified in samples
Including chromosomal location, alleles, impact and description.

6.AnalysisResult:
Results of various analyses on samples
Including analysis type, result in JSON format and recording date.

=================== how to run ====================
+. poetry run uvicorn src.gcdms.main:app --reload
=================== how to test ====================
+. config test ==> poetry run pytest 
+. api tests ==> pytest tests/test_*.py