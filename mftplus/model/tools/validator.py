import re
from datetime import datetime


# def car_name_validator(name):
#     ...


def military_serial_validator(serial):
    pass


def bank_validator(bank):
    return re.match("^[A-Za-z]{10}$", bank)

def title_validator(title):
    if isinstance(title, str) and re.match(r"^[A-Za-z]{10}$", title):
        return True
    else:
        raise ValueError("Invalid title")



class TicketValidator:
    @classmethod
    def name_validator(cls, name, message):
        if isinstance(name, str) and re.match(r'^[a-zA-Z\s]{3,20}$', name):
            return name
        else:
            raise ValueError(message)

    @classmethod
    def text_validator(cls, text, message):
        if isinstance(text, str) and re.match(r'^.{1,100}$', text):
            return text
        else:
            raise ValueError(message)

    @classmethod
    def date_time_validator(cls, date, message):
        if isinstance(date, datetime):
            return date
        else:
            raise ValueError(message)
