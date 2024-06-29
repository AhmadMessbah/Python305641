from mftplus.controller.exceptions.exeptions import BankAccountNotFoundError
from mftplus.model.da.da import DataAccess
from mftplus.model.entity.BankAccount import BankAccount

class BankAccountService:

    @staticmethod
    def save(bank_account):
        bank_account_da = DataAccess(BankAccount)
        bank_account_da.save(bank_account)
        return bank_account

    @staticmethod
    def edit(bank_account):
        bank_account_da = DataAccess(BankAccount)
        if bank_account_da.find_by_id(bank_account.id):
            bank_account_da.edit(bank_account)
            return bank_account
        raise BankAccountNotFoundError

    @staticmethod
    def remove(id):
        bank_account_da = DataAccess(BankAccount)
        if bank_account_da.find_by_id(id):
            return bank_account_da.remove(id)
        else:
            raise BankAccountNotFoundError

    @staticmethod
    def find_all():
        bank_account_da = DataAccess(BankAccount)
        return bank_account_da.find_all()

    @staticmethod
    def find_by_id(id):
        bank_account_da = DataAccess(BankAccount)
        return bank_account_da.find_by_id(id)

    @staticmethod
    def find_by_bank(bank):
        bank_account_da = DataAccess(BankAccount)
        return bank_account_da.find_by_bank(bank)

