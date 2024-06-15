import re
# def car_name_validator(name):
#     ...


def military_serial_validator(serial):
    pass

def bank_validator(bank):
    return re.match(r"^[A-Za-z]{10}$", bank)


def sender_validator(sender):
    return re.match(r"^[A-Za-z]{20}$", sender)


def receiver_validator(receiver):
    return re.match(r"^[A-Za-z]{20}$", receiver)


def group_validator(group):
    return re.match(r"^[A-Za-z]{20}$", group)


def title_validator(title):
    return re.match(r"^[A-Za-z]{20}$", title)

def priority_validator(priority):
    return re.match(r"^[A-Za-z]{20}$", priority)