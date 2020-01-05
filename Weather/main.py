import tkinter as tk
from read import *
from write import *

window = tk.Tk()
window.geometry('750x1334')
window.title("ezWeather")

title = tk.Label(window, text = "What is the (city, state) you're in? ")
title.grid(column = 0, row = 0)

txt = tk.Entry(window, width = 10)
txt.grid(column = 1, row = 0)

tip1 = tk.Label(window, text="")
tip1.grid(column = 0, row = 1)

def calculate():
    read = []
    read = goread(str(txt.get()))
    tip1.configure(text = "A little tip: {}".format(read[0]))
    

enter = tk.Button(window, width = 4, height = 1, text = "Enter", command = calculate)
enter.grid(column = 2, row = 0)


coldP = tk.PhotoImage(file = "Weather/too cold.png")
rightP = tk.PhotoImage(file = "Weather/just right.png")
hotP = tk.PhotoImage(file = "Weather/too hot.png")

question1 = tk.Label(window, text = "What do you think about the tips?")
question1.grid(column = 0, row = 5)

thank = tk.Label(window, text = "")
thank.grid(colum = 0, row = 6)

def feedback(something):
    gowrite(something)
    thank.configure(text = "Thank you for your feedback!")

coldB = tk.Button(window, width = 50, height = 50, image = coldP, command = feedback('Too Cold'))
rightB = tk.Button(window, width = 50, height = 50, image = rightP, command = feedback('Just Right'))
hotB = tk.Button(window, width = 50, height = 50, image = hotP, command = feedback('Too Hot'))
 
coldB.grid(column = 1, row = 5)
rightB.grid(column = 2, row = 5)
hotB.grid(column = 3, row = 5)

 
window.mainloop()