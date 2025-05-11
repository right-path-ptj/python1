from tkinter import *

window = Tk()

photo = PhotoImage(file="1.gif")
label1 = Label(window, image=photo)

photo1 = PhotoImage(file="2.gif")
label2 = Label(window, image=photo1)

label1.pack(side=LEFT)
label2.pack()

window.mainloop() 