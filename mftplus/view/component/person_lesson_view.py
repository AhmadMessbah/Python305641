from mftplus.model.da.da import DataAccess
from mftplus.view.component.label_text import TextWithLabel
from mftplus.view.component.table import Table
from mftplus.model.entity.lesson import Lesson
from mftplus.model.entity.person import Person
from tkinter import *

class PersonLessonView:
    def person_table_click(self,row):
        print (row)

    def lesson_table_click(self, row):
        print(row)

    def __init__(self):
        self.Person_da = DataAccess(Person)
        self.lesson_da = DataAccess(Lesson)
        self.win = Tk()
        self.title("Person Lesson View")
        self.win.geometry("500x500")

        person_table = Table(self.win,
                             ["Id", "Name", "Family", "NationalId", "Status"],
                             [60,80,80,80,50], 20, 20 ,
                             self.person_table_click)

        self.person_table.refresh_table(self.person_da.find_all())
        lesson_table = Table(self.win,
                             ["Id","Lesson_group","Department","Title", "Code", "Teacher","Status"],
                             [60,80,80,80,50,60,60],300,20 ,
                             self.lesson_table_click)

        self.win.mainloop()