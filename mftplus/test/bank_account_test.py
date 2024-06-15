from mftplus.model.da.da import DataAccess
from mftplus.model.entity.bank_account import BankAccount
from mftplus.model.entity.person import Person

bank_account = BankAccount("parsian","aaaa",1234,123456,"bbb",True)
bank_account_da = DataAccess(bank_account)
bank_account_da.save(bank_account)

person = Person("arshida","gashtasbi")
person.bank_account = bank_account
person_da = DataAccess(Person)
person_da.save(person)
print(person)

print(bank_account)