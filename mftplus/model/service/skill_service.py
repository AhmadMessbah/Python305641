from mftplus.controller.exceptions.exeptions import SkillNotFoundError
from mftplus.model.da.da import DataAccess
from mftplus.model.entity.skill import Skill


class PersonService:
    @staticmethod
    def save(skill):
        person_da = DataAccess(Skill)
        person_da.save(skill)
        return skill

    @staticmethod
    def edit(skill):
        skill_da = DataAccess(Skill)
        if skill_da.find_by_id(skill.id):
            skill_da.edit(skill)
            return skill
        else:
            raise SkillNotFoundError()

    @staticmethod
    def remove(id):
        skill_da = DataAccess(Skill)
        if skill_da.find_by_id(id):
            return skill_da.remove(id)
        else:
            raise SkillNotFoundError()

    @staticmethod
    def find_all():
        skill_da = DataAccess(Skill)
        return skill_da.find_all()

    @staticmethod
    def find_by_id(id):
        skill_da = DataAccess(Skill)
        return skill_da.find_by_id(id)
