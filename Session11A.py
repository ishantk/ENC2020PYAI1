# Standardization of Objects with Constructor
# i.e. we have the same attributes and same default data for all Objects, Initially :)
# but data can be updated later as per user's preferences

class OneWayFlightBooking:

    # __init__ is known as constructor, executed automatically whenever object ic constructed in the memory
    # self -> is the 1st input to any function which you create inside the class
    # self can be any name
    # self is a reference variable which holds the hashcode of the object which is in use
    def __init__(self):
        print("init executed and self is:", self)
        self.from_location = "Delhi"
        self.to_location = "Bangalore"
        self.departure_date = "6th Aug, 2020"
        self.travllers = 1
        self.travel_class = "economy"



def main():
    oRef1 = OneWayFlightBooking()
    oRef1.departure_date = "10th Aug, 2020"
    print("oRef1 is:", oRef1)
    print("oRef1 Object's Data is:", oRef1.__dict__)

    print()

    oRef2 = OneWayFlightBooking()
    oRef2.travllers = 4
    oRef2.travel_class = "business"
    print("oRef2 is:", oRef2)
    print("oRef2 Object's Data is:", oRef2.__dict__)

if __name__ == '__main__':
    main()