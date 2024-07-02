from mftplus.model.entity.driving_licence import DrivingLicense
from mftplus.model.service.drive_license_service import DriveLicenseService
from mftplus.model.tools.logger import Logger


class DrivingLicenseController:
    @staticmethod
    def save(drive_license):
        try:
            DriveLicenseService.save(drive_license)
            Logger.info(f"Driving License Saved - {drive_license}")
            return True, drive_license
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def edit(drive_license):
        try:
            if DriveLicenseService.find_by_id(drive_license.id):
                DriveLicenseService.edit(drive_license)
                Logger.info(f"drive license Edited - {drive_license}")
                return drive_license
            else:
                pass
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def remove(id):
        try:
            drive_license = DriveLicenseService.remove(id)
            Logger.info(f"drive license Removed - {drive_license}")
            return True, drive_license

        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_all():
        try:
            drive_license_list = DriveLicenseService.find_all()
            Logger.info(f"drive license FindAll()")
            return True, drive_license_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_id(id):
        try:
            drive_license = DriveLicenseService.find_by_id(id)
            Logger.info(f"Drive license FindById({id})")
            return True, drive_license
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_start_date_time(start_date_time):
        try:
            return DriveLicenseService.find_by_start_date_time(start_date_time)
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_expire_date_time(expire_date_time):
        try:
            return DriveLicenseService.find_by_expire_date_time(expire_date_time)
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_license_type(license_type):
        try:
            return DriveLicenseService.find_by_license_type(license_type)
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_serial(serial):
        try:
            return DriveLicenseService.find_by_serial(serial)
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"
