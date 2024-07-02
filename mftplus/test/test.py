from datetime import date, datetime
from mftplus.model.tools.validator import *

# def test(date_param):
#     if isinstance(date_param, date):
#         return date_param
#     elif isinstance(date_param, str):
#         date_param = date_param.replace('/', '-')
#         try:
#             date_param = datetime.strptime(date_param, '%Y-%m-%d').date()
#             return date_param
#         except :
#             raise ValueError("Invalid Date !!!")
#     else:
#         raise ValueError("Invalid Date !!!")


# birth_date = date(1990,12,25)
#
# @date_validator(message= "Invalid Date !!!")
# def test(self, d):
#     print(d)
#
# test("s", birth_date)