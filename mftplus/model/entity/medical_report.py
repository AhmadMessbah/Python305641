from sqlalchemy import Column, Integer, String, Boolean

from mftplus.model.entity.base import Base


class MedicalReport(Base):
    __tablename__ = "medicalreport_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _disease = Column("disease", String(20), nullable=False)
    _group = Column("group", String(20), nullable=False)
    _datetime = Column("datetime", String(20), nullable=False)
    _deleted = Column("deleted", Boolean, default=False)

    def __init__(self, disease,group,datetime, deleted=False):
        self.id = None
        self.disease = disease
        self.group = group
        self.datetime = datetime
        self.deleted = deleted

    def get_disease(self):
        return self._disease
    def set_disease(self,disease):
        self._disease = disease



    def get_group(self):
        return self._group
    def set_group(self, group):
        self._group = group



    def get_datetime(self):
        return self._datetime
    def set_datetime(self,datetime):
        self._datetime = datetime


    def get_deleted(self):
        return self._deleted
    def set_deleted(self,deleted):
        self._deleted = deleted
