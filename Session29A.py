from tkinter import *
from tkinter.ttk import *

def on_click():
    value = selected_var.get()
    print("You Selected:", value)

window = Tk()
window.title("Auribises")

lbl_gender = Label(window, text="Select Your Gender:")

# IntVar is from tkinter library
selected_var = IntVar()

rb_male = Radiobutton(window, text="Male", value=1, variable=selected_var)
rb_female = Radiobutton(window, text="Female", value=2, variable=selected_var)
rb_others = Radiobutton(window, text="Others", value=3, variable=selected_var)

btn_submit = Button(window, text="Submit", command=on_click)

lbl_gender.grid(column=0, row=0)
rb_male.grid(column=0, row=1)
rb_female.grid(column=1, row=1)
rb_others.grid(column=2, row=1)
btn_submit.grid(column=0, row=2)


window.geometry("300x300")
window.mainloop()