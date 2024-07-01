
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey

from mftplus.model.entity.base import Base
from sqlalchemy.orm import relationship
from mftplus.model.tools.validator import *
from datetime import datetime
from mftplus.model.tools.validator import date_time_validator


# todo : roya : validator

class MedicalReport(Base):
    __tablename__ = "medical_report_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _disease = Column("disease", String(20), nullable=False)
    _report_group = Column("report_group", String(20), nullable=False)
    _date_time = Column("date_time", DateTime, nullable=False)
    doctor_id = Column("doctor_id", Integer, ForeignKey("person_tbl.id"))
    _deleted = Column("deleted", Boolean, default=False)

    doctor = relationship("Person")

    def __init__(self, disease, report_group, date_time,doctor, deleted=False):
        self.id = None
        self.disease = disease
        self.report_group = report_group
        self.date_time = date_time
        self.doctor = doctor
        self.deleted = deleted

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_disease(self):
        return self._disease

    def set_disease(self, disease):
        self._disease = disease_validator(disease,"invalid disease")

    def get_report_group(self):
        return self._report_group

    def set_report_group(self, report_group):
        self._report_group = report_group

    def get_date_time(self):
        return self._date_time

    @date_time_validator(message="invalid date time")
    def set_date_time(self, date_time):
        self._date_time = date_time

    def get_deleted(self):
        return self._deleted

    def set_deleted(self, deleted):
        self._deleted = deleted

    id = property(get_id, set_id)
    disease = property(get_disease, set_disease)
    report_group = property(get_report_group, set_report_group)
    date_time = property(get_date_time, set_date_time)
    deleted = property(get_deleted, set_deleted)



