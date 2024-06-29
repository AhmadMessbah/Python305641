from mftplus.view.component.label_text import TextWithLabel
from mftplus.view.component.table import Table
from tkinter import *
from mftplus.model.da.da import DataAccess
from mftplus.model.entity.bank_account import BankAccount
from mftplus.model.entity.person import Person

class BankAccountView:
    def bank_account_table_click(self,row):
        print(row)

    def person_table_click(self, row):
        person = self.person_da.find_by_id(int(row[0]))
        total = 0
        self.car_table.refresh_table(person.car)
        self.total.variable.set(total)

    def __init__(self):
        self.person_da = DataAccess(Person)
        self.invoice_da = DataAccess(BankAccount)

        self.win = Tk()
        self.win.title("Bank Account View")
        self.win.geometry("870x300")

    self.person_table = Table(self.win,
                              ["Id", "Name", "Family", "NationalId"]
                              , [60, 80, 80, 80],
                              20, 20,
                              self.person_table_click
                              )

    self.person_table.refresh_table(self.person_da.find_all())

    self.bank_account_table = Table(self.win,
                                     ["Id", "bank", "branch", "account_number", "account_type", "card_number"],
    [60,80,80,80,50,60],
                                    300,20,
                                    self.bank_account_table_click)
    self.win.mainloop()
