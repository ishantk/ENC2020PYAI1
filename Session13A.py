"""
    Inheritance
        What is Inheritance ?
            Its a relationship between 2 types
            Rule: Whatever is in the Parent is accessible by Child, if not available with Child
        Why we need Inheritance ?
            If we closely observe the Rule of Inheritance, we can re-use the Code
            We will observe in the below program we have to write similar code again and again :(
            With Inheritance, we can re-use the repeated code :)
"""


"""
class OneWayFlightBooking:

    def __init__(self, from_location, to_location, departure_date, travllers, travel_class):
        print("OneWayFlightBooking Constructor Executed")
        self.from_location = from_location
        self.to_location = to_location
        self.departure_date = departure_date
        self.travllers = travllers
        self.travel_class = travel_class

    def show_details(self):
        print("[ONE WAY FLIGHT] Travel Details: From {} To {} On {} for {} traveller in {} class".format(self.from_location, self.to_location,
                                                                                    self.departure_date, self.travllers, self.travel_class))


class ReturnFlightBooking:

    def __init__(self, from_location, to_location, departure_date, return_date, travllers, travel_class):
        print("ReturnFlightBooking Constructor Executed")
        self.from_location = from_location
        self.to_location = to_location
        self.departure_date = departure_date
        self.travllers = travllers
        self.travel_class = travel_class
        self.return_date = return_date

    def show_details(self):
        print("[ROUND TRIP FLIGHT] Travel Details: From {} To {} On {} for {} traveller in {} class".format(self.from_location, self.to_location,
                                                                                    self.departure_date, self.travllers, self.travel_class))
        print("Return Date:", self.return_date)


class OutStationOneWayCab:
    def __init__(self, from_location, to_location, departure_date, departure_time):
        print("OutStationOneWayCab Constructor Executed")
        self.from_location = from_location
        self.to_location = to_location
        self.departure_date = departure_date
        self.departure_time = departure_time

    def show_details(self):
        print("[CAB] Travel Details: From {} To {} On {} at {}".format(self.from_location, self.to_location,
                                                                                    self.departure_date, self.departure_time))
"""


class Booking:

    def __init__(self, from_location, to_location, departure_date):
        print("Booking Constructor Executed")
        self.from_location = from_location
        self.to_location = to_location
        self.departure_date = departure_date


    def show_details(self):
        print("[BOOKING DETAILS] From {} To {} On {}".format(self.from_location, self.to_location, self.departure_date))


class OneWayFlightBooking(Booking): # Parent Child Relationship

    def __init__(self, from_location, to_location, departure_date, travllers, travel_class):
        Booking.__init__(self, from_location, to_location, departure_date)  # Re-Use Parent's Constructor to get 3 attributes created in Child Object

        # Child will write its own additional attributes :)
        print("OneWayFlightBooking Constructor Executed")
        self.travllers = travllers
        self.travel_class = travel_class

    def show_details(self):
        Booking.show_details(self)# To display, let Parent's function show the partial details
        # Child displays its own extended details
        print("[ONE WAY FLIGHT] for {} travellers in {} class".format(self.travllers, self.travel_class))


class ReturnFlightBooking(Booking):

    def __init__(self, from_location, to_location, departure_date, return_date, travllers, travel_class):

        Booking.__init__(self, from_location, to_location, departure_date)

        print("ReturnFlightBooking Constructor Executed")
        self.travllers = travllers
        self.travel_class = travel_class
        self.return_date = return_date

    def show_details(self):
        Booking.show_details(self)
        print("[RETURN FLIGHT] for {} travellers in {} class".format(self.travllers, self.travel_class))
        print("[RETURN FLIGHT] Return Date:".format(self.return_date))


class OutStationOneWayCab(Booking):
    def __init__(self, from_location, to_location, departure_date, departure_time):
        Booking.__init__(self, from_location, to_location, departure_date)
        print("OutStationOneWayCab Constructor Executed")
        self.departure_time = departure_time

    def show_details(self):
        Booking.show_details(self)
        print("[CAB] Pick Up Time".format(self.departure_date))


def main():
    oRef = OneWayFlightBooking("Delhi", "Bangalore", "10th Aug, 2020", 4, "economy")
    oRef.show_details()

    print()

    rRef = ReturnFlightBooking("Delhi", "Goa", "12th Aug, 2020", "20th Aug, 2020", 4, "economy")
    rRef.show_details()

    print()
    osRef = OutStationOneWayCab("Delhi", "Agra", "15th Aug, 2020", "12:45")
    osRef.show_details()


if __name__ == '__main__':
    main()