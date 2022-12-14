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

    def listing(date):
        op_field.delete("1.0",END)
        print(date)
        if (not (rem) ) or (date not in rem):
            messagebox.showerror(title="Error", message="No Plans.")
            E_Wid.destroy()
        elif date in rem:
            s = ""
            for j in rem[date]:
                    s += f"{date}:{j}\n"

            op_field.insert(END, s)
            op_field.grid(row=1, column=0, columnspan=3)


    Button(E_Wid, text="Go", command= lambda: listing(date_E.get_date())).grid(row=0, column=3)
    E_Wid.mainloop()


def ADDevent(date):
    global rem
    cal.calevent_create(date, "Hello", tags=["test1"])
    if date not in rem:
        rem[date]=[]
    rem[date].append("HELLO")
    print(rem)

def DELevent(date):
    MessageDIS="Select the event no. \n"
    for i in range(len(rem[date])):
        MessageDIS+=f"{i+1 :>3} : {rem[date][i] :>15}\n"
    messagebox.showinfo(title="Menu", message=MessageDIS)

    E_Wid = Toplevel(master=root)
    del_date = Entry(master=E_Wid)
    del_date.pack()

    def del_confirm():
        question = messagebox.showwarning("Please confirm","please confirm")
        if question:
            rem[date].pop(int(del_date.get())-1)
            messagebox.showinfo("done","done")
            E_Wid.destroy()
    


    Button(master=E_Wid,text="Click",command=del_confirm).pack()
    E_Wid.mainloop()    


        


Button(root, text="Add Event", command=lambda: ADDevent(cal.selection_get())).pack(side=LEFT)
Button(root, text="List Event", command=LISTevents).pack(side=LEFT)
Button(root, text="DEL Event", command=lambda: DELevent(cal.selection_get())).pack(side=LEFT)

root.mainloop()
