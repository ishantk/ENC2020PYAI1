"""
    Magic Methods In Python
    kind of format -> __abc__
"""

# private and protected in Python
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show_point(self):
        print("Point is: {} | {}".format(self.x, self.y))

    # We defined __dict__ in our class and now its kind of overriding :)
    # Hence, no one can access the data in our object now :)
    def __dict__(self):
        return None

    # Override the String function so as printing of reference or getting the data as string is now not the HashCode
    # Now our customized string will be returned rather than hashcodes if we either print the reference or use str or __str__
    def __str__(self):
        return "Point {} | {}".format(self.x, self.y)

def main():
    pRef = Point(10, 20)
    pRef.show_point()

    print(pRef.__dict__)

    print(pRef)             # here automatically __str__() is executed and hence it shows the hashcodes
    print(pRef.__str__())

    point_as_string = str(pRef)
    print(point_as_string)


if __name__ == '__main__':
    main()