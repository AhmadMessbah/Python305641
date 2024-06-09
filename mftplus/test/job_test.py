from mftplus.model.da.da import DataAccess
from mftplus.model.entity.job import Job
from mftplus.model.entity.person import Person

person = Person("ali","omidy")
person_da = DataAccess(Person)
person_da.save(person)
print(person)


job = Job("programming","google","2010/10/10","2020/10/20","termination of cooperation")
job_da = DataAccess(job)
job.person = person
job_da.save(job)
print(job)
