from mftplus.model.entity.person import Person
from mftplus.model.service.person_service import PersonService
from mftplus.model.tools.logger import Logger


class PersonController:
    @staticmethod
    def save(name, family):
        try:
            person = Person("ahmad", "messbah")
            PersonService.save(person)
            Logger.info(f"Person Saved - {person}")
            return True, person
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def edit(id, name, family):
        try:
            person = Person("ahmad", "messbah")
            person.id = id
            PersonService.edit(person)
            Logger.info(f"Person Edited - {person}")
            return True,person
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"


    @staticmethod
    def remove(id):
        try:
            person = PersonService.remove(id)
            Logger.info(f"Person Removed - {person}")
            return True,person
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def findAll():
        try:
            person_list = PersonService.find_all()
            Logger.info(f"Person FindAll()")
            return True,person_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"


    @staticmethod
    def find_by_id(id):
        try:
            person =  PersonService.find_by_id(id)
            Logger.info(f"Person FindById({id})")
            return True,person
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_family(family):
        try:
            person_list = PersonService.find_by_family(family)
            Logger.info(f"Person FindByFamily({family})")
            return True, person_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"