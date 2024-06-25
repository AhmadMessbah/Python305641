from mftplus.model.da.da import DataAccess


class DriveLicenseService:
    @staticmethod
    def save(drive_license):
        d_l_da = DataAccess(drive_license)
        d_l_da.save(drive_license)


    # todo : find by start_date_time,expire_date_time,license_type,serial