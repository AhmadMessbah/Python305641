
from sqlalchemy import Column, Integer, Boolean, String
from mftplus.model.entity.base import *

class Skill(Base):
    __tablename__ = "skill_tbl"
    _id = Column(Integer, primary_key=True)
    _group= Column(String)
    _title = Column(String)
    _description = Column(String)
    _license= Column(String)
    _deleted = Column(Boolean,default=False)

    def __init__(self, group, title, description, license):
        self._id= None
        self.group= group
        self.title= title
        self.description= description
        self.license= license
        self.deleted= False



    def get_id(self):
        return self._id

    def set_id(self, _id):
        self._id = _id



    def get_title(self):
        return self._title

    def set_title(self, _title):
        self._title = _title



    def get_description(self):
        return self._description

    def set_description(self, _description):
        self._description = _description



    def get_license(self):
        return self._license

    def set_license(self, _license):
        self._license = _license



    def get_deleted(self):
        return self._deleted
    def set_deleted(self, _deleted):
        self._deleted = _deleted


    id= property(get_id, set_id)
    group= property(get_title, set_title)
    title= property(get_title, set_title)
    description= property(get_description, set_description)
    license= property(get_license, set_license)
    deleted= property(get_deleted, set_deleted)


