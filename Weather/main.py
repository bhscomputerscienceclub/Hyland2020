import tkinter as tk
 
window = tk.Tk()
 
window.title("Easy Weather")
 
window.geometry('750x1334')
 
lbl = tk.Label(window, text="Hello", font = ("Arial Bold", 50))
 
lbl.grid(column=0, row=0)

photo1 = tk.PhotoImage(file = "Weather/Buttons/too cold.svg")

btn = tk.Button(window, image = photo1)
 
btn.grid(column=1, row=0)
 
window.mainloop()