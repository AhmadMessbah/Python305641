from mftplus.model.da.da import DataAccess
from mftplus.model.entity.driving_licence import DrivingLicense
from mftplus.model.service.drive_license_service import DriveLicenseService

# lice = DrivingLicense("164141651", "b2", "2020-10-10", "2030-10-10", True, False)
# DriveLicenseService.save(lice)
# print(DriveLicenseService.find_all())
# print(DriveLicenseService.find_by_id(7))
# DriveLicenseService.remove(7)
print(DriveLicenseService.find_by_serial(164141651))
# person = Person("bashir", "charkhab")
# person.da = DataAccess("person")
# person.da.save(person)
# print(person)
