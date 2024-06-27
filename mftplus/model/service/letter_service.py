from mftplus.controller.exceptions.exeptions import LetterNotFoundError
from mftplus.model.da.da import DataAccess
from mftplus.model.entity.letter import Letter


class LetterService:
    @staticmethod
    def save(letter):
        letter_da = DataAccess(letter)
        letter_da.save(letter)

    @staticmethod
    def edit(letter):
        letter_da=DataAccess(letter)
        if letter_da.find_by_id(letter.id):
            letter_da.edit(letter)
            return letter
        else:
            raise LetterNotFoundError()

    @staticmethod
    def remove(id):
        letter_da = DataAccess(Letter)
        if letter_da.find_by_id(id):
            return letter_da.remove(id)
        else:
            raise LetterNotFoundError()

    @staticmethod
    def find_all():
        letter_da = DataAccess(Letter)
        return letter_da.find_all()

# todo: write find_by sender ,receiver, letter_group, title, priority

    @staticmethod
    def find_by(sender):
        letter_da = DataAccess(Letter)
        return letter_da.find_by(Letter.sender == sender)

    @staticmethod
    def find_by(receiver):
        letter_da = DataAccess(Letter)
        return letter_da.find_by(Letter.receiver == receiver)

    @staticmethod
    def find_by(letter_group):
        letter_da =DataAccess(Letter)
        return letter_da.find_by(Letter.letter_group == letter_group)

    @staticmethod
    def find_by(title):
        letter_da = DataAccess(Letter)
        return letter_da.find_by(Letter.title == title)

    @staticmethod
    def find_by(priority):
        letter_da = DataAccess(priority)
        return letter_da.find_by(Letter.priority == priority)