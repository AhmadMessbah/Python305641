from sqlalchemy import Column, Integer, String, Boolean

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

    # getter/setter
