"""
    Surprise Surprise Surprise :)

    Hackathon
    Live Online Coding

    Go to repl.it
    Share link of file in which you are working on the chat and whatsapp group

    Problem Statement:
    Garbage Collection Management
    > Console Based Software

    Their are 5 different plot sizes from 100 sq yards to 500 sq yards
    which a customer owns

    1. Create a Class Property(housenum, block, street, area, size) with address and size details
    2. Create a Class Customer(name, phone, email, property) with details
    3. Link Customer and Property
       1 Customer can have 1 Property :)
    4. Create a Class Fee(phone, month, year, amount) which manages Fee for Garbage Collection every month
       Fee has to be saved in the file

    Problem Statement for Algorithmic Approach:
        A customer paid in th month of Aug i.e. 8
        9876512345, 8, 2020, 250
        9876512345, 9, 2020, 0
        9876512345, 10, 2020, 0
        9876512345, 11, 2020, 250+(500 + 0.30*500)
        Now he kipped 2 months and he has to pay in November month
        So, take the difference and calculate the bill accordingly

        A fine for 30% of the amount paid to be imposed for the non paid months

"""

# Fee for Different Sizes of Property
# Price Listing for GCM
fee_structure = {
    "100": 100,
    "200": 150,
    "300": 200,
    "400": 250,
    "500": 300
}

class Property:

    def __init__(self, houseNum=None, block=None, street=None, area=None, size=None):
        self.houseNum = houseNum
        self.block = block
        self.street = street
        self.area = area
        self.size = size

    def inputPropertyDetails(self):
        self.houseNum = input("Enter House Num: ")
        self.block = input("Enter House Block: ")
        self.street = input("Enter House Street: ")
        self.area = input("Enter House Area: ")
        self.size = int(input("Enter House Size: "))

    def showProperty(self):
        print("{} | {} | {} | {} | {}".format(self.houseNum, self.block, self.street, self.area, self.size))

    def toCSV(self):
        return "{},{},{},{},{}".format(self.houseNum, self.block, self.street, self.area, self.size)

class Customer:

    def __init__(self, name=None, phone=None, email=None, property=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.property = property # Has-A Relationship

    def inputCustomerDetails(self):
        self.name = input("Enter Customer Name: ")
        self.phone = input("Enter Customer Phone: ")
        self.email = input("Enter Customer Email: ")

    # Has-A Relationship
    def linkPropertyToCustomer(self, property):
        self.property = property

    def showCustomer(self):
        print("{} | {} | {}".format(self.name, self.phone, self.email))
        self.property.showProperty()

    def toCSV(self):
        return "{},{},{},{}\n".format(self.name, self.phone, self.email, self.property.toCSV())


class Fee:

    def __init__(self, phone=None, month=None, year=None, amount=None):
        self.phone = phone
        self.month = month
        self.year = year
        self.amount = amount

    def showFee(self):
        print("{} | {} | {} | {}".format(self.phone, self.month, self.year, self.amount))

    def toCSV(self):
        return "{},{},{},{}\n".format(self.phone, self.month, self.year, self.amount)

    # Fetching Fee Paid in the Last Month
    # manually create gc-fees.csv in your project
    def getLastFeePaidMonth(self):
        file = open("gc-fees.csv", "r")
        lines = file.readlines()

        lastFeeLine = None


        # Time Complexity - O(n)
        for line in lines:
            data = line.split(",")
            if data[0] == self.phone:
                lastFeeLine = line

        if lastFeeLine == None:
            return -1
        else:
            data = lastFeeLine.split(",")
            month = int(data[1])
            year = int(data[2]) # use year variable to get the exact difference in months
            return month

    def inputFeeDetails(self):
        self.phone = input("Enter Customer Phone: ")
        self.month = int(input("Enter Month: "))
        self.year = int(input("Enter Year: "))

        # Amount must be fetched automatically
        file = open("gc-customers.csv", "r")
        lines = file.readlines()

        is_registered = False

        # Implement Linear Search on List
        for line in lines:
            data = line.split(",")
            if data[1] == self.phone:
                is_registered = True
                size = data[len(data)-1].strip()
                self.amount = fee_structure[size]
                break

        if is_registered:
            print("Processing Garbage Fee for Customer")
        else:
            print("Customer Not Registered")

        # Check if fee was paid in the last month by the customer
        lastMonth = self.getLastFeePaidMonth()

        if lastMonth == -1:
            print(">> Fee to be Paid on {} month {} year : \u20b9{}".format(self.month, self.year, self.amount))
        else:
            difference = self.month - lastMonth
            if difference == 1:
                print(">> Fee to be Paid on {} month {} year : \u20b9{}".format(self.month, self.year, self.amount))
            else:
                difference -= 1
                pending_fee = difference * self.amount
                fine = 0.30 * pending_fee
                self.amount += fine + pending_fee
                print(">> Fee Not Paid for {} months and pending fee is: {} and fine is: {}".format(difference, pending_fee, fine))

def main():

    print("===Garbage Collector App===")

    print("1. Add Customer")
    print("2. Charge Garbage Fee")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:

        # Get the Property Details of the Customer
        property = Property()
        property.inputPropertyDetails()

        # Getting Customer Details
        customer = Customer()
        customer.inputCustomerDetails()

        # Link Property with Customer Object
        customer.linkPropertyToCustomer(property)

        customer.showCustomer()

        # Fetched CSV Data from Customer Object which will also give us the property data
        data = customer.toCSV()
        print(data)

        save = input("Would you like to save {} (yes/no)".format(customer.name))
        if save == "yes":
            file = open("gc-customers.csv", "a")
            file.write(data)
            file.close()
            print(">> Customer Saved in File")

    elif choice == 2:

        fee = Fee()
        fee.inputFeeDetails()
        fee.showFee()

        data = fee.toCSV()

        save = input("Would you like to save Fee {} for {} (yes/no)".format(fee.amount, fee.phone))
        if save == "yes":
            file = open("gc-fees.csv", "a")
            file.write(data)
            file.close()
            print(">> Fee Saved in File")

    else:
        print(">> Select Valid Choice")

if __name__ == '__main__':
  main()


# Assignment:
# check for the year and month                  max 30 mins task
# replicate the same program with MONGO DB :)   max 2 hours task

# Screen Shots / Video Recordings :)