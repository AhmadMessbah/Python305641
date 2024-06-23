from mftplus.view.component.label_text import TextWithLabel
from mftplus.view.component.table import Table
from _tkinter import *
from tkinter import ttk as Tk





class PersonLetterView:
    def letter_table_click(self,row):
        print(row)

    def person_table_click(self,row):
        person = self.person_da.find_by_id(int(row[0]))

    def __init__(self):

        self.win= Tk()
        self.win.title("Person letter")
        self.win.geometry('100x80')


        self.person_table= Table(self.win,
                            ["id","name","family","status"],
                            [60,80,80,50],
                            20,20,
                            self.person_table_click
                            )
        self.person_table.refresh_table()


        self.letter_table= Table(self.win,
                            ["id","sender","receiver","letter_group","title","priority","status","deleted"],
                            [60,80,80,80,80,80,50,60],
                            380,20,
                            self.letter_table_click
                            )


        self.win.mainloop()

