#from mftplus.model.da.da import DataAccess
#from mftplus.model.entity.person import Person
#from mftplus.model.entity.car import Car
from mftplus.controller import car_controller
#car = Car("1", "BMW", "i8", "1403/03/26")
#car = DataAccess(Car)
#car_da.save(car)
#print(car)

#person = Person("kiyana","shirzadi")
#person.car = car
#person_da = DataAccess(Person)
#person_da.save(person)
#print(person)

from mftplus.controller.car_controller import CarController
from mftplus.controller.person_controller import PersonController
from datetime import datetime

person1 = PersonController.save("kiyana", "shirzadi")
now = datetime.now()
print(CarController.save("benz", "123sh", 1403/2/12))

print(CarController.find_all())
print(CarController.find_by_id(1))
print(CarController.find_by_name("benz"))
print(CarController.find_by_model("123sh"))
print(CarController.man_date_range(1403/2/12, 1403/4/9))


