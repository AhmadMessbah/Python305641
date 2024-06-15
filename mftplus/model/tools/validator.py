import re
# def car_name_validator(name):
#     ...


def military_serial_validator(serial):
    pass

def bank_validator(bank):
    return re.match(r"^[A-Za-z]{10}$", bank)
