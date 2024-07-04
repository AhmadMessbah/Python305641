from mftplus.controller.medical_report_controller import MedicalReportController
from mftplus.controller.person_controller import PersonController
from datetime import datetime
from mftplus.model.tools.validator import *

status, person1 = PersonController.save("roya", "mirhosseini")
now = datetime.today()
print(MedicalReportController.save("stroke", "neorology", now, person1))


print(MedicalReportController.findAll())

disease = disease_validator("heart attack","invalid disease")
print(disease)
#date_time = date_time_validator(now,"invalid date time")

#print(date_time)
