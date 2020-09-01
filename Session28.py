"""
    GUI tkinter
    DataBase Connectivity with GUI
    Project Task - I
        COVID Bed Management for Hospitals
            1. Generate Requirements -> write SRS [Submit It]
            2. After SRS is approved -> Use tkinter and MongoDB to develop the project
            3. Timeline: 5 days
            4. An explainer video of your code and working project wih mongo db [Share the Video Link]



    Reference Link: https://docs.python.org/3/library/tk.html

"""



from tkinter import *


def on_click():



    customer = {'name': entry_name.get(),
                'phone': entry_phone.get(),
                'email': entry_email.get()
                }
    print(customer)


# GUI Window which we are creating
window = Tk()
print(window, type(window))

lbl_title = Label(window, text="Customer Management System")
lbl_title.pack() # add the Label in window nd pack it to take some optimal space

lbl_name = Label(window, text="Enter Customer Name")
lbl_name.pack()

entry_name = Entry(window)
entry_name.pack()

lbl_phone = Label(window, text="Enter Customer Phone")
lbl_phone.pack()

entry_phone = Entry(window)
entry_phone.pack()

lbl_email = Label(window, text="Enter Customer Email")
lbl_email.pack()

entry_email = Entry(window)
entry_email.pack()

btn_add = Button(window, text="Add Customer", command=on_click) # command here is taking reference of some function
btn_add.pack()



window.mainloop()