from mftplus.controller.exceptions.exeptions import emloyeeNotFoundError
from mftplus.model.da.da import DataAccess
from mftplus.model.entity.employeement import Employeement

class EmployeeService:
    @staticmethod
    def save(employee):
        employee_da = DataAccess(Employeement)
        employee_da.save(Employeement)
        return employee

    @staticmethod
    def edit(employee):
        employee_da = DataAccess(Employeement)
        if employee_da.find_by_id(employee.id):
            employee_da.edit(employee)
            return employee
        else:
            raise emloyeeNotFoundError()

    @staticmethod
    def remove(id):
        employee_da = DataAccess(Employeement)
        if employee_da.find_by_id(id):
            return employee_da.remove(id)
        else:
            raise emloyeeNotFoundError()

    @staticmethod
    def find_all():
        employee_da = DataAccess(Employeement)
        return employee_da.find_all()

    @staticmethod
    def find_by_id(id):
        employee_da = DataAccess(Employeement)
        return employee_da.find_by_id(id)

    @staticmethod
    def find_by_name(name):
        employee_da = DataAccess(Employeement)
        return employee_da.find_by(Employeement.name == name)



