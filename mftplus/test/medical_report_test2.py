from mftplus.model.entity.medical_report import MedicalReport
from mftplus.model.entity.person import Person
from datetime import datetime

doctor = Person("roya","mirhosseini")
now = datetime.today()
medical_report = MedicalReport("heart attack","heart",now,doctor)
print(doctor)
print(medical_report)
