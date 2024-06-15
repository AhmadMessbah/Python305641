from mftplus.model.da.da import DataAccess
from mftplus.model.entity.driving_licences import DrivingLicence
from mftplus.model.entity.person import Person


drive_lice = DrivingLicence(1,"16541651", "b1", "1/2/2020", "1/2/2030", True, "das")
drive_lice_da = DataAccess("driving_licence_da")
print(drive_lice)
