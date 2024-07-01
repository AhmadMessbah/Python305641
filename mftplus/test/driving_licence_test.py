from mftplus.model.entity.driving_licence import DrivingLicense
from mftplus.model.service.drive_license_service import DriveLicenseService

# lice = DrivingLicense("1654111651", "b1", "2020/01/01", "2030-10-10")
# DriveLicenseService.save(lice)
# DriveLicenseService.find_all()
# print(DriveLicenseService.find_all())
# print(lice)
print(DriveLicenseService.remove(1))
# print(DriveLicenseService.find_all())