from mftplus.controller.exceptions.exeptions import PersonNotFoundError
from mftplus.model.da.da import DataAccess
from mftplus.model.entity.person import Person


class PersonService:
    @staticmethod
    def save(person):
        person_da = DataAccess(Person)
        person_da.save(person)
        return person

    @staticmethod
    def edit(person):
        person_da = DataAccess(Person)
        if person_da.find_by_id(person.id):
            person_da.edit(person)
            return person
        else:
            raise PersonNotFoundError()

    @staticmethod
    def remove(id):
        person_da = DataAccess(Person)
        if person_da.find_by_id(id):
            return person_da.remove(id)
        else:
            raise PersonNotFoundError()

    @staticmethod
    def find_all():
        person_da = DataAccess(Person)
        return person_da.find_all()

    @staticmethod
    def find_by_id(id):
        person_da = DataAccess(Person)
        return person_da.find_by_id(id)

    @staticmethod
    def find_by_family(family):
        person_da = DataAccess(Person)
        return person_da.find_by(Person.family == family)
