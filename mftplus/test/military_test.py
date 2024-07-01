from mftplus.controller.exceptions.military_controller import MilitaryController
from datetime import datetime

military = MilitaryController.save("1234", 2020 / 2 / 2, "tehran", "orgA")
now = datetime.today()
print(MilitaryController.save("1234", 2020 / 2 / 2, "tehran", "orgA"))

print(MilitaryController.findAll())
print(MilitaryController.find_by_id(1))

print(MilitaryController.find_by_serial("group"))
print(MilitaryController.find_by_location("title"))
print(MilitaryController.find_by_organization("bar"))
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
print(MilitaryController.date_range(start_date, end_date))
