
person = Person("Simin","Eghbali")
person.bank_account = bank_account
person_da = DataAccess(Person)
person_da.save(person)
print(person)

print(bank_account)