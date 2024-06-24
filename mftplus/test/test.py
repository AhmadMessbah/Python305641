from datetime import datetime

from mftplus.model.da.da import DataAccess
from mftplus.model.entity.bank_account import BankAccount
from mftplus.model.entity.car import Car
from mftplus.model.entity.driving_licence import DrivingLicense
from mftplus.model.entity.job import Job
from mftplus.model.entity.lesson import Lesson
from mftplus.model.entity.letter import Letter
from mftplus.model.entity.medical_report import MedicalReport
from mftplus.model.entity.military import Military
from mftplus.model.entity.person import Person
from mftplus.model.entity.skill import Skill

from sqlalchemy import create_engine, and_, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists
from mftplus.model.entity.base import Base
from mftplus.model.service.person_service import PersonService

connection_string = "mysql+pymysql://root:root123@localhost:3306/mft"
if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

person = session.get(Person, 1)
print(person)

d = datetime.now()
entity =Military(12345, d,"Tehran", "Police" ,False,False)
entity.person = person


session.add(entity)
session.commit()
session.refresh(entity)

print(entity)

