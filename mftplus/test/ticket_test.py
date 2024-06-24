from mftplus.controller.ticket_controller import TicketController
from mftplus.controller.person_controller import PersonController
from datetime import datetime

status, person1 = PersonController.save("ahmad", "messbah")
now = datetime.today()
print(TicketController.save("group", "title", "text", person1, now))
