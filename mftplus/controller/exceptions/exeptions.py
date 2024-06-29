class PersonNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Person Not Found !!!")


class JobNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Job Not Found !!!")


class LetterNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Letter Not Found !!!")


class LessonNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Lesson Not Found !!!")


class TicketNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Ticket Not Found !!!")


class CarNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Car Not Found !!!")



class MedicalReportNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("MedicalReport Not Found !!!")

class SkillNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Skill Not Found !!!")


class emloyeeNotFoundError(Exception):
    def __init__(self,*args):
        super().__init__("emloyee not found ")

