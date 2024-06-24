from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from mftplus.model.tools.validator import TicketValidator
from mftplus.model.entity.base import Base


class Ticket:
    print("ticket")
    __tablename__ = "ticket_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _group = Column("group", String(20), nullable=False)
    _title = Column("title", String(20), nullable=False)
    _text = Column("text", String(100), nullable=False)
    _sender = Column("sender", String(20), nullable=False)
    _date_time = Column("date_time", DateTime, nullable=False)
    _status = Column("status", Boolean, default=True)
    _deleted = Column("deleted", Boolean, default=False)

    owner_id = Column(Integer, ForeignKey("person_tbl.id"))

    def __init__(self, owner_id, group, title, text, sender, date_time, status=True, deleted=False, ):
        self.id = None
        self.group = group
        self.title = title
        self.text = text
        self.sender = sender
        self.date_time = date_time
        self.status = status
        self.deleted = deleted
        self.owner_id = owner_id



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
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, sender):
        self._sender = TicketValidator.name_validator(sender, "Invalid Sender")

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

