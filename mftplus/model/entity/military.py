from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from mftplus.model.tools.validator import *
from mftplus.model.entity.base import Base
from sqlalchemy.orm import relationship
import re


# todo : mohammad : validator

class Military(Base):
    __tablename__ = "military_tbl"
    _id = Column(Integer, primary_key=True, autoincrement=True)
    _serial = Column("serial", String(30))
    military_date= Column("military_date", Integer)
    _location = Column("location", String(20))
    _organization = Column("organization", String(30))
    _status = Column("status", Integer)
    _deleted = Column("deleted", Boolean, default=False)

    owner_id = Column(Integer, ForeignKey("person_tbl.id"))
    owner = relationship("Person")

    def __init__(self, serial, military_date, location, organization, status, deleted):
        self._id = None
        self._serial = serial
        self._military_date = military_date
        self._location = location
        self._organization = organization
        self._status = status
        self._deleted = deleted

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_serial(self):
        return self._serial

    def set_serial(self, serial):
        self._serial = military_serial_validator(serial, "invalid serial")

    def get_military_date(self):
        return self._military_date

    def set_military_date(self, date):
        self._military_date = date_validator(date, "invalid date")

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
    military_date = property(get_military_date, set_military_date)
    location = property(get_location, set_location)
    organization = property(get_organization, set_organization)
    status = property(get_status, set_status)
    deleted = property(get_deleted)
