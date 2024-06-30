from mftplus.model.entity.medical_report import MedicalReport
from mftplus.model.service.medical_report_service import MedicalReportService
from mftplus.model.tools.logger import Logger


class MedicalReportController:
    @staticmethod
    def save(disease,report_group,date_time,doctor):
        try:
            medical_report = MedicalReport(disease,report_group,date_time,doctor)
            MedicalReportService.save(medical_report)
            Logger.info(f"MedicalReport Saved - {medical_report}")
            return True, medical_report
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def edit(disease, report_group, date_time,doctor):
        try:
            medical_report = MedicalReport(disease,report_group,date_time,doctor)
            medical_report.id = id
            MedicalReportService.edit(medical_report)
            Logger.info(f"MedicalReport Edited - {medical_report}")
            return True,medical_report
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"


    @staticmethod
    def remove(id):
        try:
            medical_report = MedicalReportService.remove(id)
            Logger.info(f"MedicalReport Removed - {medical_report}")
            return True,medical_report
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def findAll():
        try:
            medical_report_list = MedicalReportService.find_all()
            Logger.info(f"MedicalReport FindAll()")
            return True,medical_report_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"


    @staticmethod
    def find_by_id(id):
        try:
            medical_report =  MedicalReportService.find_by_id(id)
            Logger.info(f"MedicalReport FindById({id})")
            return True,medical_report
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_disease(disease):
        try:
            medical_report_list = MedicalReportService.find_by_disease(disease)
            Logger.info(f"MedicalReport FindByDisease({disease})")
            return True, medical_report_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"
