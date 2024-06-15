from mftplus.model.da.da import DataAccess
from mftplus.model.entity.driving_licence import DrivingLicense
from mftplus.model.entity.person import Person


drive_lice = DrivingLicense(1,"16541651", "b1", "1/2/2020", "1/2/2030")
drive_lice_da = DataAccess("driving_licence_da")
print(drive_lice)
