from sqlalchemy import Column, Integer, String, Boolean

from mftplus.model.entity.base import Base


class Person(Base):
    __tablename__ = "person_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(20), nullable=False)
    _family = Column("family", String(20), nullable=False)
    _status = Column("status", Boolean, default=True)

    def __init__(self, name, family, status=True):
        self.id = None
        self.name = name
        self.family = family
        self.status = status

    # getter / setter