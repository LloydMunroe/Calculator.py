from tkinter import *
import math
import tkinter.messagebox

window = Tk()
window.title("Lloyd Calculator.")
#window.resizable(width=False, height=False)
window.geometry("480x560")
cal = Frame(window)
cal.grid()





txtDisplay = Entry(font=('Helvetica', 15, 'bold'), bg='black', fg='white',bd=28, width=38, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4)
txtDisplay.insert(0, "0")


def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator",
                                        "Do you want to exit ?")
    if iExit > 0:
        window.destroy()
        return

def Scientific():
    window.resizable(width=False, height=False)
    window.geometry("944x568+0+0")

def Standard():
    window.resizable(width=False, height=False)
    window.geometry("480x568+0+0")

menubar = Menu(cal)

# ManuBar 1 :
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label="Standard", command=Standard)
filemenu.add_command(label="Scientific", command=Scientific)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=iExit)

# ManuBar 2 :
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_separator()
editmenu.add_command(label="Paste")

window.config(menu=menubar)


class cal():
    def __int__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum= False
        self.op = ""
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum =="_":
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total= float(txtDisplay.get())

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)


    def display(selfself,value):
        txtDisplay.delete(0,END)
        txtDisplay.delete(0, END)


added_value = cal()

#####_____ UI________####

number_pad = "789456123"
i = 0
btn = []
for j in range(2, 5):
    for k in range(0, 3):
        btn.append(Button(width=6, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'), bd=4, text=number_pad[i]))
        btn[i].grid(row=j, column=k)
        i += 1
        #btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)


btnAllClear = Button(text=chr(67) + chr(69), width=6, height=2,bg='powder blue',
                     font=('Helvetica', 20, 'bold'), bd=4).grid(row=1, column=1)

btnClear = Button(text=chr(67), width=6, height=2, bg='powder blue',
                  font=('Helvetica', 20, 'bold'), bd=4).grid(row=1, column=0, pady=1)

btnsq = Button(text="\u221A", width=6, height=2,
               bg='powder blue', font=('Helvetica',
                                       20, 'bold'),
               bd=4).grid(row=1, column=2)

btnAdd = Button(text="+", width=6, height=2,
                bg='powder blue',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.operation("add")
                ).grid(row=1, column=3)

btnSub = Button(text="-", width=6,
                height=2, bg='powder blue',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.operation("sub")
                ).grid(row=2, column=3)

btnMul = Button(text="x", width=6,
                height=2, bg='powder blue',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.operation("multi")
                ).grid(row=3, column=3)

btnDiv = Button(text="/", width=6,
                height=2, bg='powder blue',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.operation("divide")
                ).grid(row=4, column=3)

btnZero = Button(text="0", width=6,
                 height=2, bg='black', fg='white',
                 font=('Helvetica', 20, 'bold'),
                 bd=4, command=lambda: added_value.numberEnter(0)
                 ).grid(row=5, column=0)

btnDot = Button(text=".", width=6,
                height=2, bg='powder blue',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.numberEnter(".")
                ).grid(row=5, column=1)
btnPM = Button(text=chr(177), width=6, height=2, bg='powder blue', font=('Helvetica', 20, 'bold'),
               bd=4).grid(row=5, column=2, pady=1)

btnEquals = Button(text="=", width=6,
                   height=2, bg='powder blue',
                   font=('Helvetica', 20, 'bold'),
                   bd=4, command=added_value.sum_of_total
                   ).grid(row=5, column=3, pady=1)






window.mainloop()