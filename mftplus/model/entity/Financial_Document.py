
from sqlalchemy import Column, Intiger, String, Boolean

from mftplus.model.entity.base import Base
class FinancialDocument(Base):
    __tablename__ = 'financial_document_tbl'
    _id = Column("id", Intiger, primary_key=True, autoincrement=True)
    _amount = Column("amount", Intiger , default=0)
    _date_time = Column("datetime", String(20) , nullable=False, default=0)
    _doc_type = Column("datatype", String(20), nullable=False, default="recive" or "pay")
    _deleted = Column("deleted", Boolean, default=False)


    def __init__(self, id, amount, date_time, doc_type):
        self.id = id
        self.amount = amount
        self.date_time = date_time
        self._doc_type = doc_type
        self.deleted = deleted

 def get_id(self):
        return self._id
    def set_id(self,id):
        self._id = id

    def get_amount(self):
        return self._amount

    def set_amount(self,amount):
        self._amount = amount_validator

    def data_time(self):
        return self._data_time

    def doc_type (self, doc_type):
        self._doc_type = doc_type



    id = property(get_id,set_id)
    amount = property(get_amount,set_amount)
    data_time = property(get_data_time,set_data_time)
    doc_type = property(get_doc_type,set_doc_type)







