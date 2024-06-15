from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from sqlalchemy.orm import relationship
from mftplus.model.entity.base import Base
from mftplus.model.tools.validator import *


class Letter(Base):
    __tablename__ = "letter_tbl"
    _id = Column('id', Integer, primary_key=True, autoincrement=True)
    _sender = Column("sender", String(20), nullable=False)
    _receiver = Column("receiver", String(20), nullable=False)
    _group = Column("group", String(20), nullable=False)
    _title = Column("title", String(20), nullable=False)
    _priority = Column("priority", String(20), nullable=False)
    _status = Column("status", Boolean, defult=True)
    _deleted = Column("deleted", Boolean, default=False)

    person_id= Column(Integer, ForeignKey("person_tbl.id"))
    person= relationship("Person")

    def __init__(self, sender, receiver, group, title, priority, status, deleted=False):
        self.id = None
        self.sender = sender
        self.receiver = receiver
        self.group = group
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

    # group
    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, group):
        self._group = group

    # titel
    @property
    def title(self):
        return self.title

    @title.setter
    def titel(self, title):
        self.title = title

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
