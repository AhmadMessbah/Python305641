from sqlalchemy import Column, Integer, String, Boolean
from mftplus.model.entity.base import Base
from mftplus.model.tools.validator import *


class Car(Base):
    __tablename__ = "car_tbl"
    _id = Column("id", Integer, primary_key = True, autoincrement = True)
    _name = Column("name", String(20), nullable = False)
    _model = Column("model", String(20), nullable = False)
    _man_date = Column("man date", Boolean, default = True)
    _deleted = Column("deleted", Boolean, default = False)

    def __init__(self, name, model, man_date, deleted = False):
        self._id = None
        self._name = name
        self._model = model
        self._man_date = man_date
        self._deleted = deleted


    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id


    def get_name(self):
        return self._name

    def set_name(self, name):
        if name_validator(name):
            self._name = name
        else:
            raise ValueError("Invalid Name")


    def get_model(self):
        return self._model

    def set_model(self, model):
        if model_validator(name_validator):
            self._model = model
        else:
            raise ValueError("Invalid Model")


    def get_man_date(self):
        return self._man_date

    def set_man_date(self, man_date):
        if man_date(man_date):
            self._man_date = man_date
        else:
            raise ValueError("Invalid man_date")


    id = property(get_id, set_id)
    name = property(get_name, set_name)
    model = property(get_model, set_model)
    man_date = property(get_man_date, set_man_date)