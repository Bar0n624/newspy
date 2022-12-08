from tkinter import *
from tkcalendar import *
from tkinter import messagebox

root = Tk()
root.config(bg="black")

cal = Calendar(root, font="Courier 20")
cal.pack(fill="both", expand=True)

rem = {}


def LISTevents():
    ...
def ADDevent(date):
    ...

Button(root, text="Add Event", command=lambda: ADDevent(cal.get_date())).pack(side=LEFT)
Button(root, text="List Event", command=LISTevents).pack(side=LEFT)

root.mainloop()
