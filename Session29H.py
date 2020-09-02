from tkinter import *

window = Tk()
window.title("Auribises")

# relief -> flat, sunken, raised, groove and ridge

first_frame = Frame(relief="raised", borderwidth=4, bg="red")
second_frame = Frame(relief="ridge", borderwidth=4, bg="yellow")

# pack labels or other GUI widgets in Frames
label1 = Label(master=first_frame, text="This is in the First Frame")
label1.pack()

label2 = Label(master=second_frame, text="This is in the Second Frame")
label2.pack()

# pack frames in the window
second_frame.pack(side=LEFT)
first_frame.pack(side=LEFT)



window.geometry("300x300")
window.mainloop()
