"""
    OOPS
    Use Case: OLA/Uber Ride Booking

    Requirement:
    Customer will book a Cab as a Ride by providing some data as input
    Nearest Driver will be linked to the Ride having a Cab upon Customer
    Customer has an Option to select from Multiple Cabs


    Lets write Objects for our above requirement:
    1. Customer: name, phone, email
    2. Driver  : IS-A Customer i.e. extension to Customer
               : license_number, driving_experience, is_available, distance

    3. Cab     : registration_number, base_fare, make, color
    4. OlaMini : IS-A Cab, final_fare
    5. OlaSedan: IS-A Cab, final_fare, wifi_name, wifi_password
    6. OlaBike : IS-A Cab, final_fare, is_helmet_available

    7. Ride:     rbn, customer, from_location, to_location
                 Has-A Relationship for customer, cab (driver)

"""

class Customer:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def show_customer(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("{} | {} | {}".format(self.name, self.phone, self.email))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

class Driver(Customer):

    def __init__(self, name, phone, email, license_number, driving_experience):
        self.name = name
        self.phone = phone
        self.email = email
        self.license_number = license_number
        self.driving_experience = driving_experience
        self.is_available = False
        self.distance = 0

    def show_driver(self):
        print("DRIVER DETAILS")
        Customer.show_customer(self)
        print("{} | {}".format(self.license_number, self.driving_experience))
        print("{} | {}".format(self.is_available, self.distance))
        print("----------------------------------------------------")

    # Controller Functions i.e. will hold some logic for us
    def accept_ride(self):
        print("You Got a New Ride !!")
        choice = input("Please Accept/Reject The Ride (yes/no)")

        # if choice == "yes":
        #     return True
        # else:
        #     return False

        return choice == "yes"


    def go_on_duty(self, enable):
        self.is_available = enable


class Cab:

    def __init__(self, registration_number, base_fare, make, color):
        self.registration_number = registration_number
        self.base_fare = base_fare
        self.make = make
        self.color = color

    def show_cab(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("{} | {}".format(self.registration_number, self.base_fare))
        print("{} | {}".format(self.make, self.color))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def attach_driver(self, driver):
        self.driver = driver


class OlaMini(Cab):
    def __init__(self, registration_number, base_fare, make, color):
        Cab.__init__(self, registration_number, base_fare, make, color)
        self.final_fare = base_fare + 50

    def show_ola_cab(self):
        print("CAB - OLA MINI DETAILS")
        Cab.show_cab(self)
        print("More Details: {}".format(self.final_fare))
        print("----------------------------------------------------")
        print()


class OlaSedan(Cab):
    def __init__(self, registration_number, base_fare, make, color,  wifi_name, wifi_password):
        Cab.__init__(self, registration_number, base_fare, make, color)
        self.final_fare = base_fare + 100
        self.wifi_name = wifi_name
        self.wifi_password = wifi_password

    def show_ola_cab(self):
        print("CAB - OLA SEDAN DETAILS")
        Cab.show_cab(self)
        print("More Details: {} | {} | {}".format(self.final_fare, self.wifi_name, self.wifi_password))
        print("----------------------------------------------------")
        print()


class OlaBike(Cab):
    def __init__(self, registration_number, base_fare, make, color, is_helmet_available):
        Cab.__init__(self, registration_number, base_fare, make, color)
        self.final_fare = base_fare + 20
        self.is_helmet_available = is_helmet_available

    def show_ola_cab(self):
        print("CAB - OLA BIKE DETAILS")
        Cab.show_cab(self)
        print("More Details: {} | {}".format(self.final_fare, self.is_helmet_available))
        print("----------------------------------------------------")
        print()


class Ride:

    def __init__(self, customer):
        ride_id = str(hex(id(self)))
        self.rbn = ride_id[2:].upper()
        self.customer = customer

    def enter_location(self):
        self.from_location = input("Enter Source Location")
        self.to_location = input("Enter Destination Location")

    def select_cab(self, cabs):

        print("1. Ola Mini")
        print("2. Ola Sedan")
        print("3. Ola Bike")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            self.cab = cabs[0] # Mini
        elif choice == 2:
            self.cab = cabs[1] # Sedan
        elif choice == 3:
            self.cab = cabs[2] # Bike


    def book_cab(self):
        print("Please Confirm Cab Booking ?")
        print("Route Details: {} - {}".format(self.from_location, self.to_location))
        print()
        self.cab.show_ola_cab()

        choice = input("Would You Like to book the Cab? (yes/no)")

        if choice == "yes":
            result = self.cab.driver.accept_ride()
            if result:
                self.customer.show_customer()
                print("Your Ride is Confirmed {}".format(self.rbn))
                self.cab.driver.show_driver()
            else:
                # recursive Logic to look for some other driver
                print("Looking for some other driver :(")

        else:
            print("Thank You !!")
            print("We would like to serve you whenever you need us !!")





def main():

    customer = Customer("John", "+91 99999 11111", "john@example.com")

    driver1 = Driver("Kim", "+91 98765 12345", "kim@example.com", "ABX123", 5)
    driver2 = Driver("Leo", "+91 90909 54331", "leo@example.com", "PPA331", 3)
    driver3 = Driver("Harry", "+91 80989 43561", "harry@example.com", "RTS232", 1)

    driver1.go_on_duty(True)
    driver2.go_on_duty(False)
    driver3.go_on_duty(True)

    # Hard-Coded Distance for Drivers
    driver1.distance = 1
    driver2.distance = 2
    driver3.distance = 3

    # Looking above, 2 drivers are available for the duty i.e. to be booked for some ride :)

    # customer.show_customer()

    print()

    # driver1.show_driver()
    # driver2.show_driver()
    # driver3.show_driver()


    print()

    cab1 = OlaMini("PB10AB1234", 100, "TATA", "White")
    cab2 = OlaSedan("PB10FG1010", 100, "Maruti", "Black", "OLAWifi", "ab34qw12")
    cab3 = OlaBike("PB10AB5431", 40, "Hero", "Black", True)

    # cab1.show_ola_cab()
    # cab2.show_ola_cab()
    # cab3.show_ola_cab()

    # Hard-Coded example, in real time it would be an algo to compute and link drivers accordingly
    cab1.attach_driver(driver1)
    cab2.attach_driver(driver2)
    cab3.attach_driver(driver3)

    # Must be sorted on the basis of distance for the driver :)
    #        0      1    2
    cabs = [cab1, cab2, cab3]

    rRef = Ride(customer)
    rRef.enter_location()
    rRef.select_cab(cabs)
    rRef.book_cab()


if __name__ == '__main__':
    main()
