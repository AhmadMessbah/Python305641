from datetime import datetime, date
import re


# todo : kiana
def car_name_validator(name):
    pass

# todo : kiana
def car_model_validator(model):
    pass


def bank_validator(bank):
    return re.match("^[A-Za-z]{10}$", bank)


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
