from tkinter import *
from tkinter.ttk import*

from time import strftime

window = Tk()
window.title("Lloyd's Digital Clock")

def time():
    string = strftime('%H:%M:%S:%p')
    label.config(text=string)
    label.after(1000,time)

label = Label(window,font=("ds-digital", 100))
label.pack()


time()

window.mainloop()