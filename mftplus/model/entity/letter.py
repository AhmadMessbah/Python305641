import re

from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from sqlalchemy.orm import relationship
from mftplus.model.entity.base import Base
from mftplus.model.tools.validator import *

# todo : dornika : validator

class Letter(Base):
    __tablename__ = "letter_tbl"
    _id = Column('id', Integer, primary_key=True, autoincrement=True)
    _sender = Column("sender", String(20), nullable=False)
    _receiver = Column("receiver", String(20), nullable=False)
    _letter_group = Column("letter_group", String(20), nullable=False)
    _title = Column("title", String(20), nullable=False)
    _priority = Column("priority", String(20), nullable=False)
    _status = Column("status", Boolean, defult=True)
    _deleted = Column("deleted", Boolean, default=False)

    person_id= Column(Integer, ForeignKey("person_tbl.id"))
    person= relationship("Person")

    def __init__(self, sender, receiver, letter_group, title, priority, status, deleted=False):
        self.id = None
        self.sender = sender
        self.receiver = receiver
        self.letter_group = letter_group
        self.title = title
        self.priority = priority
        self.status = status
        self.deleted = deleted


    # sender
    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, sender):
        self._sender = sender

    # reciver
    @property
    def receiver(self):
        return self.receiver

    @receiver.setter
    def receiver(self, receiver):
        self.receiver = receiver

    # letter_group
    @property
    def letter_group(self):
        return self._letter_group

    @letter_group.setter
    def letter_group(self, letter_group):
        self._letter_group = letter_group

    # titel
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    # priarty
    @property
    def priority(self):
        return self.priority

    @priority.setter
    def priority(self, priority):
        self.priority = priority

    # status
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status


def sender_validator(self,sender):
    if isinstance(sender,str) and re.match(r"^[a-zA-Z]{2,20}&",sender):
        return sender
    else:
        raise ValueError("invalid sender")


def receiver_validator(self,receiver):
    if isinstance(receiver,str) and re.match(r"^[a-zA-Z]{2,20}&",receiver):
        return receiver
    else:
        raise ValueError("invalid receiver")


def letter_group_validator(self,letter_group):
    if isinstance(letter_group,str) and re.match(r"^[a-zA-Z]{2,20}&",letter_group):
        return letter_group
    else:
        raise ValueError("invalid letter group")


def title_validator(self,title):
    if isinstance(title,str) and re.match(r"^[a-zA-Z]{2,20}&",title):
        return title
    else:
        raise ValueError("invalid title")


def priority_validator(self,priority):
    if isinstance(priority,str) and re.match(r"^[a-zA-Z]{2,20}&",priority):
        return priority
    else:
        raise ValueError("invalid priority")
