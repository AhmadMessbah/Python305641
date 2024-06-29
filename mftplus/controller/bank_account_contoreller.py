from mftplus.model.service.bank_account_service import BankAccountService
from mftplus.model.tools.logger import Logger

class BankAccountController:

    @staticmethod
    def save(bank_account):
        try:
            bank_account_service = BankAccountService(bank_account)
            logger = Logger(f"Bank Account Saved - {bank_account}")
            return True , bank_account
        except Exception as e:
            logger.error(f"{e}")
            return False , f"{e}"

    @staticmethod
    def edit(bank_account):
        try:
            if BankAccountService.find_by_id(bank_account.id):
                BankAccountService.edit(bank_account)
                logger = Logger(f"Bank Account edited - {bank_account}")
                return True , bank_account
        except Exception as e:
            logger.error(f"{e}")
            return False , f"{e}"

    @staticmethod
    def remove(bank_account):
        try:
            bank_account = BankAccountService.remove(id)
            logger.info = Logger(f"Bank Account Removed - {bank_account}")
            return True , bank_account
        except Exception as e:
            logger.error(f"{e}")
            return False , f"{e}"

    @staticmethod
    def find_all(bank_account):
        try:
            bank_account_list = BankAccountService.find_all()
            logger.info = Logger(f"Bank Account Find All")
            return True , bank_account_list
        except Exception as e:
            logger.error(f"{e}")
            return False , f"{e}"
    def find_by_id(bank_account):
        try:
            bank_account = BankAccountService.find_by_id(id)
            logger.info = Logger(f"Bank Account Find by Id - {id}")
            return True , bank_account
        except Exception as e:
            logger.error(f"{e}")
            return False , f"{e}"

    @staticmethod
    def find_by_bank(bank_account):
        try:
            bank_account_list = BankAccountService.find_by_bank(bank_account)
            logger.info = Logger(f"Bank Account"-{bank})
            return True , bank_account_list
        except Exception as e:
            logger.error(f"{e}")
            return False , f"{e}"



