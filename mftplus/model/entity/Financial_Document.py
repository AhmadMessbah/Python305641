from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from mftplus.model.tools.validator import *
from mftplus.model.entity.base import Base
from datetime import datetime

class FinancialDocument(Base):
    __tablename__ = 'financial_document_tbl'
    _id = Column("id", Integer, primary_key=True, auto_increment=True)
    _amount = Column("amount", Integer, default=0)
    _date_time = Column("date_time", DateTime, nullable=False)
    _doc_type = Column("doc_type", String(20), nullable=False)
    _deleted = Column("deleted", Boolean, default=False)

    def __init__(self, id, amount, date_time, doc_type, deleted=False):
        self._id = id
        self._amount = amount
        self._date_time = date_time
        self._doc_type = doc_type
        self._deleted = deleted

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_amount(self):
        return self._amount

    def set_amount(self, amount):
        self._amount = amount

    @date_time.setter
    def get_data_time(self,date_time):
       if isinstance(date_time, datetime):
            self._data_time
       else:
            raise ValueError("Invalid DataTime")

    def set_doc_type(self, doc_type):
        self._doc_type = doc_type

    id = property(get_id, set_id)
    amount = property(get_amount, set_amount)
    date_time = property(get_data_time, set_data_time)
    doc_type = property(get_doc_type, set_doc_type)
