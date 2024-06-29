from mftplus.model.da.da import DataAccess
from mftplus.model.entity.employeement import Employeement
from mftplus.view.component.label_text import TextWithLabel
from mftplus.view.component.table import Table
from tkinter import *

class EmployeeMentView:
    def employeement_table_click(self, row):
        print(row)

    def emloyeement_table_click(self,row):
        print(row)

    def __init__(self):
        self.Employee_da = DataAccess(Employeement)
        self.win = Tk()
        self.title("Employee View")
        self.win.geometry("500x500")

        employee_table = Table(self.win,["id","name","family","insurance","peyment"],
                               [60,80,80,80,50,60,60],300,20,
                               self.employeement_table_click)
        self.win.mainloop()

