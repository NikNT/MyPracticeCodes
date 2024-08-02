from tkinter import *


def click():
    print("You clicked the 'Click Me' button")


window = Tk()

button = Button(
    window,
    text="Click Me!",
    command=click,
    font=("Comic Sans", 30),
    fg="#00FF00",
    bg="#000000",
    activeforeground="#00ff00",
    activebackground="#000000",
)
button.pack()

window.mainloop()
