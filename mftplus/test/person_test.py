from datetime import date

from mftplus.controller.person_controller import PersonController
from mftplus.model.service.person_service import PersonService
from mftplus.model.da.da import DataAccess
from mftplus.model.entity.person import Person
from mftplus.model.entity.sim_card import SimCard
from mftplus.model.tools.logger import Logger
from mftplus.model.tools.validator import Validator

PersonController.save("ahmad", "messbah")
# مدیریت خطا
    #{
    # اعتبار سنجی
    # شی person ساخته می شود
    # فراخوانی سرویس
        # {
        # چک کردن قواعد تجاری
            # فراخوانی Data Access
                # ذخیره/ویرایش/حذف/جستجو
            # جواب
        # جواب
        # }
    # }
# نمایش پاسخ به کاربر
# Log





# sim_card = SimCard("0123456","MCI")
# sim_da = DataAccess(SimCard)
# sim_da.save(sim_card)
# print(sim_card)



# # person.sim_card = sim_card
# person_da = DataAccess(Person)
# person_da.save(person)
# PersonService.save(person)
# print(person)


# Validator.name_validator("ali1", "Invalid")

