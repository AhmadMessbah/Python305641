from mftplus.model.da.da import DataAccess
from mftplus.model.entity.Financial_Document import FinancialDocument
from mftplus.model.entity.person import Person




Financial_Document = FinancialDocument("2222","55555","2024/01/01","recive","bbb")
Financial_Document_da = FinancialDocument(Financial_Document)
Financial_Document_da.save(FinancialDocument)
print(Financial_Document)

person = Person("Simin","Eghbali")
person_da = DataAccess(Person)
person_da.save(person)
print(person)

