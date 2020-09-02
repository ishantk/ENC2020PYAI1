from tkinter import *


window = Tk()
window.title("Auribises")


spin_box = Spinbox(window, from_=1, to=10, width=10)
spin_box.grid(column=0, row=0)

# to get the data from the SpinBox
# spin_box.get()

window.geometry("300x300")
window.mainloop()