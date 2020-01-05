import tkinter as tk
from read import *
from write import *
import time as timelib

import weathertest as wt
from datetime import datetime
import tzlocal

time = int(wt.time.time())

window = tk.Tk()
window.geometry('750x500')
window.configure(background='white')
window.title("ezWeather")

#def get_digit(number, n):
#   return number // 10**n % 10
#window.root.wm_attributes('-transparentcolor','black')
print(datetime.utcfromtimestamp(time))
'''
local_timezone = tzlocal.get_localzone() # get pytz timezone
local_time = datetime.fromtimestamp(time, local_timezone)
#hour
hour = str(local_time)[11]+ str(local_time)[12]
date = str(local_time)[5:10]'''

morning_pic = "Weather/Background Pics/clear-day.png"
night_pic = "Weather/Background Pics/clear-ight.png"
time_picture = tk.PhotoImage(file = "")
'''
if int(hour) >=6 and int(hour) < 18:
    time_picture = morning_pic
else:
    time_picture = night_pic'''

background_image = time_picture
background_label = tk.Label(window, image = background_image)
background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

#read part
title = tk.Label(window, text = "What is the (city, state) you're in? ")

title.grid(column = 0, row = 0)

txt = tk.Entry(window, width = 10)
txt.grid(column = 1, row = 0)

tip1 = tk.Label(window, text="", font = ("Roboto", 30))
tip1.grid(columnspan = 8, row = 14)

temperature = 0

no_pre = tk.PhotoImage(file = "Weather/no precipitation.png")
yes_pre = tk.PhotoImage(file = "Weather/rainy.png")
prec_image = tk.PhotoImage(file = "")

class fcc():
    pass

def calculate():
    read = []
    read = goread(str(txt.get()))
    tip1.configure(text = "A little tip: {}".format(read[0]))
    global fcc
    fcc = wt.fcur(wt.getloc(txt.get()),time) 
    temperature = fcc.temperature
    temp_value.configure(text = str(temperature) + " degrees")
    if fcc.precipProbability > .2:
        prec_image = yes_pre
    else:
        prec_image = no_pre
    prec_value.configure(image = prec_image)
    time_picture.configure(file =  "Weather/Background Pics/{}.png".format(fcc.icon))
    #hour = str(timelib.strftime("%H", timelib.gmtime(time)))
    '''if int(hour) >=6 and int(hour) < 18:
        time_picture = morning_pic
    else:
        time_picture = night_pic'''
   

enter = tk.Button(window, width = 4, height = 1, text = "Enter", command = calculate)
enter.grid(column = 2, row = 0)


quote = tk.Label(window, bg = "pink", text = 'Daily Quote: ' + '"Success is a journey not a destination"' + '\n' + '-Ben Sweetland', font = ("Caveat", 20))
quote.grid(columnspan = 8, row = 40)

#write part
coldP = tk.PhotoImage(file = "Weather/too cold.png")
rightP = tk.PhotoImage(file = "Weather/just right.png")
hotP = tk.PhotoImage(file = "Weather/too hot.png")


question1 = tk.Label(window, text = "What do you think about the tips today?")
question1.grid(column = 0, row = 16)

thank = tk.Label(window, text = "")
thank.grid(column = 0, row = 18)

def feedback5(something):
    gowrite(something)
    thank.configure(text = "Thank you for your feedback! It's " + something)

coldB = tk.Button(window, width = 50, height = 50, image = coldP, command = lambda: feedback5("Too Cold"))
rightB = tk.Button(window, width = 50, height = 50, image = rightP, command = lambda: feedback5("Just Right"))
hotB = tk.Button(window, width = 50, height = 50, image = hotP, command = lambda: feedback5("Too Hot"))
 
coldB.grid(column = 1, row = 16)
rightB.grid(column = 2, row = 16)
hotB.grid(column = 3, row = 16)

# date temperature and precipitation
date1 = tk.Label(window, text = "Date", font = ("none", 20))
temp1 = tk.Label(window, text = "Temperature", font = ("none", 20))
prec1 = tk.Label(window, text = "Precipitation", font = ("none", 20))
date1.grid(column = 0, row = 10)
temp1.grid(column = 2, row = 10)
prec1.grid(column = 4, row = 10)

date_value = tk.Label(window, text = str(timelib.strftime("%m-%d", timelib.gmtime(time))), font = ("none", 30))
temp_value = tk.Label(window, text = str(temperature) + " degree", font = ("none", 30))
prec_value = tk.Label(window, image = prec_image)
date_value.grid(column = 0, row = 11)
temp_value.grid(column = 2, row = 11)
prec_value.grid(column = 4, row = 11)

time12345 = tk.Label(window, text = "Time: ", font = ("none", 15))
time1234 = tk.Label(window, text = str(timelib.strftime("%H:%M", timelib.gmtime(time))), font = ("none", 15))
time12345.grid(column = 0, row = 20)
time1234.grid(column = 0, row = 21)

window.mainloop()