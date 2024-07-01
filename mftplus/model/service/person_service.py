from mftplus.controller.exceptions.exeptions import PersonNotFoundError
from mftplus.model.da.da import DataAccess
from mftplus.model.entity.person import Person
from mftplus.model.tools.decorators import *


class PersonService:
    @classmethod
    def save(cls,person):
        person_da = DataAccess(Person)
        person_da.save(person)
        return person

    @classmethod
    def edit(cls,person):
        person_da = DataAccess(Person)
        if person_da.find_by_id(person.id):
            person_da.edit(person)
            return person
        else:
            raise PersonNotFoundError()

    @classmethod
    def remove(cls,id):
        person_da = DataAccess(Person)
        if person_da.find_by_id(id):
            return person_da.remove(id)
        else:
            raise PersonNotFoundError()

    @classmethod
    def find_all(cls,):
        person_da = DataAccess(Person)
        return person_da.find_all()

    @classmethod
    def find_by_id(cls,id):
        person_da = DataAccess(Person)
        return person_da.find_by_id(id)

    @classmethod
    def find_by_family(cls,family):
        person_da = DataAccess(Person)
        return person_da.find_by(Person.family == family)
