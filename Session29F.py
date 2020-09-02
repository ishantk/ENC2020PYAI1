from tkinter import *
# from tkinter import Menu


window = Tk()
window.title("Auribises")

menu = Menu(window)

item = Menu(menu)
item.add_command(label="New")

item.add_separator()

item.add_command(label="Save")

menu.add_cascade(label="File", menu=item)

window.config(menu=menu)


# Explore how event handling can work with menus :)

window.geometry("300x300")
window.mainloop()