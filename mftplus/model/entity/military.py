from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from mftplus.model.tools.validator import *
from mftplus.model.entity.base import Base
from sqlalchemy.orm import relationship
import re


# todo : mohammad : validator

class Military:
    __tablename__ = "military_tbl"
    _id = Column(Integer, primary_key=True, autoincrement=True)
    _serial = Column("serial", String(30))
    _date = Column("date", Integer)
    _location = Column("location", String(20))
    _organization = Column("organization", String(30))
    _status = Column("status", Integer)
    _deleted = Column("deleted", Boolean, default=False)

    owner_id = Column(Integer, ForeignKey("person_tbl.id"))
    owner = relationship("Person")

    def __init__(self, id, serial, date, location, organization, status, deleted):
        self._id = None
        self._serial = serial
        self._date = date
        self._location = location
        self._organization = organization
        self._status = status
        self._deleted = deleted

    def __repr__(self):
        return str(self.__dict__)

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_serial(self):
        return self._serial

    def set_serial(self, serial):
        self._serial = military_serial_validator(serial, "invalid serial")

    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date_validator(date, "invalid date")

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = military_location_validator(location, "invalid location")

    def get_organization(self):
        return self._organization

    def set_organization(self, organization):
        self._organization = military_organization_validator(organization, "invalid organization")

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = military_status_validator(status, "invalid status")

    def get_deleted(self):
        return self._deleted

    def set_deleted(self, deleted):
        self._deleted = deleted


    id = property(get_id, set_id)
    serial = property(get_serial, set_serial)
    date = property(get_date, set_date)
    location = property(get_location, set_location)
    organization = property(get_organization, set_organization)
    status = property(get_status, set_status)
    deleted = property(get_deleted)
