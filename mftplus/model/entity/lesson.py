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

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_group(self):
        return self._group

    def set_group(self, group):
        self._group = group

    def get_department(self):
        return self._department

    def set_department(self, department):
        self._department = department

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_code(self):
        return self._code

    def set_code(self, code):
        self._code = code

    def get_teacher(self):
        return self._teacher

    def set_teacher(self, teacher):
        self._teacher = teacher

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    id = property(get_id, set_id)
    group = property(get_group, set_group)
    department = property(get_department, set_department)
    title = property(get_title, set_title)
    code = property(get_code, set_code)
    teacher = property(get_teacher, set_teacher)
    status = property(get_status, set_status)
