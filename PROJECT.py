from tkinter import *
from tkinter import messagebox
import json
import requests


wid = Tk()
wid.title("Curreny Exchanger")
wid.resizable(0, 0)

def DETAILS():
    global choices
    info_wid=Tk()
    info_wid.resizable(0,1)
    info_wid.title("Detailed Information")
    s=""
    s+=f"{'Country Name':<35}\t{':' :^2}\t{'Country code':>15}\n"
    s+="_"*54+"\n"
    for i in choices:
        s+=f"{choices[i]:<35}\t{':' :^2}\t{i:>15}\n"
    T=Text(master=info_wid)
    T.insert(INSERT, s)
    T.configure(state='disabled')
    T.pack(expand=True,fill=BOTH)

    info_wid.mainloop()



menuBar = Menu(wid)
MENU1 = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='OPTION & HELP', menu=MENU1)
MENU1.add_command(label='Detailed Information',command=DETAILS)
wid.config(menu = menuBar)

amount = StringVar()


choice_from = StringVar()
choice_from.set("INR")


choice_to = StringVar()
choice_to.set("USD")


final_amt = StringVar()
final_amt.set("0")


with open('data.json', 'r', encoding="utf8") as fileObj:
    choices = json.load(fileObj)
    fileObj.close()


Label(wid, text="From: ").grid(row=0, column=0, columnspan=2)
MenuFrom = OptionMenu(wid, choice_from, *choices)
MenuFrom.grid(row=0, column=1, columnspan=2)
Label(wid, text="To: ").grid(row=0, column=2, columnspan=2)
MenuTo = OptionMenu(wid, choice_to, *choices)
MenuTo.grid(row=0, column=3, columnspan=2)
Label(wid, text="Amount: ").grid(row=1, column=0, columnspan=2)


def click(event):
    if input_entry.get() == 'Currency value.':
        input_entry.config(state=NORMAL)
        input_entry.delete(0, END)
    else:
        input_entry.config(state=NORMAL)


def unclick(event):
    if input_entry.get() == '':
        input_entry.delete(0, END)
        input_entry.insert(0, 'Currency value.')
        input_entry.config(state=DISABLED)
    else:
        input_entry.config(state=DISABLED)


input_entry = Entry(wid, textvariable=amount, width=15)
input_entry.grid(row=1, column=2, columnspan=2, sticky="W")

input_entry.insert(0, 'Currency value.')
input_entry.config(state=DISABLED)

input_entry.bind("<Button-1>", click)
input_entry.bind('<Leave>', unclick)

result_label = Label(wid)
result_label.grid(row=2, column=2, columnspan=2, sticky="E")


def convert():
    # print(str(choice_to.get()))
    # print(str(choice_from.get()))
    if str(amount.get()) == "Currency value.":
        amount.set("1")
    con_url = f"https://api.apilayer.com/fixer/convert?to={str(choice_to.get())}&from={str(choice_from.get())}&amount={str(amount.get())}"
    symbolsCurrencyJson = requests.get(
        "https://gist.githubusercontent.com/ksafranski/2973986/raw/5fda5e87189b066e11c1bf80bbfbecb556cf2cc1/Common-Currency.json").json()

    headers = {"apikey": "gibY1ggFgTfO5XY02pF69ZWZLYaOTFec"}

    response = requests.request("GET", con_url, headers=headers)

    result = response.json()
    Label(wid, text="Converted Amount: ").grid(
        row=2, column=0, columnspan=2, sticky="W")
    result_label.config(text=symbolsCurrencyJson[str(
        choice_to.get())]["symbol"]+" "+str(result["result"]))


Cal_button = Button(wid, text="Convert", command=convert)
Cal_button.grid(row=1, column=4)

wid.mainloop()
