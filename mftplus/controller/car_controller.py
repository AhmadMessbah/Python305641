from mftplus.model.entity.car import Car
from mftplus.model.service.car_service import CarService
from mftplus.model.tools.logger import Logger


class CarController:
    @staticmethod
    def save(name, model, man_date):
        try:
            car = Car("benz", "123sh")
            CarService.save(car)
            Logger.info(f"Car Saved - {car}")
            return True, car
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def edit(id, name, model, man_date):
        try:
            car = Car("benz", "123sh")
            car.id = id
            CarService.edit(car)
            Logger.info(f"Car Edited - {car}")
            return True, car
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"


    @staticmethod
    def remove(id):
        try:
            car = CarService.remove(id)
            Logger.info(f"Car Removed - {car}")
            return True, car
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def findAll():
        try:
            car_list = CarService.find_all()
            Logger.info(f"Car FindAll()")
            return True, car_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_id(id):
        try:
            car = CarService.find_by_id(id)
            Logger.info(f"Car FindById({id})")
            return True, car
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_name(name):
        try:
            car =  CarService.find_by_name(name)
            Logger.info(f"Car FindByName({name})")
            return True, car
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_model(model):
        try:
            car_list = CarService.find_by_model(model)
            Logger.info(f"Car FindByModel({model})")
            return True, car_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def man_date_range(start_date, end_date):
        try:
            car = CarService.man_date_range(start_date, end_date)
            Logger.info(f"Car FindByMan_Date_Range({start_date}-{end_date})")
            return True, car
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"