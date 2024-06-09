from model.entity.car import Car
from sqlalchemy import create_engine
from sqlalchemy.utils import create_database, database_exists

connection_string = 'mysql+pymysql://root:root123@localhost:3306/car_db'

if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string, echo=True)

class CarDa:
    def __init__(self):
        self.session = None



    def save(self, car):
        self.session.add(car)
        self.session.commit()


    def edit(self, car):
        self.session.merge(car)
        self.session.commit()


    def remove(self, id):
        car = self.session.get(Car, id)
        self.session.delete(car)
        self.session.commit()


    def find_all(self):
        pass


    def find_by_id(self, id):
        return self.session.get(Car, id)
