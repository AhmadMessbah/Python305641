from mftplus.model.da.da import DataAccess
from mftplus.model.entity.car import Car
from mftplus.model.entity.person import Person
from mftplus.view.component.label_text import TextWithLabel
from mftplus.view.component.table import Table
from tkinter import *

class PersonCarView:
    def car_table_click(self, row):
        print(row)

    def person_table_click(self, row):
        person = self.person_da.find_by_id(int(row[0]))
        total = 0


        self.car_table.refresh_table(person.car)
        self.total.variable.set(total)

    def __init__(self):
        self.person_da = DataAccess(Person)
        self.invoice_da = DataAccess(Car)

        self.win = Tk()
        self.win.title("Persons cars View")
        self.win.geometry("870x300")

        self.person_table = Table(self.win,
                                  ["Id", "Name", "Family", "NationalId"]
                                  , [60, 80, 80, 80],
                                  20, 20,
                                  self.person_table_click
                                  )

        self.person_table.refresh_table(self.person_da.find_all())

        self.car_table = Table(self.win,
                                   ["Id", "Name", "Model", "Man_Date"],
                                   [60, 80, 80, 50],
                                   400, 20,
                                   self.car_table_click
                                   )

        self.total = TextWithLabel(self.win, "Total", 400, 260)


        self.win.mainloop()
