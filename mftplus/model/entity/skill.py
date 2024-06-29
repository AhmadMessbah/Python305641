from sqlalchemy import Column, Integer, Boolean, String
from mftplus.model.entity.base import *
import re


# todo : negar : validator
class Skill(Base):
    __tablename__ = "skill_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _group = Column("group", String(20))
    _title = Column("title", String(40))
    _description = Column("description", String(20))
    _license = Column("license", String(20))
    _deleted = Column("deleted", Boolean, default=False)

    def __init__(self, group, title, description, license, deleted=False):
        self.id = None
        self.group = group
        self.title = title
        self.description = description
        self.license = license
        self.deleted = False

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_license(self):
        return self._license

    def set_license(self, license):
        self._license = license

    def get_deleted(self):
        return self._deleted

    def set_deleted(self, deleted):
        self._deleted = deleted

    id = property(get_id, set_id)
    group = property(get_title, set_title)
    title = property(get_title, set_title)
    description = property(get_description, set_description)
    license = property(get_license, set_license)
    deleted = property(get_deleted, set_deleted)



def skill_group_validator(skill_group , message):
    if isinstance(skill_group, str) and re.match("^[A-Za-z]$", skill_group):
        return skill_group
    else:
        raise ValueError(message)
