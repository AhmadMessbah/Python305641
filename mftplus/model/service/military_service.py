from mftplus.controller.exceptions.exeptions import militaryNotFoundError
from mftplus.model.da.da import DataAccess
from mftplus.model.entity.military import Military
from mftplus.controller.exceptions.exeptions import militaryNotFoundError




class MilitaryService:
        @staticmethod
        def save(military):
            military_da = DataAccess(military)
            military_da.save(military)
            return military

        @staticmethod
        def edit(military):
            military_da = DataAccess(Military)
            if military_da.find_by_id(military.id):
                military_da.edit(military)
                return military
            else:
                raise militaryNotFoundError()

        @staticmethod
        def remove(id):
            military_da = DataAccess(Military)
            if military_da.find_by_id(id):
                return military_da.remove(id)
            else:
                raise militaryNotFoundError()

        @staticmethod
        def find_all():
            military_da = DataAccess(Military)
            return military_da.find_all()

        @staticmethod
        def find_by_id(id):
            military_da = DataAccess(Military)
            return military_da.find_by_id(id)

        @staticmethod
        def find_by_serial(serial):
            military_da = DataAccess(Military)
            return military_da.find_by(Military.serial == serial)

        @staticmethod
        def find_by_organization(organization):
            military_da = DataAccess(Military)
            return military_da.find_by(Military.organization == organization)

        @staticmethod
        def find_by_date_range(date_range):
            military_da = DataAccess(Military)
            return military_da.find_by(military_da.start_date <= date_range <= military_da.end_date)