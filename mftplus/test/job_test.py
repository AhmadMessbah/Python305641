from mftplus.controller.job_controller import JobController
from mftplus.controller.job_controller import *
from mftplus.model.da.da import DataAccess
from mftplus.model.entity.job import Job
from mftplus.model.entity.person import Person



# print(JobController.find_all())
# print(JobController.save("programming","google","2000/10/10","2002/9/9"))
# print(JobController.edit(3,"None","google","2000/10/10","2002/9/9"))
JobController.remove(5)
# print(JobController.find_by_date_range("2000/10/9", "2001/9/9"))
# print(JobController.find_by_title("ali"))
# print(JobController.find_by_organisation("google"))