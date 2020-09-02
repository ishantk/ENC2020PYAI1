from tkinter import *
from tkinter import filedialog

def on_click():
   file = filedialog.askopenfilename()
   print(file)

window = Tk()
window.title("Auribises")

# ScrolledText is a TextArea -> We can get and set data from TextArea

btn_submit = Button(window, text="Select File", command=on_click)

btn_submit.grid(column=0, row=0)

window.geometry("300x300")
window.mainloop()