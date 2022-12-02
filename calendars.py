from tkinter import *
from tkcalendar import *
from tkinter import messagebox

root = Tk()
root.config(bg="black")

cal = Calendar(root, font="Courier 20")
cal.pack(fill="both", expand=True)

rem = {}


def LISTevents():
    E_Wid = Toplevel(master=root)

    Label(master=E_Wid, text="Date : ").grid(row=0, column=0)
    date_E = DateEntry(master=E_Wid)
    date_E.grid(row=0, column=2)
    op_field = Text(master=E_Wid, font="Courier 20")

    def listing():

        if not (rem):
            messagebox.showerror(title="Error", message="No Plans.")
            E_Wid.destroy()
        else:
            s = ""
            for i in rem:
                for j in rem[i]:
                    s += f"{i}:{j}\n"

            op_field.insert(END, s)
            op_field.grid(row=1, column=0, columnspan=3)
    Button(E_Wid, text="Go", command=listing).grid(row=0, column=3)
    E_Wid.mainloop()


def ADDevent(date):
    global rem
    E_Wid = Toplevel(master=root)
    Label(master=E_Wid, text=f"Date of the event {date}.").pack()

    E_Name = Entry(master=E_Wid)
    E_Name.pack()

    def ADDER():
        if date not in rem:
            rem[date] = []
        rem[date].append(str(E_Name.get()))
        print(rem)
        ans = messagebox.showinfo(
            title="successfully Added", message="Event added successfully to the Plans.")
        print(ans)

        E_Wid.destroy()
    Button(E_Wid, text="Add Event", command=ADDER).pack()

    E_Wid.mainloop()


Button(root, text="Add Event", command=lambda: ADDevent(
    cal.get_date())).pack(side=LEFT)
Button(root, text="List Event", command=LISTevents).pack(side=LEFT)

root.mainloop()
