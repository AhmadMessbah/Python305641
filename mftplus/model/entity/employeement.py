from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from mftplus.model.entity.base import Base

class Employeement(Base):
    __tablename__ = "employeement_tbl"
    _id = Column("id",Integer, primery_key=True,autoincrement=True)
    _name = Column("name",String(20),nullable=False)
    _family = Column("family",String(20),nullable=False)
    _insurance = Column("insurance",String(20),nullable=False)
    _pay_ment = Column("pay_ment",String(20),nullable=False)


    def __init__(self,name,family,insurance,pay_ment):
        self._id = None
        self._name = name
        self._family = family
        self._insurance = insurance
        self._pay_ment = pay_ment



    def get_id(self):
        return self._id
    def set_id(self,id):
        self._id = id

    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name

    def get_family(self):
        return self._family
    def set_family(self,family):
        self._family = family

    def get_insurance(self):
        return self._insurance
    def set_insurance(self, insurance):
        if isinstance(insurance,bool):
            self._insurance = insurance
        else:
            raise ValueError("Invalid Insurance information")

    def get_pay_ment(self):
        return self._pay_ment
    def set_pay_ment(self,pay_ment):
        if isinstance(pay_ment,int):
            self._pay_ment = pay_ment
        else:
            raise ValueError("invalid input paymentation")






    id = property(get_id,set_id)
    name = property(get_name,set_name)
    family = property(get_family,set_family)
    insurance = property(get_insurance,set_insurance)
    pay_ment = property(get_pay_ment,set_pay_ment)


pey_ment1 = Employee("Pey","<EMAIL>","ali",True,"a")