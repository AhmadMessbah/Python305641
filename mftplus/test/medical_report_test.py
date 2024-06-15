from mftplus.model.da.da import DataAccess
from mftplus.model.entity.person import Person
from mftplus.model.entity.medical_report import MedicalReport

medical_report = MedicalReport("stroke","2", None)
medical_report_da = DataAccess(MedicalReport)
medical_report_da.save(medical_report)
print(medical_report)

person = Person("ahmad","messbah")
person.medical_report = medical_report
person_da = DataAccess(Person)
person_da.save(person)
print(person)
