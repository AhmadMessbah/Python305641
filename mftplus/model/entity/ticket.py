from sqlalchemy import Column, Integer, String, Boolean

from mftplus.model.entity.base import Base


class Ticket(Base):
    __tablename__ = "ticket_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _group = Column("group", String(20), nullable=False)
    _family = Column("family", String(20), nullable=False)
    _status = Column("status", Boolean, default=True)

    def __init__(self, group, family, status=True):
        self.id = None
        self.group = group
        self.family = family
        self.status = status

    # getter / setter