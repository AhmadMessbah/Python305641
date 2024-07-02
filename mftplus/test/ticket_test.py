from mftplus.controller.ticket_controller import TicketController
from mftplus.controller.person_controller import PersonController
from datetime import datetime

status, person1 = PersonController.save("farbod", "orang")
now = datetime.today()
print(TicketController.save("group", "title", "This text is created solely for testing purposes.", person1, now))


print(TicketController.findAll())
print(TicketController.find_by_id(1))
print(TicketController.find_by_group("group"))
print(TicketController.find_by_title("title"))
print(TicketController.find_by_text_content("bar"))
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
print(TicketController.date_range(start_date, end_date))
