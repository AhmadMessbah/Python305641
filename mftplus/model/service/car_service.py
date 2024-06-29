from mftplus.controller.exceptions.exeptions import CarNotFoundError
from mftplus.model.da.da import DataAccess
from mftplus.model.entity.car import Car


class CarService:
    @staticmethod
    def save(car):
        car_da = DataAccess(Car)
        car_da.save(car)
        return car

    @staticmethod
    def edit(car):
        car_da = DataAccess(Car)
        if car_da.find_by_id(car.id):
            car_da.edit(car)
            return car
        else:
            raise CarNotFoundError()

    @staticmethod
    def remove(id):
        car_da = DataAccess(Car)
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
    def find_by_name(name):
        car_da = DataAccess(Car)
        return car_da.find_by(Car.name == name)

    @staticmethod
    def find_by_model(model):
        car_da = DataAccess(Car)
        return car_da.find_by(Car.model == model)

    @staticmethod
    def find_by_man_date_range(man_date_range):
        car_da = DataAccess(Car)
        return car_da.find_by(Car.man_date_range == man_date_range)
