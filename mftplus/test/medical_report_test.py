from mftplus.controller.medical_report_controller import MedicalReportController
from mftplus.controller.person_controller import PersonController
from datetime import datetime

status, person1 = PersonController.save("roya", "mirhosseini")
now = datetime.today()
print(MedicalReportController.save("stroke", "neorology", now, person1))


print(MedicalReportController.findAll())
