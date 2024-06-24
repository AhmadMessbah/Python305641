from mftplus.controller.exceptions.exeptions import CarNotFoundError
from mftplus.model.da.da import DataAccess
from mftplus.model.entity.car import Car


class CarService:
    @staticmethod
    def save(car):
        person_da = DataAccess(car)
        person_da.save(car)
        return car

    @staticmethod
    def edit(car):
        car_da = DataAccess(car)
        if person_da.find_by_id(car.id):
            person_da.edit(car)
            return car
        else:
            raise CarNotFoundError()

    @staticmethod
    def remove(id):
        car_da = DataAccess(car)
        if car_da.find_by_id(id):
            return car_da.remove(id)
        else:
            raise CarNotFoundError()

    @staticmethod
    def find_all():
        car_da = DataAccess(Car)
        return car_da.find_all()

    @staticmethod
    def find_by_id(id):
        car_da = DataAccess(Car)
        return car_da.find_by_id(id)

    @staticmethod
    def find_by_model(model):
        car_da = DataAccess(car)
        return car_da.find_by(Car.model == model)
