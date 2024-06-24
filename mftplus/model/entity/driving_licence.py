import re
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship

from mftplus.model.entity.base import Base
from mftplus.model.tools.validator import date_time_validator


# todo : bashir charkhab : validator
class DrivingLicense(Base):
    __tablename__ = "driving_license_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _serial = Column("serial", Integer, unique=True)
    _license_type = Column("license_type", String(30))
    _start_date_time = Column("start_date_time", DateTime)
    _expire_date_time = Column("expire_date_time", DateTime)
    _status = Column("status", Integer)
    _deleted = Column("deleted", Boolean, default=False)

    owner_id = Column(Integer, ForeignKey("person_tbl.id"))
    owner = relationship("Person")

    def __init__(self, serial, license_type, start_date_time, expire_date_time, status=True, deleted=False):
        self._id = None
        self._serial = serial
        self._license_type = license_type
        self._start_date_time = start_date_time
        self._expire_date_time = expire_date_time
        self._status = status
        self._deleted = deleted
        self._owner = None

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
    def license_type(self):
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        self._license_type = license_type_validator(license_type, "invalid License!!")

    @property
    def start_date_time(self):
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        self._start_date_time = date_time_validator(start_date_time, "invalid time!!")

    @property
    def expire_date_time(self):
        return self._expire_date_time

    @expire_date_time.setter
    def expire_date_time(self, expire_date_time):
        self._expire_date_time = date_time_validator(expire_date_time, "invalid time!!")

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
        self._deleted = boolean_validator(deleted, "invalid data!!")


def boolean_validator(bool_value, message):
    if isinstance(bool_value, bool):
        return bool_value
    else:
        raise ValueError(message)


def date_time_validator(date_time_value, message):
    if isinstance(date_time_value, datetime):
        return date_time_value
    else:
        raise ValueError(message)


def license_type_validator(license_type, message):
    if isinstance(license_type, str) and license in ("b1" | "b2" | "b3"):
        return license_type
    else:
        raise ValueError(message)


def serial_validator(serial, message):
    if isinstance(serial, str) and re.match(r"^/d{10}", serial):
        return serial
    else:
        raise ValueError(message)
