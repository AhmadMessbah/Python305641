from mftplus.model.entity.person import Person
from mftplus.model.service.person_service import PersonService
from mftplus.model.tools.decorators import exception_handling


class PersonController:
    @classmethod
    @exception_handling
    def save(cls, name, family):
        person = Person(name, family)
        return True, PersonService.save(person)

    @classmethod
    @exception_handling
    def edit(cls, id, name, family):
        person = Person(name, family)
        person.id = id
        return True, PersonService.edit(person)

    @classmethod
    @exception_handling
    def remove(cls, id):
        return True, PersonService.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls, ):
        return True, PersonService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, PersonService.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_family(cls, family):
        return True, PersonService.find_by_family(family)
