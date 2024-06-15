
from sqlalchemy import Column, Intiger, String, Boolean

from mftplus.model.entity.base import Base
class FinancialDocument(Base):
    __tablename__ = 'financial_document_tbl'
    _id = Column("id", Intiger, primary_key=True, autoincrement=True)
    _amount = Column("amount", Intiger , default=0)
    _date_time = Column("datetime", String(20) , nullable=False, default=0)
    _data_type = Column("datatype", String(20), nullable=False, default="recive" or "pay")
    _deleted = Column("deleted", Boolean, default=False)


    def __init__(self, id, amount, date_time, doc_type):
        self.id = id
        self.amount = amount
        self.date_time = date_time
        self.data_type = data_type
        self.deleted = deleted





