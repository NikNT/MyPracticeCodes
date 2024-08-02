from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_lable.config(text=time_string)

    day_string = strftime("%A")
    day_lable.config(text=day_string)

    date_string = strftime("%B %d %Y")
    date_lable.config(text=date_string)

    window.after(1000, update)

window = Tk()

time_lable = Label(window, font=("Arial", 50), fg="#00FF00", bg="#000000")
time_lable.pack()

day_lable = Label(window, font=("Ink Free", 25))
day_lable.pack()

date_lable = Label(window, font=("Ink Free", 25))
date_lable.pack()


update()

window.mainloop()
