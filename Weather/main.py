import tkinter as tk
from read import *
from write import *

window = tk.Tk()
window.geometry('750x1334')
window.configure(background='white')
window.title("ezWeather")

quote = tk.Label(window, bg = "pink", text = 'Daily Quote: ' + '"Success is a journey not a destination"' + '\n' + '-Ben Sweetland', font = ("Caveat", 20))
quote.grid(columnspan = 8, row = 8)

#read part
title = tk.Label(window, text = "What is the (city, state) you're in? ")
title.grid(column = 0, row = 0)

txt = tk.Entry(window, width = 10)
txt.grid(column = 1, row = 0)

tip1 = tk.Label(window, text="", font = ("Roboto", 10))
tip1.grid(column = 0, row = 1)

def calculate():
    read = []
    read = goread(str(txt.get()))
    tip1.configure(text = "A little tip: {}".format(read[0]))
    

enter = tk.Button(window, width = 4, height = 1, text = "Enter", command = calculate)
enter.grid(column = 2, row = 0)

#write part
coldP = tk.PhotoImage(file = "Weather/too cold.png")
rightP = tk.PhotoImage(file = "Weather/just right.png")
hotP = tk.PhotoImage(file = "Weather/too hot.png")

question1 = tk.Label(window, text = "What do you think about the tips?")
question1.grid(column = 0, row = 5)

thank = tk.Label(window, text = "")
thank.grid(column = 0, row = 6)

def feedback(something):
    gowrite(something)
    thank.configure(text = "Thank you for your feedback!")

coldB = tk.Button(window, width = 50, height = 50, image = coldP, command = feedback("Too Cold"))
rightB = tk.Button(window, width = 50, height = 50, image = rightP, command = feedback("Just Right"))
hotB = tk.Button(window, width = 50, height = 50, image = hotP, command = feedback("Too Hot"))
 
coldB.grid(column = 1, row = 5)
rightB.grid(column = 2, row = 5)
hotB.grid(column = 3, row = 5)

# date temperature and precipitation
date1 = tk.Label(window, text = "Date", font = ("none", 20))
temp1 = tk.Label(window, text = "Temperature", font = ("none", 20))
prec1 = tk.Label(window, text = "Precipitation", font = ("none", 20))
date1.grid(column = 0, row = 10)
temp1.grid(column = 2, row = 10)
prec1.grid(column = 4, row = 10)

date_value = tk.Label(window, text = "x", font = ("none", 30))
temp_value = tk.Label(window, text = "y degrees", font = ("none", 30))
prec_value = tk.Label(window, text = "x ", font = ("none", 30))
date_value.grid(column = 0, row = 11)
temp_value.grid(column = 2, row = 11)
prec_value.grid(column = 4, row = 11)
 
window.mainloop()