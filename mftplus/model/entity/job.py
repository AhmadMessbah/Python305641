from sqlalchemy import Column, Integer, String, Boolean

from mftplus.model.entity.base import Base


class Job(Base):
    __tablename__ = "person_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _title = Column("title", String(20), nullable=False)
    _organisation = Column("organisation", String(20), nullable=False)
    _start_date = Column("start_date", Boolean, default=True)
    _end_date = Column("end_date", Boolean, default=True)
    _deleted = Column("deleted", Boolean, default=False)

    def __init__(self,title,organisation,start_date,end_date, status=True,deleted = False):
        self.id = None
        self.title = title
        self.organisation = organisation
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.deleted = deleted

    # getter / setter

    def get_id(self):
        return self._id
    def set_id(self,id):
        self._id = id

    def get_title(self):
        return self._title
    def set_title(self,title):
        self._title = title

    def get_organisation(self):
        return self._organisation
    def set_organisation(self,organisation):
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
        self.status = status
    def get_deleted(self):
        return self._deleted
    def set_deleted(self,deleted):
        self._deleted = deleted
