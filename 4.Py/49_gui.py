# widgets : GUI elements - Buttons, Textbox, Labels, Images
# windows : container to contain widgets

from tkinter import *
window = Tk() # instantiate an instance of a window
window.geometry("420x420")
window.title('First Tkinter GUI')

icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)

window.config(background="#5CFCFF")


window.mainloop() # place window on screen and listen for events

