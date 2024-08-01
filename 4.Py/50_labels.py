# label = area widget that holds a text or image

from tkinter import *
window = Tk()
window.geometry("1440x1080")
photo = PhotoImage(file='logo.png')

label = Label(window, 
              text="Hello World", 
              font=('Arial', 40, 'bold'), 
              fg='#00ff00', 
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20, 
              image=photo, 
              compound='top')

label.place(x=100, y=100)
window.mainloop()
