from mftplus.controller.skill_controller import SkillController
from mftplus.controller.person_controller import PersonController

status, person1 = PersonController.save("gdfgd", "yytt")
print(SkillController.save("b", "listening", "most important", "a"))


print(SkillController.findAll())
print(SkillController.find_by_id(1))
print(SkillController.find_by_group("group"))
#print(SkillController.find_by_title("title"))

