from mftplus.model.da.da import DataAccess
from mftplus.model.entity.person import Person

person = Person("ahmad","messbah")

person_da = DataAccess(Person)
person_da.save(person)

print(person)
