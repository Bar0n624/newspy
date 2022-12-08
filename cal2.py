from tkinter import *
from tkcalendar import *
from tkinter import messagebox

root = Tk()
root.config(bg="black")

cal = Calendar(root, font="Courier 20")
cal.pack(fill="both", expand=True)

rem = {}


def LISTevents(date):
    print(rem[date])

def ADDevent(date):
    global rem
    cal.calevent_create(date, "Hello", tags=["test1"])
    if date not in rem:
        rem[date]=[]
    rem[date].append("HELLO")
    print(rem)

Button(root, text="Add Event", command=lambda: ADDevent(cal.selection_get())).pack(side=LEFT)
Button(root, text="List Event", command= lambda: LISTevents(cal.selection_get())).pack(side=LEFT)

root.mainloop()
