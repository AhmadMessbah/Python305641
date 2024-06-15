from mftplus.model.da.da import DataAccess
from mftplus.model.entity.person import Person
from mftplus.model.entity.car import Car

car = Car("1", "BMW", "i8", "1403/03/26")
car = DataAccess(Car)
car_da.save(car)
print(car)

person = Person("kiyana","shirzadi")
person.car = car
person_da = DataAccess(Person)
person_da.save(person)
print(person)

