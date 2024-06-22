from mftplus.model.da.da import DataAccess
from mftplus.model.entity.skill import Skill

skill = Skill("b", "listening", "most important", "a")
skill_da = DataAccess(Skill)
skill_da.save(skill)
print(skill)
