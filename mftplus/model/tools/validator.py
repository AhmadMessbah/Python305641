import re
# def car_name_validator(name):
#     ...


def military_serial_validator(serial):
    pass

def bank_validator(bank):
    return re.match("^[A-Za-z]{10}$", bank)

def title_validator(title):
    if re.match("^[A-Za-z]{10}$", title):
        return title
    else:
        return "Invalid title"