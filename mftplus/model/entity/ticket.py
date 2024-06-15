from sqlalchemy import Column, Integer, String, Boolean, DateTime , ForeignKey 
from sqlalchemy.orm import relationship

from mftplus.model.entity.base import Base
from datetime import datetime

class Ticket(Base):
    __tablename__ = "ticket_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _group = Column("group", String(20), nullable=False)
    _title = Column("title", String(20), nullable=False)
    _text = Column("text", String(100), nullable=False)
    _sender = Column("sender", String(20), nullable=False)
    _date_time = Column("date_time", DateTime, nullable=False)
    _status = Column("status", Boolean, default=True)
    _deleted = Column("deleted", Boolean, default=False)


    owner_id = Column(Integer, ForeignKey("person_tbl.id") )
    owner = relationship("Person")
    
    def __init__(self, group, title, text, sender, date_time, status=True,deleted=False):
        self.id = None
        self.group = group
        self.title = title
        self.text = text
        self.sender = sender
        self.date_time = date_time
        self.status = status
        self.deleted = status
        self.owner_id = None

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
    def date_time(self):
        return self._date_time
    
    @date_time.setter
    def date_time(self,date_time):
        if isinstance(date_time, datetime):
            self._date_time = date_time
        else:
            raise ValueError("Invalid DateTime")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self,status):
        if isinstance(status, bool):
            self._status = status
        else:
            raise ValueError("Invalid Status")

    @property
    def deleted(self):
        return self._deleted

    @deleted.setter
    def deleted(self,deleted):
        if isinstance(deleted, bool):
            self._deleted = deleted
        else:
            raise ValueError("Invalid deleted")
