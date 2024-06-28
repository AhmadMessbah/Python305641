from mftplus.model.da.da import DataAccess
from mftplus.model.entity.job import Job
from mftplus.controller.exceptions.exeptions import JobNotFoundError

class JobService:
    @staticmethod
    def save(job):
        job_da = DataAccess(job)
        job_da.save(job)
        return job

    @staticmethod
    def edit(job):
        job_da = DataAccess(Job)
        if job_da.find_by_id(job.id):
            job_da.edit(job)
            return job
        else:
            raise JobNotFoundError()

    @staticmethod
    def remove(id):
        job_da = DataAccess(Job)
        if job_da.find_by_id(id):
            return job_da.remove(id)
        else:
            raise JobNotFoundError()

    @staticmethod
    def find_all():
        job_da = DataAccess(Job)
        return job_da.find_all()

    @staticmethod
    def find_by_id(id):
        job_da = DataAccess(Job)
        return job_da.find_by_id(id)


    # todo : find by title, organisation , date_range

    @staticmethod
    def find_by_title(title):
        job_da = DataAccess(Job)
        return job_da.find_by(Job.title == title)

    @staticmethod
    def find_by_organisation(organisation):
        job_da = DataAccess(Job)
        return job_da.find_by(Job.organisation == organisation)

    @staticmethod
    def find_by_date_range(date_range):
        job_da = DataAccess(Job)
        return job_da.find_by(job_da.start_date <= date_range <= job_da.end_date)
