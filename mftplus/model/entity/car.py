from sqlalchemy import Column, Integer, String, Boolean
from mftplus.model.entity.base import Base


class Car(Base):
    __tablename__ = "car_table"
    _id = Column("id", Integer, primary_key = True, autoincrement = True)
    _name = Column("name", String(20), nullable = False)
    _model = Column("model", String(20), nullable = False)
    _man_date = Column("man date", Boolean, default = True)
    deleted = False

    def __init__(self, name, model, man_date, deleted = False):
        self._id = None
        self._name = name
        self._model = model
        self._man_date = man_date


    # getter / setter