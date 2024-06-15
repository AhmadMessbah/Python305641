from mftplus.model.da.da import DataAccess
from mftplus.model.entity.job import Job

job = Job("programming","google","2010/10/10","2020/10/20","termination of cooperation")

person_da = DataAccess(job)
person_da.save(job)

print(job)