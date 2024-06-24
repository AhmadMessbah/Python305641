from sqlalchemy import Column, Integer, String, Boolean

from mftplus.model.entity.base import Base


# todo : roya : validator

class MedicalReport:
    __tablename__ = "medical_report_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _disease = Column("disease", String(20), nullable=False)
    _report_group = Column("report_group", String(20), nullable=False)
    _date_time = Column("date_time", String(20), nullable=False)
    _deleted = Column("deleted", Boolean, default=False)

    def __init__(self, disease, report_group, date_time, deleted=False):
        self.id = None
        self.disease = disease
        self.report_group = report_group
        self.date_time = date_time
        self.deleted = deleted

    def get_disease(self):
        return self._disease

    def set_disease(self, disease):
        self._disease = disease

    def get_report_group(self):
        return self._report_group

    def set_report_group(self, report_group):
        self._report_group = report_group

    def get_date_time(self):
        return self._date_time

    def set_date_time(self, date_time):
        self._date_time = date_time

    def get_deleted(self):
        return self._deleted

    def set_deleted(self, deleted):
        self._deleted = deleted
