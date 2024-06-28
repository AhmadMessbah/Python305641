from mftplus.controller.exceptions.exeptions import MedicalReportNotFoundError
from mftplus.model.da.da import DataAccess
from mftplus.model.entity.medical_report import MedicalReport


class MedicalReportService:
    @staticmethod
    def save(medical_report):
        medical_report_da = DataAccess(MedicalReport)
        medical_report_da.save(medical_report)
        return medical_report

    @staticmethod
    def edit(medical_report):
        medical_report_da = DataAccess(MedicalReport)
        if medical_report_da.find_by_id(medical_report.id):
            medical_report_da.edit(medical_report)
            return medical_report
        else:
            raise MedicalReportNotFoundError()

    @staticmethod
    def remove(id):
        medical_report_da = DataAccess(MedicalReport)
        if medical_report_da.find_by_id(id):
            return medical_report_da.remove(id)
        else:
            raise MedicalReportNotFoundError()

    @staticmethod
    def find_all():
        medical_report_da = DataAccess(MedicalReport)
        return medical_report_da.find_all()

    @staticmethod
    def find_by_id(id):
        medical_report_da = DataAccess(MedicalReport)
        return medical_report_da.find_by_id(id)

    @staticmethod
    def find_by_disease(disease):
        medical_report_da = DataAccess(MedicalReport)
        return medical_report_da.find_by(MedicalReport.disease == disease)
