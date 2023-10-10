from tkinter import *
import calendar


window = Tk()
window.title("Lloyd's Calendar Check.")
window.config(padx=20, pady=20, background="honeydew1")
window.geometry("200x170")
contents = calendar.calendar(2023)


### Function to get the Calendar____#
def showCalender():
    window = Tk()
    window.config(background='cyan')
    year = int(cal_entry.get())    ## need to be integer as calendar takes an integer input
    window.title(f"The Calender for the year {year}")
    window.geometry("580x520")
    window_content=calendar.calendar(year)
    calYear = Label(window, text=window_content, font="Consolas 10 bold", justify=LEFT)
    calYear.grid(row=5, column=1, padx=10)


#####____UI______####

cal_label = Label(text="Calendar",bg="turquoise1", font=("impact", 30, "bold"))
cal_label.grid(row=0, column=0, columnspan=2)

year_label = Label(text="Please enter the year.")
year_label.grid(row=1, column=1)

cal_entry = Entry(width=20, )
cal_entry.focus()##This will allow the cursor to start inside the entry box.
cal_entry.grid(row=2, column=0,columnspan=2)

cal_button = Button(text="Show Calender", fg="white", bg="black", command=showCalender)
cal_button.grid(row=3, column=1)




# contents = calendar.calendar(year)
# print(year)




window.mainloop()
