from sqlalchemy import Column, Integer, String, Boolean

from mftplus.model.entity.base import Base


class Ticket(Base):
    __tablename__ = "ticket_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _group = Column("group", String(20), nullable=False)
    _title = Column("title", String(20), nullable=False)
    _text = Column("text", String(100), nullable=False)
    _sender = Column("sender", String(20), nullable=False)
    _datetime = Column("datetime", String(20), nullable=False)
    _status = Column("status", Boolean, default=True)

    def __init__(self, group, title, text, sender, datetime, status=True):
        self.id = None
        self.group = group
        self.title = title
        self.text = text
        self.sender = sender
        self.datetime = datetime
        self.status = status

    @property
    def group(self):
        return self._group
    
    @group.setter
    def group(self,group):

        self._group = group

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
        self._title = title

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self,text):
        self._text = text
        
    @property
    def datetime(self):
        return self._datetime
    
    @datetime.setter
    def datetime(self,datetime):
        self._datetime = datetime

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self,status):
        self._status = status
