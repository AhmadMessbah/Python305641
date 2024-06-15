from mftplus.model.da.da import DataAccess
from mftplus.model.entity.ticket import Ticket



tick1 = Ticket("group","title","description","sender","2024-06-15")
# person.sim_card = sim_card
ticket_da = DataAccess(Ticket)
ticket_da.save(Ticket)
print(tick1)
