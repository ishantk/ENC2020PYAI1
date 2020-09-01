from tkinter import *
from Session28B import *

class CustomerManagementApp:

    def __init__(self):
        self.db = DB(collection="customers")

    def on_click(self):
        customer = {'name': self.entry_name.get(),
                    'phone': self.entry_phone.get(),
                    'email': self.entry_email.get()
                    }
        print(customer)
        self.db.add_customer(customer)


    def run_app(self):

        window = Tk()
        print(window, type(window))

        lbl_title = Label(window, text="Customer Management System")
        lbl_title.pack()  # add the Label in window nd pack it to take some optimal space


        self.btn_add = Button(window, text="Add Customer",
                         command=self.add_customer_gui)  # command here is taking reference of some function
        self.btn_add.pack()

        self.btn_delete = Button(window, text="Delete Customer",
                              command=self.add_customer_gui)  # command here is taking reference of some function
        self.btn_delete.pack()

        self.btn_update = Button(window, text="Update Customer",
                              command=self.add_customer_gui)  # command here is taking reference of some function
        self.btn_update.pack()

        self.btn_fetch = Button(window, text="Fetch Customers",
                              command=self.add_customer_gui)  # command here is taking reference of some function
        self.btn_fetch.pack()

        window.mainloop()


    def add_customer_gui(self):
        window = Tk()
        print(window, type(window))

        lbl_title = Label(window, text="Customer Management System")
        lbl_title.pack()  # add the Label in window nd pack it to take some optimal space

        lbl_name = Label(window, text="Enter Customer Name")
        lbl_name.pack()

        self.entry_name = Entry(window)
        self.entry_name.pack()

        lbl_phone = Label(window, text="Enter Customer Phone")
        lbl_phone.pack()

        self.entry_phone = Entry(window)
        self.entry_phone.pack()

        lbl_email = Label(window, text="Enter Customer Email")
        lbl_email.pack()

        self.entry_email = Entry(window)
        self.entry_email.pack()

        self.btn_add = Button(window, text="Add Customer",
                              command=self.on_click)  # command here is taking reference of some function
        self.btn_add.pack()

        window.mainloop()


def main():
    app = CustomerManagementApp()
    app.run_app()

if __name__ == '__main__':
    main()

# Assignment:
# Implement Delete, Update and Fetch Customer Buttons
# for fetching and displaying the data on GUI explore UI Objects -> List, DataTable and TreeView
