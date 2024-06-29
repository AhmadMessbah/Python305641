# from mftplus.controller.exceptions.exeptions import SkillNotFoundError
from mftplus.model.da.da import DataAccess
from mftplus.model.entity.skill import Skill
from mftplus.controller.exceptions.exeptions import SkillNotFoundError


class SkillService:

    # todo : find by group, title, description, license

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
    @staticmethod
    def find_by_group(group):
       skill_da = DataAccess(Skill)
       return skill_da.find_by_group(group)





    @staticmethod
    def find_by_title(title):
        skill_da = DataAccess(Skill)
        return skill_da.find_by_title(title)

    @staticmethod
    def find_by_description(description):
        skill_da = DataAccess(Skill)
        return skill_da.find_by_description(description)

    @staticmethod
    def  find_by_license(license):
        skill_da = DataAccess(Skill)
        return skill_da.find_by_license(license)










