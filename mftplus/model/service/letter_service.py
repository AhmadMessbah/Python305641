from mftplus.controller.exceptions.exeptions import LetterNotFoundError
from mftplus.model.da.da import DataAccess
from mftplus.model.entity.letter import Letter


class LetterService:
    @staticmethod
    def save(letter):
        letter_da = DataAccess(letter)
        letter_da.save(letter)


# todo: write find_by sender ,receiver, letter_group, title, priority