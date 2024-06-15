from sqlalchemy import Column, Integer, String, Boolean
from mftplus.model.tools.validator import *
from mftplus.model.entity.base import Base
import re


class Military(Base):
    __tablename__ = "military_tbl"
    _id = Column(Integer, primary_key=True , autoincrement=True)
    _serial = Column("serial", String(30))
    _date = Column("date", Integer)
    _location = Column("location", String(20))
    _organization = Column("organization", String(30))
    _status = Column("status", Integer)
    _deleted = Column("deleted", Boolean, default=False)

    def __init__(self, id , serial , date , location , organization , status , deleted):
        self._id = None
        self._serial = serial
        self._date = date
        self._location = location
        self._organization = organization
        self._status  = status
        self._deleted = deleted

    def get_serial(self):
        return self._serial

    def set_serial(self, serial):
        self._serial = military_serial_validator(serial, "invalid serial")


    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date_validator (date, "invalid date")

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location_validator(location, "invalid location")

    def get_organization(self):
        return self._organization

    def set_organization(self, organization):
        self._organization = organization_validator(organization, "invalid organization")

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status(status,"invalid status")