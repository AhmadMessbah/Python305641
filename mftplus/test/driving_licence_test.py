from mftplus.model.da.da import DataAccess
from mftplus.model.entity.driving_licence import DrivingLicense

lice = DrivingLicense("1", "16541651", "b1", "1/2/2020", "1/2/2030", True, False)
lice.id= 1
lice_da = DataAccess(DrivingLicense)
lice_da.save(lice )
print(lice)

# person = Person("bashir", "charkhab")
# person.da = DataAccess("person")
# person.da.save(person)
# print(person)
