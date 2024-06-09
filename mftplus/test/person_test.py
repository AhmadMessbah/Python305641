from mftplus.model.da.da import DataAccess
from mftplus.model.entity.person import Person
from mftplus.model.entity.sim_card import SimCard

# sim_card = SimCard("0123456","MCI")
# sim_da = DataAccess(SimCard)
# sim_da.save(sim_card)
# print(sim_card)

person = Person("ahmad","messbah")
# person.sim_card = sim_card
person_da = DataAccess(Person)
person_da.save(person)
print(person)
