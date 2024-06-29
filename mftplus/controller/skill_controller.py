from mftplus.model.entity.skill import Skill
from mftplus.model.service.skill_service import SkillService
from mftplus.model.tools.logger import Logger


class SkillController:
    @staticmethod
    def save(group,title,description,license):
        try:
            skill= Skill("a", "listening","grade 1","b")
            SkillService.save(skill)
            Logger.info(f"Skill Saved - {skill}")
            return True, skill
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def edit(id,group,title,description,license):
        try:
            skill = Skill("a", "writing","updated","a")
            skill.id = id
            SkillService.edit(skill)
            Logger.info(f"Skill Edited - {skill}")
            return True,skill
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"


    @staticmethod
    def remove(id):
        try:
            skill = SkillService.remove(id)
            Logger.info(f"Person Removed - {skill}")
            return True,skill
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def findAll():
        try:
            skill_list = SkillService.find_all()
            Logger.info(f"Skill FindAll()")
            return True,skill_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"


    @staticmethod
    def find_by_id(id):
        try:
            skill= SkillService.find_by_id(id)
            Logger.info(f"Skill FindById({id})")
            return True,Skill
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_group(group):
        try:
            group_list = SkillService.find_by_group(group)
            Logger.info(f"Skill FindByGroup({group})")
            return True, group_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"
