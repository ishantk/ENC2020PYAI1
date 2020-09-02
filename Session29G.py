from tkinter import *

window = Tk()
window.title("Auribises")

first_frame = Frame()
second_frame = Frame()

# pack labels or other GUI widgets in Frames
label1 = Label(master=first_frame, text="This is in the First Frame")
label1.pack()

label2 = Label(master=second_frame, text="This is in the Second Frame")
label2.pack()

# pack frames in the window
second_frame.pack()
first_frame.pack()



window.geometry("300x300")
window.mainloop()
