from tkinter import *
import json
from tkinter import messagebox
def main():



    ct_root=Tk()

    with open("user_custom.json",'r') as setting:
                current_default = json.load(setting)

    ct_root.title("Settings")
    Label(ct_root,text='Settings',font="Algerian 20").grid(row=0,column=0,columnspan=2,pady=(12,25),padx=20)


    Label(ct_root,text='Stocks  ').grid(row=1,column=0,sticky=W)
    stock_entry=Entry(ct_root)
    stock_entry.insert(END,current_default["tickerlist"])
    stock_entry.grid(row=1,column=1)


    Label(ct_root,text='Background  ').grid(row=2,column=0,sticky=W)
    bg_entry=Entry(ct_root)
    bg_entry.grid(row=2,column=1)

    Label(ct_root,text='Theme  ').grid(row=3,column=0,sticky=W)
    th_val=StringVar()
    th_val.set(current_default["colormode"])
    th_menu=OptionMenu(ct_root, th_val,"Light","Dark","Auto")
    th_menu.grid(row=3,column=1)

    Label(ct_root,text='Weather location  ').grid(row=4,column=0,sticky=W)
    weather_entry=Entry(ct_root)
    weather_entry.grid(row=4,column=1)

    def save_changes():
        ans = messagebox.askokcancel("Confirmaton","Confirm changes ?")
        if ans :

            print(current_default)
            current_default["tickerlist"] = stock_entry.get().split(" ")
            current_default["colormode"] = str(th_val.get())
        
            with open("user_custom.json",'w') as setting:
                json.dump(current_default,setting,indent=4)
            print(current_default)
            ct_root.destroy()
        else:
            return
            
    cb=Button(ct_root,text="Cancel",command=ct_root.destroy)
    cb.grid(row=5,column=0)
    sb=Button(ct_root,text="Save",command=save_changes)
    sb.grid(row=5,column=1)


    ct_root.mainloop()

if __name__ == "__main__":
    main()