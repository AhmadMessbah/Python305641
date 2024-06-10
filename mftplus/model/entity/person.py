from sqlalchemy import Column, Integer, String, Boolean

from mftplus.model.entity.base import Base


class Military(Base):
    __tablename__ = "military_tbl"


    _id = Column(Integer, primary_key=True , autoincrement=True)
    _serial = Column("serial", Integer(30))
    _date = Column("date", Integer(20))
    _location = Column("location", Integer(20))
    _organization = Column("organization", Integer(30))
    _status = Column("status", Integer(20))
    _deleted = Column("deleted", default=False)

    def __init__(self,serial , date , location , organization , status , deleted):
        self._id = None
        self._serial = serial
        self._date = date
        self._location = location
        self._organization = organization
        self._status  = status
        self._deleted = deleted

    # getter / setter

    #serial  date  location organization status deleted