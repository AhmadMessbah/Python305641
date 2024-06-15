from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from mftplus.model.entity.base import Base


class DrivingLicence(Base):
    __tablename__ = "driving_licence_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _serial = Column("serial", Integer, unique=True)
    _licence_type = Column("license_type", String(30))
    _start_date = Column("start_data_time", Integer)
    _expire_date = Column("expire_data_time", Integer)
    _status = Column("status", Integer)
    _deleted = Column("deleted", Boolean, default=False)

    def __init__(self, id, serial, license_type, start_data_time, expire_data_time, status, deleted):
        self._id = None
        self._serial = serial
        self._license_type = license_type
        self._start_data_time = start_data_time
        self._expire_data_time = expire_data_time
        self._status = status
        self._deleted = deleted

    owner_id = Column(Integer, ForeignKey("person_tbl.id"))
    owner = relationship("Person")

    # getter/setter

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def serial(self):
        return self._serial

    @serial.setter
    def serial(self, serial):
        self._serial = serial

    @property
    def licence_type(self):
        return self._license_type

    @licence_type.setter
    def licence_type(self, licence_type):
        self._license_type = licence_type

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        self._start_date = start_date

    @property
    def expire_date(self):
        return self._expire_data_time

    @expire_date.setter
    def expire_date(self, expire_date):
        self._expire_data_time = expire_date

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def deleted(self):
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        self._deleted = deleted
