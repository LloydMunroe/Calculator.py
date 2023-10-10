from tkinter import *
#from PyDictionary import PyDictionary

window = Tk()
window.title("Lloyd's Denshi Jisho")
window.config(padx=10, pady=10)

###___ UI_______####

####___ Text Display_____###
txtDisplay = Entry(font=('Helvetica', 12, 'bold'), bg='white', fg='blue',bd=4, width=60, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=10)
txtDisplay.insert(0, "|")

#####____To get Menu_________#

def Language():
    pass

def others():
    pass


def iExit():
    pass


menubar = Menu(window)



#ManuBar1:
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label="Language", command=Language)
filemenu.add_command(label="Others", command=others)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=iExit)


editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_separator()
editmenu.add_command(label="Paste")

window.config(menu=menubar)

letter_pad = "QAZWSXEDCRFVTGBYHNUJMIK?OL@P'&"
i = 0
btn = []
for j in range(0, 10):
    for k in range(1, 4):
        btn.append(Button(width=4, height=2, bg='blue', fg='white', font=('Helvetica', 12, 'bold'), bd=2, text=letter_pad[i]))
        btn[i].grid(row=k, column=j)
        i += 1
trans_btn = Button(text="Translate", width=16, height=2,bg='black', fg= "white", font=('Helvetica', 12, 'bold'), bd=2).grid(row=4, column=0, columnspan=3)
an_btn = Button(text="Antonym", width=16, height=2,bg='blue', fg= "white", font=('Helvetica', 12, 'bold'), bd=2).grid(row=4, column=3, columnspan=3)
sy_btn = Button(text="Meaning", width=20, height=2,bg='blue', fg= "white", font=('Helvetica', 12, 'bold'), bd=2).grid(row=4, column=6, columnspan=4)


window.mainloop()

# Import Required Library
# from tkinter import *
# from PyDictionary import PyDictionary
#
# # Create Objects
# dictionary = PyDictionary()
# root = Tk()
#
# # Set geometry
# root.geometry("400x400")
#
#
# def dict():
# 	meaning.config(text=dictionary.meaning(word.get())['Noun'][0])
# 	synonym.config(text=dictionary.synonym(word.get()))
# 	antonym.config(text=dictionary.antonym(word.get()))
#
#
# # Add Labels, Button and Frames
# Label(root, text="Dictionary", font=(
# 	"Helvetica 20 bold"), fg="Green").pack(pady=10)
#
# # Frame 1
# frame = Frame(root)
# Label(frame, text="Type Word", font=("Helvetica 15 bold")).pack(side=LEFT)
# word = Entry(frame, font=("Helvetica 15 bold"))
# word.pack()
# frame.pack(pady=10)
#
# # Frame 2
# frame1 = Frame(root)
# Label(frame1, text="Meaning:- ", font=("Helvetica 10 bold")).pack(side=LEFT)
# meaning = Label(frame1, text="", font=("Helvetica 10"))
# meaning.pack()
# frame1.pack(pady=10)
#
# # Frame 3
# frame2 = Frame(root)
# Label(frame2, text="Synonym:- ", font=("Helvetica 10 bold")).pack(side=LEFT)
# synonym = Label(frame2, text="", font=("Helvetica 10"))
# synonym.pack()
# frame2.pack(pady=10)
#
# # Frame 4
# frame3 = Frame(root)
# Label(frame3, text="Antonym:- ", font=("Helvetica 10 bold")).pack(side=LEFT)
# antonym = Label(frame3, text="", font=("Helvetica 10"))
# antonym.pack(side=LEFT)
# frame3.pack(pady=10)
#
# Button(root, text="Submit", font=("Helvetica 15 bold"), command=dict().pack()
#
# # Execute Tkinter
# root.mainloop()