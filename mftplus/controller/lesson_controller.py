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
    def edit(id, lesson_group, department, title, code, teacher, status):
        try:
            lesson = Lesson(lesson_group, department, title, code, teacher, status)
            lesson.id = id
            LessonService.edit(lesson)
            Logger.info(f"Lesson Edited - {lesson}")
            return True, lesson
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def remove(id):
        try:
            lesson = LessonService.remove(id)
            Logger.info(f"lesson Removed - {lesson}")
            return True, lesson
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_all():
        try:
            lesson_list = LessonService.find_all()
            Logger.info(f"Lesson FindAll()")
            return True, lesson_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_id(id):
        try:
            lesson = LessonService.find_by_id(id)
            Logger.info(f"Lesson Find By Id({id})")
            return True, lesson
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_teacher(teacher):
        try:
            lesson = LessonService.find_by_teacher(teacher)
            Logger.info(f"Lesson Find By Teacher({teacher})")
            return True, lesson
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_lesson_group(lesson_group):
        try:
            lesson = LessonService.find_by_lesson_group(lesson_group)
            Logger.info(f"Lesson Find By Lesson Group({lesson_group})")
            return True, lesson
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_code(code):
        try:
            lesson = LessonService.find_by_code(code)
            Logger.info(f"Lesson Find By Code({code})")
            return True, lesson
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_title(title):
        try:
            lesson = LessonService.find_by_title(title)
            Logger.info(f"Lesson Find By Title({title})")
            return True, lesson
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_department(department):
        try:
            lesson = LessonService.find_by_department(department)
            Logger.info(f"Lesson Find By Department({department})")
            return True, lesson
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"
