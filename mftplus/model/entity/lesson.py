from sqlalchemy import Column, Integer, String, Boolean

from mftplus.model.entity.base import Base


class Lesson(Base):
    __tablename__ = "lesson_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _group = Column("group", String(20), nullable=False)
    _department = Column("department", String(20), nullable=False)
    _title = Column("title", String(20), nullable=False)
    _code = Column("code", Integer, nullable=False)
    _teacher = Column("teacher", String(20), nullable=False)
    _status = Column("status", Boolean, nullable=False)
    _deleted = Column("deleted", Boolean, default=False)

    def __init__(self, group, department, title, code, teacher, status, deleted=False):
        self.id = id
        self.group = group
        self.department = department
        self.title = title
        self.code = code
        self.teacher = teacher
        self.status = status
        self.deleted = deleted
