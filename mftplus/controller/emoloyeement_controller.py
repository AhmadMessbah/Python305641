from mftplus.model.entity.employeement import Employeement
from mftplus.model.service.employeement_service import EmployeeService
from mftplus.model.tools.logger import Logger

class EmployeeController:
    @staticmethod
    def save(name):
        try:
            employee = (Employeement
                        ("aaaa","aaa",True,5))
            EmployeeService.save(employee)
            Logger.info(f"employee saved- {employee}")
            return True, employee
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def edit(id,name,family,insurance,peyment):
        try:
            empolyee = (Employeement
                        ("aaaa","aaaa",True,2))
            empolyee.id = id
            EmployeeService.edit(empolyee)
            Logger.info(f"employee edited - {empolyee}")
            return True,empolyee
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def remove(id):
        try:
            employee = EmployeeService.remove(id)
            Logger.info(f"Person removed - {employee}")
            return True, employee
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_Name(name):
        try:
            employee = EmployeeService.find_by_id(name)
            Logger.info(f"employee find by id - {name}")
            return True,employee
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_family(family):
        try:
            employee = EmployeeService.find_by_id(family)
            Logger.info(f"employee found by family - {family}")
            return True,employee
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"



