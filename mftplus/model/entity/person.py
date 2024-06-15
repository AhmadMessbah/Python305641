from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from mftplus.model.entity.base import Base


class Person(Base):
    __tablename__ = "person_tbl"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(20), nullable=False)
    family = Column("family", String(20), nullable=False)
    status = Column("status", Boolean, default=True)

    def __init__(self, name, family, status=True):
        self._id = None
        self._name = name
        self._family = family
        self._status = status

    # getter / setter
