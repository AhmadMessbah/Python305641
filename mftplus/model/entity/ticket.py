from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
#from mftplus.model.tools.validator import TicketValidator
from mftplus.model.entity.base import Base
from datetime import datetime
import re


class Ticket(Base):
    __tablename__ = "ticket_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _group = Column("group", String(20), nullable=False)
    _title = Column("title", String(20), nullable=False)
    _text = Column("text", String(100), nullable=False)
    sender_id = Column("sender_id", Integer, ForeignKey("person_tbl.id"))
    _date_time = Column("date_time", DateTime, nullable=False)
    _status = Column("status", Boolean, default=True)
    _deleted = Column("deleted", Boolean, default=False)

    sender = relationship("Person")

    def __init__(self, group, title, text, sender, date_time, status=True, deleted=False):
        self.id = None
        self.group = group
        self.title = title
        self.text = text
        self.sender_id = sender.id
        self.date_time = date_time
        self.status = status
        self.deleted = deleted
        self.owner = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, group):
        self._group = TicketValidator.name_validator(group, "Invalid Group")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = TicketValidator.name_validator(title, "Invalid Title")

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = TicketValidator.text_validator(text, "Invalid Text")

    @property
    def date_time(self):
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        self._date_time = TicketValidator.date_time_validator(date_time, "Invalid Date")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if isinstance(status, bool):
            self._status = status
        else:
            raise ValueError("Invalid Status")

    @property
    def deleted(self):
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        if isinstance(deleted, bool):
            self._deleted = deleted
        else:
            raise ValueError("Invalid deleted")


class TicketValidator:
    @classmethod
    def name_validator(cls, name, message):
        if isinstance(name, str) and re.match(r'^[a-zA-Z\s]{3,20}$', name):
            return name
        else:
            raise ValueError(message)

    @classmethod
    def text_validator(cls, text, message):
        if isinstance(text, str) and re.match(r'^.{1,100}$', text):
            return text
        else:
            raise ValueError(message)

    @classmethod
    def date_time_validator(cls, date, message):
        if isinstance(date, datetime):
            return date
        else:
            raise ValueError(message)
