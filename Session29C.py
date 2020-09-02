from tkinter import *
from tkinter import messagebox

def on_click():
    # messagebox.showinfo("This is Title", "This is Message in Message Box")
    # messagebox.showerror("This is Title", "This is Message in Message Box")
    # messagebox.showwarning("This is Title", "This is Message in Message Box")

    # response = messagebox.askquestion("Delete", "Would you like to delete the User?")
    # print(response, type(response)) # yes or no as 2 different strings :)

    # askyesnocancel gives us Boolean in Return
    response = messagebox.askyesnocancel("Delete", "Would you like to delete the User?")
    print(response)

window = Tk()
window.title("Auribises")

# ScrolledText is a TextArea -> We can get and set data from TextArea

btn_submit = Button(window, text="Submit", command=on_click)

btn_submit.grid(column=0, row=0)

window.geometry("300x300")
window.mainloop()