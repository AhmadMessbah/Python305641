from mftplus.model.da.da import DataAccess
from mftplus.view.component.label_text import TextWithLabel
from mftplus.view.component.table import Table
from mftplus.model.entity.medical_report import MedicalReport
from mftplus.model.entity.person import Person
from tkinter import *

class PersonMedicalReportView:
    def person_table_click(self,row):
        print (row)

    def medical_report_table_click(self, row):
        print(row)

    def __init__(self):
        self.Person_da = DataAccess(Person)
        self.medical_report_da = DataAccess(MedicalReport)
        self.win = Tk()
        self.title("Person MedicalReport View")
        self.win.geometry("500x500")

        person_table = Table(self.win,
                             ["Id", "Name", "Family", "NationalId", "Status"],
                             [60,80,80,80,50], 20, 20 ,
                             self.person_table_click)

        self.person_table.refresh_table(self.person_da.find_all())



        medical_report_table = Table(self.win,
                             ["Id","Disease","ReportGroup","DateTime", "Deleted"],
                             [60,80,80,80,60],300,20 ,
                             self.medical_report_table_click)

        self.win.mainloop()