from mftplus.controller.exceptions.exeptions import DrivingLicenseReportNotFoundError
from mftplus.model.da.da import DataAccess
from mftplus.model.entity.driving_licence import DrivingLicense


class DriveLicenseService:
    @staticmethod
    def save(drive_license):
        drive_lice_da = DataAccess(DrivingLicense)
        drive_lice_da.save(drive_license)

    @staticmethod
    def edit(drive_license):
        drive_lice_da = DataAccess(DrivingLicense)
        if drive_lice_da.find_by_id(drive_license.id):
            drive_lice_da.edit(drive_license)
            return drive_license
        else:
            raise DrivingLicenseReportNotFoundError

    @staticmethod
    def remove(id):
        drive_lice_da = DataAccess(DrivingLicense)
        if drive_lice_da.find_by_id(id):
            return drive_lice_da.remove(id)
        else:
            raise DrivingLicenseReportNotFoundError

    @staticmethod
    def find_all():
        drive_lice_da = DataAccess(DrivingLicense)
        return drive_lice_da.find_all()

    @staticmethod
    def find_by_id(id):
        drive_lice_da = DataAccess(DrivingLicense)
        return drive_lice_da.find_by_id(id)

    @staticmethod
    def find_by_start_date_time(start_date_time):
        drive_lice_da = DataAccess(DrivingLicense)
        return drive_lice_da.find_by_start_date_time(start_date_time)

    @staticmethod
    def find_by_expire_date_time(expire_date_time):
        drive_lice_da = DataAccess(DrivingLicense)
        return drive_lice_da.find_by_expire_date_time(expire_date_time)

    @staticmethod
    def find_by_license_type(license_type):
        drive_lice_da = DataAccess(DrivingLicense)
        return drive_lice_da.find_by_license_type(license_type)

    @staticmethod
    def find_by_serial(serial):
        drive_lice_da = DataAccess(DrivingLicense)
        return drive_lice_da.find_by_serial(serial)

    # todo : find by start_date_time,expire_date_time,license_type,serial
