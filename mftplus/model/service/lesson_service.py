from mftplus.controller.exceptions.exeptions import LessonNotFoundError
from mftplus.model.da.da import DataAccess
from mftplus.model.entity.lesson import Lesson

class LessonService:
    @staticmethod
    def save(lesson):
        person_da = DataAccess(Lesson)
        person_da.save(lesson)
        return lesson

    @staticmethod
    def edit(lesson):
        lesson_da = DataAccess(lesson)
        if lesson_da.find_by_id(lesson.id):
            lesson_da.edit(lesson)
            return lesson
        else:
            raise LessonNotFoundError()

    @staticmethod
    def remove(id):
        lesson_da = DataAccess(Lesson)
        if lesson_da.find_by_id(id):
            return lesson_da.remove(id)
        else:
            raise LessonNotFoundError()

    @staticmethod
    def find_all():
        lesson_da = DataAccess(Lesson)
        return lesson_da.find_all()

    @staticmethod
    def find_by_id(id):
        lesson_da = DataAccess(Lesson)
        return lesson_da.find_by_id(id)

    # todo : group, department, title, code

    @staticmethod
    def find_by_lesson_group(lesson_group):
        lesson_da = DataAccess(Lesson)
        return lesson_da.find_by_lesson_group(lesson_group)
    @staticmethod
    def find_by_department(department):
        lesson_da = DataAccess(Lesson)
        return lesson_da.find_by_department

    @staticmethod
    def find_by_title(title):
        lesson_da = DataAccess(Lesson)
        return lesson_da.find_by(Lesson.title == title)
    def find_by_code(code):
        lesson_da = DataAccess(Lesson)
        return lesson_da.find_by_code