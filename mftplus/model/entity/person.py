from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from mftplus.model.entity.base import Base


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


    # getter / setter
