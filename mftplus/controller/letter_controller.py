from mftplus.model.entity.letter import Letter
from mftplus.model.service.letter_service import LetterService
from mftplus.model.tools.logger import Logger

class LetterController:
    @staticmethod
    def save(sender, receiver, letter_group, title, priority):
        try:
            letter = Letter("sss","ddd","aaa","lll","kkk")
            LetterService.save(letter)
            Logger.info(f"letter save -{letter}")
            return True, letter
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def edit(id,sender, receiver, letter_group, title, priority):
        try:
            letter = Letter("sss","ddd","aaa","lll","kkk")
            letter.id= id
            LetterService.edit(letter)
            Logger.info(f"letter edit -{letter}")
            return True, letter
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def remove(id):
        try:
            letter = LetterService.remove(id)
            Logger.info(f"Letter remove -{letter}")
            return True, letter
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def findAll():
        try:
            letter_list =LetterService.find_all()
            Logger.info(f"letter findAll()")
            return True, letter_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_id(id):
        try:
            letter = LetterService.find_by_id(id)
            Logger.info(f"letter findById({id})")
            return True,letter
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_sender(sender):
        try:
            letter_list = LetterController.find_by_sender(sender)
            Logger.info(f"letterFindBysender({sender})")
            return True, letter_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_receiver(receiver):
        try:
            letter_list = LetterController.find_by_receiver(receiver)
            Logger.info(f"letterFindByreceiver({receiver})")
            return True, letter_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"


    @staticmethod
    def find_by_letter_group(letter_group):
        try:
            letter_list = LetterController.find_by_letter_group(letter_group)
            Logger.info(f"letterFindBylettergroup({letter_group})")
            return True, letter_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"


    @staticmethod
    def find_by_title(title):
        try:
            letter_list = LetterController.find_by_title(title)
            Logger.info(f"letterFindBytitle({title})")
            return True, letter_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"



    @staticmethod
    def find_by_priority(priority):
        try:
            letter_list = LetterController.find_by_priority(priority)
            Logger.info(f"letterFindBypriority({priority})")
            return True, letter_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"



