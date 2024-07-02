from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from mftplus.model.entity.base import Base
from mftplus.model.tools.validator import pattern_validator


class Person(Base):
    __tablename__ = "person_tbl"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(20))
    family = Column("family", String(20))
    status = Column("status", Boolean)

    def __init__(self, name, family, status=True):
        self.id = None
        self.name = name
        self.family = family
        self.status = status


    @property
    def name(self):
        return self._name

    @name.setter
    @pattern_validator(r"^[a-zA-Z\s]{2,30}$", "Invalid Name !!!")
    def name(self, name):
        self._name = name
