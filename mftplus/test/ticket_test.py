from mftplus.model.da.da import DataAccess
from mftplus.model.entity.ticket import Ticket
from mftplus.model.entity.person import Person

from datetime import datetime

now = datetime.today()
pers1 = Person("farbod", "owrang")
da = DataAccess(Person)
da.save(pers1)

tick1 = Ticket(pers1.id, "group", "title", "description", "sender", date_time=now)
print(tick1)

ticket_da = DataAccess(Ticket)
ticket_da.save(tick1)
