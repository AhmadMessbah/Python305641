from mftplus.controller.exceptions.exeptions import MilitaryInfoNotFoundError
from mftplus.model.da.da import DataAccess
from mftplus.model.entity.military import Military
from mftplus.controller.exceptions.exeptions import MilitaryInfoNotFoundError




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
                raise MilitaryInfoNotFoundError()

        @staticmethod
        def remove(id):
            military_da = DataAccess(Military)
            if military_da.find_by_id(id):
                return military_da.remove(id)
            else:
                raise MilitaryInfoNotFoundError()

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
        def find_by_date(military_date):
            return MilitaryService.find_by_date_range(military_date,military_date)


        @staticmethod
        def find_by_date_range(start_date, end_date):
            military_da = DataAccess(Military)
            return military_da.find_by(Military.military_date.between(start_date, end_date))

