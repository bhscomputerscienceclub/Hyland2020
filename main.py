import tkinter as tk
from read import *
from write import *

 
window = tk.Tk()
window.geometry('750x1334')
window.title("Easy Weather")

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



coldB = tk.Button(window, width = 50, height = 50, image = coldP, command = gowrite('Too Cold'))
rightB = tk.Button(window, width = 50, height = 50, image = rightP, command = gowrite('Just Right'))
hotB = tk.Button(window, width = 50, height = 50, image = hotP, command = gowrite('Too Hot'))
 
coldB.grid(column=0, row=5)
rightB.grid(column=1, row=5)
hotB.grid(column=2, row=5)

 
window.mainloop()