class PersonNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Person Not Found !!!")


class LetterNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("letter Not Found !!!")