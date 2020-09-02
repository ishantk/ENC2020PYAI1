"""
    tkinter
    More of GUI
"""

from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Auribises")

# UI components in window are known as Widgets :)
lbl_title = Label(window, text="Welcome to Auribises")
# lbl_title.pack() # pack the widget in the center with the size occupied automatically

lbl_title.grid(column=0, row=0)

# btn_submit = Button(window, text="Submit", bg="orange", fg="red")
btn_submit = Button(window, text="Submit")
btn_submit.grid(column=1, row=0)

combo = Combobox(window)
combo['values'] = ("Select City", "Ludhiana", "Chandigarh", "Delhi", "Bangalore", "Chennai")
combo.current(0)
combo.grid(column=0, row=2)

# to get the current data in combo box
# combo.get()

check_button_state = BooleanVar() # BooleanVar is from tkinter
check_button_state.set(True)
check_button = Checkbutton(window, text="I Agree Terms & Conditions", var=check_button_state)
check_button.grid(column=0, row=3)

# to get the current state of Check button as true or false :)
# check_button_state.get()

window.geometry('350x350')
window.mainloop()

# Layouts or Formats -> pack and grid and many more to explore :)