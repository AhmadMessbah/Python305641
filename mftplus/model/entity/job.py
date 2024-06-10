from sqlalchemy import Column, Integer, String, Boolean

from mftplus.model.entity.base import Base


class Person(Base):
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

    # getter / setter