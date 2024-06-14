from sqlalchemy import Column, Intiger, String, Boolean

from mftplus.model.entity.base import Base


class Letter(Base):
    __tablename__ = "letter_tbl"
    _id=Column('id',Intiger,primary_key=True,autoincrement=True)
    _sender=Column("sender",String(20),nullable=False)
    _reciver=Column("reciver",String(20),nullable=False)
    _group=Column("group",String(20),nullable=False)
    _title=Column("title",String(20),nullable=False)
    _priarty=Column("priarty",String(20),nullable=False)
    _status=Column("status",Boolean,defult=True)
    _deleted=Column("deleted",Boolean,default=False)

    def __init__(self,sender,reciver,group,titel,priarty,status,deleted=False):
        self.id=None
        self.sender=sender
        self.reciver=reciver
        self.group=group
        self.title=titel
        self.priarty=priarty
        self.status=status
        self,deleted=deleted

    def __repr__(self):
        return f"{self.__dict__}"
#sender
    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self,sender):
        self._sender=sender

#reciver
    @property
    def reciver(self):
        return self._reciver
    @reciver.setter
    def reciver(self,reciver):
        self._reciver=reciver

#group
    @property
    def group(self):
        return self._group
    @group.setter
    def group(self,group):
        self._group=group

#titel
    @property
    def titel(self):
        return self._titel
    @titel.setter
    def titel(self,titel):
        self._titel=titel

#priarty
    @property
    def priarty(self):
        return self._priarty
    @priarty.setter
    def priarty(self,priarty):
        self._priarty=priarty

#status
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self,status):
        self._status=status





