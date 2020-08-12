"""
    Install mysql-connector
    1. From Settings
    OR
    2. From Terminal: pip install mysql-connector

"""

import mysql.connector as db

# mysql.connector will give us some built in functions for us to use
# these all built in codes are known as API's for us
# API: Application Programming Interfaces

def main():

    # Step1: Write SQL Query
    state = input("Enter State: ")
    active = int(input("Enter active Cases: "))
    confirmed = int(input("Enter confirmed Cases: "))
    recovered = int(input("Enter recovered Cases: "))
    deceased = int(input("Enter deceased Cases: "))
    tested = int(input("Enter tested Cases: "))

    sql = "insert into CovidIndia values('{}', {}, {}, {}, {}, {})".format(state, active, confirmed, recovered, deceased, tested)
    print("SQL Query Is:", sql)

    # Step2: Create Connection to the DataBase
    # 127.0.0.1 is localhost
    # 3306 is port number where db is running (XAMPP Control Panel will show this)
    connection = db.connect(user="root", password="", database="auridb", host="127.0.0.1", port="3306")
    print("Connection Created")

    # Step3: Execute SQL Statement
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit() # To ensure SQL will be executed over the connection

    print("SQL Statement Executed :)")

if __name__ == '__main__':
    main()