from datetime import datetime
from mftplus.controller.medical_report_controller import MedicalReport
from mftplus.controller.person_controller import PersonController
from mftplus.controller.medical_report_controller import MedicalReportController

from datetime import datetime
now = datetime.now()

status, person1 = PersonController.save("farbod", "orang")
now = datetime.today()
print(MedicalReportController.save("ddd","drtd",now))


# print(PersonController.findAll())