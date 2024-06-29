from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from mftplus.model.entity.base import Base
from mftplus.model.tools.validator import car_model_validator
from mftplus.model.tools.validator import car_name_validator
from mftplus.model.tools.validator import man_date_validator
from datetime import datetime
import re

# todo : kiana : validator
class Car(Base):
    __tablename__ = "car_tbl"
    _id = Column("id", Integer, primary_key = True, autoincrement = True)
    _name = Column("name", String(20), nullable = False)
    _model = Column("model", String(20), nullable = False)
    _man_date = Column("man_date", Boolean, default = True)
    _deleted = Column("deleted", Boolean, default = False)

    owner_id = Column(Integer, ForeignKey("person_tbl.id"))
    owner = relationship("Person")


    def __init__(self,  name, model, man_date, deleted = False):
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
        self._name = car_name_validator(name)


    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = car_model_validator(model)

    def get_man_date(self):
        return self._man_date

    def set_man_date(self, man_date):
        self._man_date = man_date_validator(man_date)


    id = property(get_id, set_id)
    name = property(get_name, set_name)
    model = property(get_model, set_model)
    man_date = property(get_man_date, set_man_date)
