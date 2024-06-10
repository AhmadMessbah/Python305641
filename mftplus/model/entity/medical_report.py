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

    # getter / setter