from mftplus.controller.exceptions.exeptions import MedicalReportNotFoundError
from mftplus.model.da.da import DataAccess
from mftplus.model.entity.medical_report import MedicalReport
from mftplus.model.tools.decorators import *


class MedicalReportService:
    @classmethod
    def save(cls,medical_report):
        medical_report_da = DataAccess(MedicalReport)
        medical_report_da.save(medical_report)
        return medical_report

    @classmethod
    def edit(cls,medical_report):
        medical_report_da = DataAccess(MedicalReport)
        if medical_report_da.find_by_id(medical_report.id):
            medical_report_da.edit(medical_report)
            return medical_report
        else:
            raise MedicalReportNotFoundError()

    @classmethod
    def remove(cls,id):
        medical_report_da = DataAccess(MedicalReport)
        if medical_report_da.find_by_id(id):
            return medical_report_da.remove(id)
        else:
            raise MedicalReportNotFoundError()

    @classmethod
    def find_all(cls,):
        medical_report_da = DataAccess(MedicalReport)
        return medical_report_da.find_all()

    @classmethod
    def find_by_id(cls,id):
        medical_report_da = DataAccess(MedicalReport)
        return medical_report_da.find_by_id(id)

    @classmethod
    def find_by_disease(cls,disease):
        medical_report_da = DataAccess(MedicalReport)
        return medical_report_da.find_by(MedicalReport.disease == disease)

