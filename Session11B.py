# Standardization of Objects with Constructor
# i.e. we have the same attributes and same default data for all Objects, Initially :)
# but data can be updated later as per user's preferences

class OneWayFlightBooking:

    """
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
    """

    # here, old init function i.e. constructior will be destroyed and new init will be considered
    # hence, above written init will be of no use
    # finally, we can have only 1 single constructor in our class
    def __init__(self, from_location, to_location, departure_date, travllers, travel_class):
        print("init with inputs executed and self is:", self)
        self.from_location = from_location
        self.to_location = to_location
        self.departure_date = departure_date
        self.travllers = travllers
        self.travel_class = travel_class

    # we cannot re-define constructors in class with different inputs i.e. overloading not supported

    # we can also create functions in class for our display/logical part
    # for any function created in class, self will be the 1st input
    def show_details(self):
        print("Travel Details: From {} To {} On {} for {} traveller in {} class".format(self.from_location, self.to_location,
                                                                                    self.departure_date, self.travllers, self.travel_class))


def main():

    oRef1 = OneWayFlightBooking("Delhi", "Bangalore", "10th Aug, 2020", 2, "economy")
    oRef1.departure_date = "15th Aug, 2020"
    print("oRef1 is:", oRef1)
    print("oRef1 Object's Data is:", oRef1.__dict__)

    print()

    oRef2 = OneWayFlightBooking("Delhi", "Goa", "12th Aug, 2020", 2, "economy")
    oRef2.travllers = 4
    oRef2.travel_class = "business"
    print("oRef2 is:", oRef2)
    print("oRef2 Object's Data is:", oRef2.__dict__)

    print()

    oRef1.show_details()    # automatically in the background translated to  ->  OneWayFlightBooking.show_details(oRef1)
    oRef2.show_details()

    # printing the data in class, we will see some built ins and the functions i.e. init and show_details created by us
    print("Class Details:", OneWayFlightBooking.__dict__)

    # PS:
    # Object shall contain data
    # Class shall contain functions or may be data as well

    print()

    OneWayFlightBooking.show_details(oRef1)
    OneWayFlightBooking.show_details(oRef2)

if __name__ == '__main__':
    main()