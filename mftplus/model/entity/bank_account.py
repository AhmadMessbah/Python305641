from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from mftplus.model.entity.base import Base
from mftplus.model.tools.validator import *
class BankAccount(Base):
    __tablename__ = "bank_account_tbl"
    _id = Column("id",Integer, primary_key=True, autoincrement=True)
    _bank = Column("bank",String(30), nullable=False)
    _branch = Column("branch",String(30), nullable=False)
    _account_number = Column("account_number",Integer, nullable=False)
    _card_number = Column("card_number",Integer, nullable=False)
    _account_type = Column("account_type",String(20), nullable=False)
    _status = Column("status",Boolean, default=True)

    owner_id = Column("owner_id",Integer,ForeignKey("person_tbl.id"))
    owner = relationship("Person")

    def __init__(self,bank,branch,accunt_number,card_number,accunt_type,status):
        self.id = None
        self.bank = bank
        self.branch = branch
        self.account_number = accunt_number
        self.card_number = card_number
        self.account_type = accunt_type
        self.status = status

    def get_id(self):
        return self._id
    def set_id(self,id):
        self._id = id

    def get_bank(self):
        return self._bank

    def set_bank(self,bank):
        self._bank = bank_validator(bank,"Invalid Bank")

    def get_branch(self):
        return self._branch

    def set_branch(self, branch):
        self._branch = branch

    def get_account_number(self):
        return self._account_number

    def set_account_number(self, account_number):
        if isinstance("account_number",Integer):
            self._account_number = account_number
        else:
            raise ValueError("Invalid Account Number")

    def get_card_number(self):
        return self._card_number

    def set_card_number(self, card_number):
        if isinstance("card_number",Integer):
            self._card_number = card_number
        else:
            raise ValueError("Invalid Card Number")

    def get_account_type(self):
        return self._account_type

    def set_account_type(self, account_type):
        self._account_type = account_type

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    id = property(get_id,set_id)
    bank = property(get_bank,set_bank)
    branch = property(get_branch,set_branch)
    account_number = property(get_account_number,set_account_number)
    card_number = property(get_card_number,set_card_number)
    account_type = property(get_account_type,set_account_type)
    status = property(get_status,set_status)