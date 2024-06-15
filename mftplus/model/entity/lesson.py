from sqlalchemy import Boolean, Integar , string
from tkinter import StringVar


class Lesson(Base):
    __tablename__ = "lesson_tbl"
    _id = Column("id",int,primary_key = True , autoincrement = True)
    _group = Column("group",StringVar(20),nullable = False)
    _department = Column("department",StringVar(20),nullable = False)
    _title = Column("title",StringVar(20),nullable = False)
    _code = Column("code",int,nullable = False)
    _teacher = Column("teacher",StringVar(20),nullable = False)
    _status = Column("status",Boolean,nullable = False)
    _deleted = Column("deleted",Boolean, default = False)

    def __init__(self,group,department,title,code,teacher,status,deleted=False):
        self.id = id
        self.group = group
        self.department=department
        self.title=title
        self.code=code
        self.teacher=teacher
        self.status= status
        self.deleted = deleted