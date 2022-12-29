from tkinter import *
import json
from tkinter import messagebox
import newsgui
def main(root):



    ct_root=Tk()
    ct_root.geometry('300x200')
    with open("user_custom.json",'r') as setting:
                current_default = json.load(setting)

    ct_root.title("Settings")
    Label(ct_root,text='Settings',font="Algerian 20").grid(row=0,column=0,columnspan=2,pady=(12,25),padx=20)


    Label(ct_root,text='Stocks  ').grid(row=1,column=0,sticky=W)
    stock_entry=Entry(ct_root,width=30)
    stock_entry.insert(END,current_default["tickerlist"])
    stock_entry.grid(row=1,column=1)



    Label(ct_root,text='Theme  ').grid(row=2,column=0,sticky=W)
    th_val=StringVar()

    th_val.set(str(current_default["colormode"]))

    print(th_val.get())
    th_menu=OptionMenu(ct_root, th_val,"Light","Dark","Auto")
    th_menu.grid(row=2,column=1)

    Label(ct_root,text='Weather location  ').grid(row=3,column=0,sticky=W)
    weather_entry=Entry(ct_root)
    weather_entry.grid(row=3,column=1)

    def save_changes():
        ans = messagebox.askokcancel("Confirmaton","Confirm changes ?")
        if ans :

            print(current_default)
            current_default["tickerlist"] = stock_entry.get().split(" ")
            current_default["colormode"] = str(th_val.get())

            
            a=current_default['tickerlist']
            if len(a)>5:
                s=messagebox.showerror("Interruption",'Please enter only 5 stocks ')
                return
                        
            with open("user_custom.json",'w') as setting:
                json.dump(current_default,setting,indent=4)
            print(current_default)
            # root.config(bg="black") 
            ct_root.destroy()
            # root.update_idletasks()
            root.destroy()
            newsgui.main()
            
        else:
            return
            
    cb=Button(ct_root,text="Cancel",command=ct_root.destroy)
    cb.grid(row=4,column=0)
    sb=Button(ct_root,text="Save",command=save_changes)
    sb.grid(row=4,column=1)


    ct_root.mainloop()

if __name__ == "__main__":
    main()