import tkinter

window = tkinter.Tk()
window.title("Easy Weather")

window.geometry('750x1334')

photo1 = tkinter.PhotoImage(file = "too_cold.svg")

lbl = tkinter.Label(window, text = "Hello", font = ("Arial Bold", 50))
lbl.grid(column = 0, row = 0)

btn = tkinter.Button(window, text = "Read", image=photo1)
btn.grid(column = 1, row = 0)




window.mainloop()