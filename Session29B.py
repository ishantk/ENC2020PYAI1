from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext

window = Tk()
window.title("Auribises")

# ScrolledText is a TextArea -> We can get and set data from TextArea

scroll_text = scrolledtext.ScrolledText(window, width=60, height=10)
scroll_text.grid(column=0, row=0)

# scroll_text.get()
# scroll_text.setvar()

window.geometry("300x300")
window.mainloop()