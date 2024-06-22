from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from mftplus.model.entity.base import Base

# todo : roksana : getter setter validator !!!

class SimCard(Base):
    __tablename__ = 'sim_card_tbl'

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _number = Column("number", String(12))
    _operator = Column("operator", String(12))

    owner_id = Column(Integer, ForeignKey("person_tbl.id") )
    owner = relationship("Person")

    def __init__(self, number, operator):
        self.id = None
        self.number = number
        self.operator = operator
