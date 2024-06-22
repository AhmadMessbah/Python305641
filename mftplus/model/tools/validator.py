import re

def name_validator(name, message):
    if isinstance(name, str) and re.match(r"^[a-zA-Z\s]{2,30}$", name):
        return name
    else:
        raise ValueError(message)


def national_id_validator(national_id, message):
    if isinstance(national_id, str) and re.match(r"^\d{10}$", national_id):
        return national_id
    else:
        raise ValueError(message)


def positive_int_validator(int_value, message):
    if isinstance(int_value, int) and int_value >= 0:
        return int_value
    else:
        raise ValueError(message)


def boolean_validator(bool_value, message):
    if isinstance(bool_value, bool):
        return bool_value
    else:
        raise ValueError(message)


def date_validator(date_value, message):
    if isinstance(date_value, date):
        return date_value
    else:
        raise ValueError(message)


def date_time_validator(date_time_value, message):
    if isinstance(date_time_value, datetime):
        return date_time_value
    else:
        raise ValueError(message)




def car_name_validator(name):
    ...

def car_model_validator(model):
    ...

def bank_validator(bank):
    return re.match("^[A-Za-z]{10}$", bank)


from datetime import datetime, date


def military_serial_validator(serial):
    if isinstance(serial, int):
        return serial
    else:
        raise ValueError("Invalid serial number")


def military_date_validator(date):
    if isinstance(date, int):
        return date
    else:
        raise ValueError("Invalid date")


def military_location_validator(location):
    if isinstance(location, str) and re.match(r"^[0-9]+$", location):
        return location
    else:
        raise ValueError("Invalid location")


def military_organization_validator(organization):
    if isinstance(organization, str) and re.match(r"^[0-9]+$", organization):
        return organization
    else:
        raise ValueError("Invalid organization")


def military_status_validator(self, status):
    if isinstance(status, bool):
        self._status = status
    else:
        raise ValueError("Invalid status")

def code_validator(self, code):
    if isinstance(code, int) and re.match(r"^[0-9]$", code):
        return code
    else:
        raise ValueError("Invalid code")