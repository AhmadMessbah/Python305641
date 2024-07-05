import re


def pattern_validator(pattern, message):
    def inner1(function_name):
        def inner2(self, text):
            if isinstance(text,str) and re.match(pattern, text):
                result = function_name(self, text)
            else:
                raise ValueError(message)
            return result
        return inner2
    return inner1


def date_validator(message):
    def inner1(function_name):
        def inner2(self, date_param):
            if isinstance(date_param, date):
                result = function_name(self, date_param)
            elif isinstance(date_param, str):
                date_param = date_param.replace('/', '-')
                try:
                    date_param = datetime.strptime(date_param, '%Y-%m-%d').date()
                    result = function_name(self, date_param)
                except:
                    raise ValueError(message)
            else:
                raise ValueError(message)
            return result
        return inner2
    return inner1


def date_time_validator(message):
    def inner1(function_name):
        def inner2(self, date_time_param):
            if isinstance(date_time_param, date):
                result = function_name(self, date_time_param)
            elif isinstance(date_time_param, str):
                date_time_param = date_time_param.replace('/', '-')
                try:
                    date_time_param = datetime.strptime(date_time_param, '%Y-%m-%d %H:%M:%S').date()
                    result = function_name(self, date_time_param)
                except:
                    raise ValueError(message)
            else:
                raise ValueError(message)
            return result
        return inner2
    return inner1


def boolean_validator(message):
    def inner1(function_name):
        def inner2(self, bool_param):
            if isinstance(bool_param, bool):
                result = function_name(self, bool_param)
            else:
                raise ValueError(message)
            return result

        return inner2

    return inner1


class Validator:
    @staticmethod
    def name_validator(name, message):
        if isinstance(name, str) and re.match(r"^[a-zA-Z\s]{2,30}$", name):
            return name
        else:
            raise ValueError(message)

    @staticmethod
    def national_id_validator(national_id, message):
        if isinstance(national_id, str) and re.match(r"^\d{10}$", national_id):
            return national_id
        else:
            raise ValueError(message)


# todo : class

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


def boolean_validator1(bool_value, message):
    if isinstance(bool_value, bool):
        return bool_value
    else:
        raise ValueError(message)


def date_validator1(date_value, message):
    if isinstance(date_value, date):
        return date_value
    else:
        raise ValueError(message)


def date_time_validator1(date_time_value, message):
    if isinstance(date_time_value, datetime):
        return date_time_value
    else:
        raise ValueError(message)


def car_name_validator(name, message):
    if isinstance(name, str) and re.match(r"^[a-zA-Z\s]{2,30}$", name):
        return name
    else:
        raise ValueError(message)


def car_model_validator(model, message):
    if isinstance(model, str) and re.match(r"^[a-zA-Z\s]{2,30}$", model):
        return model
    else:
        raise ValueError(message)


def man_date_validator(man_date, message):
    if isinstance(man_date, man_date):  # جلوی این man_date اول، چی باید بنویسم؟
        return man_date
    else:
        raise ValueError(message)


def bank_validator(bank):
    return re.match("^[A-Za-z]{10}$", bank)


from datetime import datetime, date


# military validator

def military_serial_validator(serial, message):
    if isinstance(serial, str) and re.match(r"^\s[0-9]{20}$", serial):
        return serial
    else:
        raise ValueError(message)


def military_location_validator(location, message):
    if isinstance(location, str) and re.match(r"^[0-9]{2,30}$", location):
        return location
    else:
        raise ValueError(message)


def military_organization_validator(organization, message):
    if isinstance(organization, str) and re.match(r"^[0-9]{2,30}$", organization):
        return organization
    else:
        raise ValueError(message)


def military_status_validator(status, message):
    if isinstance(status, bool):
        return status
    else:
        raise ValueError(message)


def code_validator(code, message):
    if isinstance(code, str) and re.match(r"^[0-9]{2,30}$", code):
        return code
    else:
        raise ValueError(message)


# medical_report
@classmethod
def disease_validator(cls,disease, message):
    if isinstance(disease, str) and re.match(r"^[a-zA-Z\s]{3,30}$", disease):
        return disease
    else:
        raise ValueError(message)


#def date_time_validator(date_time_value,message):
#    if isinstance(date_time_value,datetime):
#        return date_time_value
#    else:
#        raise ValueError(message)


# -----------------------
