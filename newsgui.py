'''
News GUI
News GUI is a clean, intuitive and functional GUI written in python. 
The module Tkinter is used to create a native GUI and several APIs are used to collect various data like the latest news, financial information, weather data and covid-19 statistics. 
The data is collected from the APIs using the python requests library in the json format and is then parsed by the json module. 
The parsed data is then organized in the GUI using the Tkinter widgets. The Tkinter widgets - buttons, labels, canvas and frame - are gridded into the GUI and the final layout is presented to the user.
Salient features include:
    Intuitive layout
    Automatic detection of the user's country and location using the network IP address
    Current weather information for the user's city
    Latest information about the value of user inputted stocks, neatly organized in a graph
    Top news in the user's country with related pictures and a short snippet of the article. When button or text is clicked, user is taken to the article in the default web browser
    Automatic dark theme based on the time of the day to reduce strain on the eyes
'''
from tkinter import *
from time import strftime
import os, errno, stock, webbrowser, weather, news, location
import yfinance as yf

#Create Nominatim object for geolocation

stockdownloadlist = {}
flagdaynight = True
colormode=-1

#Default stock ticker list
tickerlist = ["MSFT", "AAPL", "TSLA", "GOOGL", "GME"]


def time(): 
    currenttime = strftime('%I:%M:%S %p') 
    timeLabel.configure(text = currenttime)  
    timeLabel.after(1000,time)

def greeting():
    currenthour = int(strftime('%H'))
    #Greeting based on the time of the day
    if 5<=currenthour<12:
        greetLabel.configure(text="Good morning")
    elif 12<=currenthour<17:
        greetLabel.configure(text="Good afternoon")
    elif 17<=currenthour<=23 or 0<=currenthour<5:
        greetLabel.configure(text="Good evening")

def date():
    #sets date
    currentdate = strftime('%A, %d %B %Y')
    dateLabel.configure(text = currentdate)

def open_site(url):
    #function to open a url in browser
    webbrowser.open(url, new=0)

def mkdir_p(path):
    #creates path for assets and other important stuff
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
if __name__=='__main__':  #this is the main function of the program
    print ("Collecting data from the internet. Please Wait...")
    mkdir_p("assets")
    city_name, country_name, country_code = location.location() #gets information from the location file
    hour = int(strftime('%H'))

    if ((0<=hour<6 or 18<hour<=23) and colormode==0) or colormode==1: #function to change between lightmode and dark mode depending upon user preferences and time
        bgcol = "#303032"
        fgcol = "white"
        flagdaynight=False
    else:
        bgcol="white"
        fgcol = "black"

    #Tkinter boilerplate shit
    root = Tk()
    root.geometry("1400x750")
    root.title("NEWS")
    root.configure(bg=bgcol)

    #Frames

    #frame for daytime
    framedaytime = Frame(root)
    framedaytime.grid(row=0,column=1,padx=(130,0), sticky="w")
    framedaytime.configure(bg=bgcol)

    #frame for weather
    frameweather = Frame(root)
    frameweather.grid(row=0,column=2,padx=(60,0))
    frameweather.configure(bg=bgcol)

    #frame for stocks
    framestock = Frame(root)
    framestock.grid(row=1,column=0, sticky="n")
    framestock.configure(bg=bgcol)
    framenews = Frame(root)
    framenews.grid(row=1, column=1, padx=(30,0), columnspan=2, sticky="n")
    framenews.configure(bg=bgcol)
    
    
    #Widgets

    #Greetings and date time
    greetLabel = Label(framedaytime, font=("bahnschrift",20), bg=bgcol, fg=fgcol)
    greeting()

    timeLabel = Label(framedaytime, font=("century gothic",40), bg=bgcol, fg=fgcol)
    time()

    dateLabel = Label(framedaytime, font =("bahnscrift", 15), bg=bgcol, fg=fgcol)
    date()

    greetLabel.grid(row = 0, column = 1,sticky = 'w')
    timeLabel.grid(row = 1, column=1, sticky='w')
    dateLabel.grid(row = 2, column = 1, sticky = 'w')

    #Weather information is set in the next few lines of code using information from the weather file

    weathertextLabel = Label(frameweather, text = "Weather", font =("century gothic bold", 25), bg=bgcol, fg=fgcol)
    weatherLabel = Label(frameweather, font =("century gothic", 20), bg=bgcol, fg=fgcol)
    weatherLabel.configure(text=weather.weather(city_name), compound="right")

    locLabel = Label(frameweather, text = "%s, %s"%(city_name,country_name), font =("century gothic", 15), bg=bgcol, fg=fgcol)

    weatherim = PhotoImage(file="assets/weather.png") #loads the weather asset png
    weatherLabel.configure(image=weatherim)

    weathertextLabel.grid(row=0,column=1,sticky="w")
    weatherLabel.grid(row = 1,column=1,sticky="nw")

    locLabel.grid(row=0,column=3,sticky="w", padx=(30,0))

    #Stock information
    stockLabel = Label(framestock, text = "Live Stock Info", font =("century gothic bold", 20), bg=bgcol, fg=fgcol)
    stockLabel.grid(row=0,column=0,columnspan=2, sticky="n", pady=(30,0))

    rownumgraph = 1
    print (f"Collecting data for {len(tickerlist)} stock ticker(s)...")

    #calls stock function within stock file to load stock data into the stock labels
    stock.stock(tickerlist,framestock,bgcol,fgcol,yf,stockdownloadlist,flagdaynight,rownumgraph)

    #News data
    news.newsparse(framenews,bgcol,fgcol,country_code)

    root.mainloop()

