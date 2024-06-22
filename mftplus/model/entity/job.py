from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from mftplus.model.entity.base import Base
from sqlalchemy.orm import relationship
from mftplus.model.tools.validator import *


class Job(Base):
    __tablename__ = "job_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _title = Column("title", String(20), nullable=False)
    _organisation = Column("organisation", String(20), nullable=False)
    _start_date = Column("start_date", Boolean, default=True)
    _end_date = Column("end_date", Boolean, default=True)
    _deleted = Column("deleted", Boolean, default=False)

    person_id = Column(Integer, ForeignKey("person_tbl.id") )
    person = relationship("Person")

    def __init__(self,title,organisation,start_date,end_date, status=True,deleted = False):
        self.id = None
        self.title = title
        self.organisation = organisation
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.deleted = deleted
        self.person = None

    def get_id(self):
        return self._id
    def set_id(self,id):
        self._id = id

    def get_title(self):
        return self._title
    def set_title(self,title):
        if isinstance(title,str) and title_validator(title):
            self._title = title

    def get_organisation(self):
        return self._organisation
    def set_organisation(self,organisation):
        if isinstance(organisation, str) and title_validator(organisation):
            self._organisation = organisation

    def get_start_date(self):
        return self._start_date
    def set_start_date(self,start_date):
        self._start_date = start_date

    def get_end_date(self):
        return self._end_date
    def set_end_date(self,end_date):
        self._end_date = end_date

    def get_status(self):
        return self.status
    def set_status(self,status):
        if isinstance(status,bool):
            self.status = status
        else:
            raise ValueError("Status must be boolean")
    def get_deleted(self):
        return self._deleted
    def set_deleted(self,deleted):
        self._deleted = deleted

    id = property(get_id,set_id)
    title = property(get_title,set_title)
    organisation = property(get_organisation,set_organisation)
    start_date = property(get_start_date,set_start_date)
    end_date = property(get_end_date,set_end_date)
    status = property(get_status,set_status)
    deleted = property(get_deleted,set_deleted)
