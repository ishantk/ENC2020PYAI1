"""
    Inheritance
    Polymorphism -> ref can be either Customer or PrimeCustomer Object
    Use Case: Amazon Prime :)
"""

class Customer:

    def __init__(self):
        self.name = input("Enter Your Name: ")
        self.phone = input("Enter Your Phone: ")
        self.email = input("Enter Your Email: ")

    def show_customer_details(self):
        print("Customer Details:")
        print("{} | {} | {}".format(self.name, self.phone, self.email))


class PrimeCustomer(Customer): # IS-A Relationship | Inheritance
    def __init__(self):
        Customer.__init__(self)
        self.prime = True
        self.video = True
        self.music = True
        self.valid_till = "15th Aug, 2021"

    def upgrade_to_prime(self):
        self.prime = True
        self.video = True
        self.music = True
        self.valid_till = "15th Sep, 2020"

    def show_customer_details(self):
        Customer.show_customer_details(self)
        print("Prime Details:")
        print("Video {} | Music {} | Validity {}".format(self.video, self.music, self.valid_till))


def main():

    print("New User? Sign Up")
    print("1. Regular Signup")
    print("2. Prime Customer Signup")


    choice = int(input("Enter Your Choice: "))

    ref = None
    flag = 0

    # Polymorphism: ref can either point to Customer object or PrimeCustomer Object
    if choice == 1:
        ref = Customer()
        prime_choice = input("Would you like to try Prime for a Month free of Cost ? (yes/no)")
        if prime_choice == "yes":
            flag = 1
            PrimeCustomer.upgrade_to_prime(ref)
            print("Customer Upgraded to Prime")

    else:
        ref = PrimeCustomer()

    # The same function will execute and show details accordingly
    # print("Dictionary:", ref.__dict__)

    if flag != 1:
        ref.show_customer_details()
    else:
        PrimeCustomer.show_customer_details(ref)

if __name__ == '__main__':
    main()


# Assignment: When we go to McDonalds, we order a Burger and staff asks us to upgrade your burger to a meal :)
#              implement the above program in McDonalds Use Case :)