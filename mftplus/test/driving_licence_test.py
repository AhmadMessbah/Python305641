from mftplus.model.da.da import DataAccess
from mftplus.model.entity.driving_licence import DrivingLicense
from mftplus.model.entity.person import Person


drive_lice = DrivingLicense("16541651", "b1", "1/2/2020", "1/2/2030")
# drive_lice_da = DataAccess(DrivingLicense)
# drive_lice_da.save(drive_lice)
print(drive_lice)

#person = Person("bashir", "charkhab")
#person.da = DataAccess("person")
#person.da.save(person)
#print(person)