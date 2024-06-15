import re

def id_validator(id):
    return re.match(r"^[\d]{2,30}$", id)
def car_name_validator(name):
    return isinstance(name, str) and bool(re.match(r"^[a-zA-Z\s]{2,30}$", name))
def car_model_validator(model):
    return isinstance(model, str) and bool(re.match(r"^[a-zA-Z\s]{2,30}$", model))
def car_man_date_validator(man_date):
    return isinstance(man_date, int) and bool(re.match(r"^\d{4}/\d{2}/\d{2}$", man_date))



def military_serial_validator(serial):
    pass


def bank_validator(bank):
    return re.match("^[A-Za-z]{10}$", bank)


from datetime import datetime, date


#@classmethod
def military_serial_validator(serial):
    if isinstance(serial, int):
        return serial
    else:
        raise ValueError("Invalid serial number")


#@classmethod
def military_date_validator(date):
    if isinstance(date, int):
        return date
    else:
        raise ValueError("Invalid date")


#@classmethod
def military_location_validator(location):
    if isinstance(location, str) and re.match(r"^[0-9]+$", location):
        return location
    else:
        raise ValueError("Invalid location")


#@classmethod
def military_organization_validator(organization):
    if isinstance(organization, str) and re.match(r"^[0-9]+$", organization):
        return organization
    else:
        raise ValueError("Invalid organization")


#@classmethod
def military_status_validator(self, status):
    if isinstance(status, bool):
        self._status = status
    else:
        raise ValueError("Invalid status")
