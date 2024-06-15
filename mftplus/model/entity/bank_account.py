from sqlalchemy import Column, Integer, String, Boolean

from mftplus.model.entity.base import Base

class BankAccount(Base):
    __tablename__ = "bank_account_tbl"
    _id = Column("id",Integer, primary_key=True, autoincrement=True)
    _bank = Column("bank",String(30), nullable=False)
    _branch = Column("branch",String(30), nullable=False)
    _account_number = Column("account_number",Integer(10), nullable=False)
    _card_number = Column("card_number",Integer(16), nullable=False)
    _account_type = Column("account_type",String(20), nullable=False)
    _status = Column("status",Boolean, default=True)

    def __init__(self,id,bank,branch,accunt_number,card_number,accunt_type,status):
        self._id = None
        self._bank = bank
        self._branch = branch
        self._account_number = accunt_number
        self._card_number = card_number
        self._account_type = accunt_type
        self._status = status

