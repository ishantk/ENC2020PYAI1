"""
    OOPS in Python
    Object
    Class

    For storing the data we have containers
    single value containers     eg: int
    multiple value containers   eg: list | Data Structures
        tuple, list, set, dictionary, string

        We have more other ways to structure data and we can innovate the ways as well
        so we cannot be limited in structuring the data only within given structures

        For customizations and other ways to look on your data is achieved through object

        OBJECT: is a multi value container, just like dictionary
        attribute: data just like key: value in dictionary

        Object is quite closer to the dictionary.
        So that we can write our own functions and may work in creating some customized data structure

    class is majorly to define the type of storage container
    limiting our object to use the features available in that class

    classes are used to make or define the object structure i.e. what it will have/hold


    Principle of OOPS:
        1. Think of an Object
            Object will attributes i.e. features w.r.t. it

            Object      : OneWayFlightBooking
            Attributes  : from_location, to_location, departure_date, travellers, travel_class

        2. Create the Class i.e. Type of Object

        3. From the Class create Real Object in Memory

    Pillars of OOPS:
    1. Encapsulation
    2. Inheritance
    3. Abstraction
    4. Polymorphism

    PS: We have design Patterns, which shall solve problems and they are written with the help OOPS Pillars
        Reactive Programming

"""

one_way_flight_booking = {
    "from_location": "Delhi",
    "to_location": "Bangalore",
    "departure_date": "6th Aug, 2020",
    "travellers": 2,
    "travel_class": "economy"
}

print(one_way_flight_booking, type(one_way_flight_booking))


#  2. Create the Class i.e. Type of Object
class OneWayFlightBooking:
    pass

def main():

    # 3. From the Class create Real Object in Memory
    oRef1 = OneWayFlightBooking()
    oRef2 = OneWayFlightBooking()
    oRef3 = oRef1       # Reference Copy


    print("oRef1 is:", oRef1, type(oRef1))
    print("oRef1 Object Contains:", oRef1.__dict__) # {} -> empty dictionary
    # __dict__ -> shall give the data within the object as dictionary :)

    print()

    print("oRef2 is:", oRef2, type(oRef2))
    print("oRef2 Object Contains:", oRef1.__dict__)  # {} -> empty dictionary

    print()

    print("oRef3 is:", oRef3, type(oRef3))
    print("oRef3 Object Contains:", oRef1.__dict__)  # {} -> empty dictionary

    print()

    # operations on object
    # 1. add/update data in object
    oRef1.from_location = "Delhi"
    oRef3.to_location = "Bangalore"
    oRef1.departure_date = "6th Aug, 2020"
    oRef3.travellers = 4
    oRef1.travel_class = "economy"

    # updating the data in Object
    oRef3.departure_date = "15th Aug, 2020"

    oRef2.from_location = "Delhi"
    oRef2.to_location = "Goa"
    oRef2.departure_date = "10th Aug, 2020"
    oRef2.travellers = 2
    oRef2.travel_class = "business"

    oRef2.kids = 1
    oRef2.kids_age = 2

    print("oRef1 Object Contains:", oRef1.__dict__)
    print("oRef2 Object Contains:", oRef2.__dict__)
    print("oRef3 Object Contains:", oRef3.__dict__)

    # PS: Different objetcs of same type i.e. class can contain different data as well :)

    # delete operation
    del oRef1.travel_class
    del oRef2.kids_age

    print()

    # reading the data in object
    print("oRef1 Object Contains:", oRef1.__dict__)
    print("oRef2 Object Contains:", oRef2.__dict__)
    print("oRef3 Object Contains:", oRef3.__dict__)

    # Decorated Printing
    print("Travel Details From {} to {} on {} for {} passengers".format(oRef1.from_location, oRef1.to_location, oRef1.departure_date, oRef3.travellers))
    print("Travel Details From {} to {} on {} for {} passengers".format(oRef2.from_location, oRef2.to_location,
                                                                        oRef2.departure_date, oRef2.travellers))


if __name__ == '__main__':
    main()