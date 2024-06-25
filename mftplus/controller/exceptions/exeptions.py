class PersonNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Person Not Found !!!")


class JobNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Job Not Found !!!")


class LetterNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("letter Not Found !!!")

class LessonNotFoundError(Exception):
    def __init__(self,*args):
        super().__init__("lesson Not Found !!!")