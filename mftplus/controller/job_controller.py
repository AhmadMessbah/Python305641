from mftplus.model.entity.job import Job
from mftplus.model.service.job_service import JobService
from mftplus.model.tools.logger import Logger

class JobController:
    @staticmethod
    def save(title, organisation, start_date, end_date):
        try:
            job = Job(title, organisation, start_date, end_date)
            JobService.save(job)
            Logger.info(f"Job saved {job}")
            return True, job
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def edit(id,title, organisation, start_date, end_date):
        try:
            job = Job(title, organisation, start_date, end_date)
            job.id = id
            JobService.edit(job)
            Logger.info(f"Job Edited - {job}")
            return True,job
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"


    @staticmethod
    def remove(id):
        try:
            job = JobService.remove(id)
            Logger.info(f"Job Removed - {job}")
            return True,job
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_all():
        try:
            job_list = JobService.find_all()
            Logger.info(f"Job FindAll()")
            return True,job_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_title(title):
        try:
            job_list = JobService.find_by_title(title)
            Logger.info(f"Job FindByTitle({title})")
            return True,job_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_date_range(date_range):
        try:
            job_list = JobService.find_by_date_range(date_range)
            Logger.info(f"Job FindByDateRange({date_range})")
            return True,job_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_organisation(organisation):
        try:
            job_list = JobService.find_by_organisation(organisation)
            Logger.info(f"Job FindByOrganisation({organisation})")
            return True,job_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

