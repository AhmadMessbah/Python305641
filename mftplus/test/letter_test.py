from mftplus.model.da.da import DataAccess
from mftplus.model.entity.letter import Letter
from mftplus.model.entity.person import Person

# letter = Letter('aaa','kkkk','kkkk','sss','kkkk',True,True)
#
# da = DataAccess(Letter)
#
# da.save(letter)
# print(letter)

person = Person("ggg","llll")
person_da = DataAccess(Person)
person_da.save(person)
print(person)

