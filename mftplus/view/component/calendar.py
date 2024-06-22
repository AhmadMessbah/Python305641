import tkinter.ttk
import datetime
from persiantools.jdatetime import JalaliDate


class Calendar:
    def date_change(self, event):
        days_in_month = self.now.days_in_month(int(self.month_cmb.get()), int(self.year_cmb.get()))
        self.day_cmb['values'] = list(range(1, days_in_month + 1))
        print(self.now.isoweekday())

    def __init__(self, master, x=20, y=20):
        self.now = JalaliDate.today()
        self.year = self.now.year
        self.month = self.now.month
        self.day = self.now.day
        self.days_in_month = self.now.days_in_month(self.month, self.year)

        self._year_cmb = tkinter.ttk.Combobox(master, width=5)
        self._year_cmb['state'] = 'readonly'
        self._year_cmb['values'] = list(range(self.year - 50, self.year + 1))
        self._year_cmb.current(50)
        self._year_cmb.bind("<FocusIn>", self.date_change)
        self._year_cmb.place(x=x, y=y)

        self.month_cmb = tkinter.ttk.Combobox(master, width=8)
        self.month_cmb['state'] = 'readonly'
        # self.month_cmb['values'] = ['فروردین','اردیبهشت','خرداد','تیر','مرداد','شهریور','مهر','آبان','آذر','دی','بهمن','اسفند']
        self.month_cmb['values'] = list(range(1, 13))
        self.month_cmb.current(self.month - 1)
        self.month_cmb.bind("<FocusIn>", self.date_change)
        self.month_cmb.place(x=x + 60, y=y)

        self.day_cmb = tkinter.ttk.Combobox(master, width=4)
        self.day_cmb['state'] = 'readonly'
        self.day_cmb['values'] = list(range(1, self.days_in_month + 1))
        self.day_cmb.current(self.day - 1)
        self.day_cmb.place(x=x + 140, y=y)
