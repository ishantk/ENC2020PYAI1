# Customer Management Solution | COVID-19 Based
# Register the Customer who so ever enters in the store

# Customer : name, phone, email, temperature, intime, outtime

import mysql.connector as db
import datetime

"""
    SQL:
    create table Customer(
       cid int primary key auto_increment, 
       name varchar(256),
       phone varchar(10) unique,
       email varchar(256),
       temperature float, 
       intime varchar(256),
       outime varchar(256)
    )

"""

class Customer:

    def __init__(self):
        self.name = input("Enter Customer Name: ")
        self.phone = input("Enter Customer Phone: ")
        self.email = input("Enter Customer Email: ")
        self.temperature = input("Enter Customer Temperature: ")
        self.intime = str(datetime.datetime.today())
        self.outtime = ""

    def show_Customer(self):
        print("Customer Details:")
        print("-----------------")
        print("{} | {} | {}".format(self.name, self.phone, self.email))
        print("{} | {} | {}".format(self.temperature, self.intime, self.outtime))
        print("-----------------")


class DB:

    def __init__(self):
        self.connection = db.connect(user="root", password="", database="auridb", host="127.0.0.1", port="3306")
        self.cursor = self.connection.cursor()
        print("Connection Created and Cursor Obtained")


    def execute_sql_write_operation(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()
        print("SQL Command Executed")

    def execute_sql_read_operation(self, sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data


def covid_19_cms_app():

    # today = str(datetime.datetime.today())
    # print(today, type(today))

    while True:

        print("===============================")
        print("Welcome to Customer Management")
        print("In COVID-19 You must record your customer details")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Press 1 to Register Customer and Mark Entry")
        print("Press 2 to Mark Exit of Customer")
        print("Press 3 to Update Customer")
        print("Press 4 to Fetch Customer on the basis of Phone Number")
        print("Press 5 to Fetch All Customers")
        print("Press 6 to Delete the Customer on the basis of Phone Number")
        print("Press 0 to Quit :)")
        print("===============================")

        choice = int(input("Enter Your Choice:  "))

        if choice == 0:
            print("Thank You For Using CMS")
            break

        dbRef = DB()

        if choice == 1:
            cRef = Customer()
            cRef.show_Customer()

            save = input("Enter yes to Save: ")
            if save == "yes":
                sql = "insert into Customer values(null, '{}', '{}', '{}', {}, '{}', '{}')"\
                    .format(cRef.name, cRef.phone, cRef.email, cRef.temperature, cRef.intime, cRef.outtime)
                dbRef.execute_sql_write_operation(sql)

        elif choice == 2:
            phone = input("Enter Customer Phone: ")
            outtime = str(datetime.datetime.today())

            update = input("Enter yes to Save: ")
            if update == "yes":
                sql = "update Customer set outime = '{}' where phone = '{}'".format(outtime, phone)
                dbRef.execute_sql_write_operation(sql)

        elif choice == 3:
            cRef = Customer()
            cRef.show_Customer()

            update = input("Enter yes to Save: ")
            if update == "yes":
               sql = "update customer set .... where phone='{}'"
               # implement update operation

        elif choice == 4:
            phone = input("Enter Customer Phone: ")
            sql = "select * from Customer where phone = '{}'".format(phone)
            data = dbRef.execute_sql_read_operation(sql)
            print(data)

        elif choice == 5:
            sql = "select * from Customer"
            data = dbRef.execute_sql_read_operation(sql)
            # print(data)

            for row in data:
                print(row)

        elif choice == 6:
            phone = input("Enter Customer Phone: ")
            delete = input("Enter yes to delete")

            if delete == "yes":
                sql = "delete from Customer where phone = '{}'".format(phone)
                dbRef.execute_sql_write_operation(sql)

# SQL: has built in functions, count, max, min, avg :) Explore them

if __name__ == '__main__':
    covid_19_cms_app()


# Assignment
# Stats as Conclusions:
# 1. How many customers were having a high grade (>100) fever and they entered our store
# 2. for any customer if we enter phone number, we must be able to see time spent in the store
# 3. What is the average time spent inside the store of customers
#    we need to find time difference first and than process the data :)
# 4. How many customers entered in the store day wise. We can enter todays date and should come to know the number of customers entered on that day :)

# You may need to explore more of SQL Commands :)
