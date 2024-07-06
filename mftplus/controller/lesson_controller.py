from mftplus.model.entity.lesson import Lesson
from mftplus.model.service.lesson_service import LessonService
from mftplus.model.tools.decorators import exception_handling
from mftplus.model.tools.logger import Logger

class LessonController:
    @classmethod
    @exception_handling
    def save(cls, lesson_group, department, title, code, teacher):
        lesson = Lesson(lesson_group, department, title, code, teacher)
        LessonService.save(lesson)
        return True, lesson

    @staticmethod
    @exception_handling
    def edit(id, lesson_group, department, title, code, teacher, status):
        lesson = Lesson(lesson_group, department, title, code, teacher, status)
        lesson.id = id
        LessonService.edit(lesson)
        return True, lesson


    @staticmethod
    def remove(id):
        lesson = LessonService.remove(id)
        Logger.info(f"lesson Removed - {lesson}")
        return True, lesson


    @staticmethod
    @exception_handling
    def find_all():
        lesson_list = LessonService.find_all()
        Logger.info(f"Lesson FindAll()")
        return True, lesson_list
    @staticmethod
    @exception_handling
    def find_by_id(id):
        lesson = LessonService.find_by_id(id)
        Logger.info(f"Lesson Find By Id({id})")
        return True, lesson


    @staticmethod
    @exception_handling
    def find_by_teacher(teacher):
        lesson = LessonService.find_by_teacher(teacher)
        Logger.info(f"Lesson Find By Teacher({teacher})")
        return True, lesson


    @staticmethod
    @exception_handling
    def find_by_lesson_group(lesson_group):
        lesson = LessonService.find_by_lesson_group(lesson_group)
        Logger.info(f"Lesson Find By Lesson Group({lesson_group})")
        return True, lesson

    @staticmethod
    @exception_handling
    def find_by_code(code):
        lesson = LessonService.find_by_code(code)
        return True, lesson

    @staticmethod
    @exception_handling
    def find_by_title(title):
            lesson = LessonService.find_by_title(title)
            Logger.info(f"Lesson Find By Title({title})")
            return True, lesson


    @staticmethod
    @exception_handling
    def find_by_department(department):
        lesson = LessonService.find_by_department(department)
        Logger.info(f"Lesson Find By Department({department})")
        return True, lesson

