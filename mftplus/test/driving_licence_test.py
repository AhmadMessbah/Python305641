from mftplus.model.da.da import DataAccess
from mftplus.model.entity.driving_licence import DrivingLicense
from mftplus.model.service.drive_license_service import DriveLicenseService

lice = DrivingLicense( "16541651", "b1", "1/2/2020", "1/2/2030", True, False)
DriveLicenseService.save()
print(lice)

# person = Person("bashir", "charkhab")
# person.da = DataAccess("person")
# person.da.save(person)
# print(person)
