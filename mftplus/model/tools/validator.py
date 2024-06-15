import re

def car_id_validator(id):
    return re.match("r^[\d]{2,30}$", id)


def car_name_validator(name):
    return isinstance(name, str) and bool(re.match(r"^[a-zA-Z\s]{2,30}$", name))


def car_model_validator(model):
    return isinstance(model, str) and bool(re.match(r"^[a-zA-Z\d\s]{2,30}$", model))


def car_man_date_validator(man_date):
    return isinstance(man_date, int) and re.match(r"^\d{4}/\d{2}/\d{2}$", man_date)




