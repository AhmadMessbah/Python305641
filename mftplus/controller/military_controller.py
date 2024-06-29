from mftplus.model.entity.military import Military
from mftplus.model.service.military_service import MilitaryService
from mftplus.model.tools.logger import Logger


class MilitaryController:
    @staticmethod
    def save(serial, military_date, location, organization, status):
        try:
            military = Military(serial, military_date, location, organization, status,)
            MilitaryService.save(military)
            Logger.info(f"military save -{military}")
            return True, military
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def edit(id, serial, military_date, location, organization, status, deleted):
        try:
            military = Military("123456", 20240201, "Tehran", "orgA", False)
            military.id = id
            MilitaryService.edit(military)
            Logger.info(f"military edit -{military}")
            return True, military
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def remove(id):
        try:
            military = MilitaryService.remove(id)
            Logger.info(f"Military remove -{military}")
            return True, military
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def findAll():
        try:
            military_list = MilitaryService.find_all()
            Logger.info(f"military FindAll()")
            return True, military_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_id(id):
        try:
            military = MilitaryService.find_by_id(id)
            Logger.info(f"militaryFindByid({id})")
            return True, military
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_serial(serial):
        try:
            military_list = MilitaryController.find_by_serial(serial)
            Logger.info(f"militaryFindBySerial({serial})")
            return True, military_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_location(location):
        try:
            military_list = MilitaryController.find_by_location(location)
            Logger.info(f"militaryFindByLocation({location})")
            return True, military_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_organization(organization):
        try:
            letter_list = MilitaryController.find_by_organization(organization)
            Logger.info(f"letterFindByOrganization({organization})")
            return True, letter_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"
