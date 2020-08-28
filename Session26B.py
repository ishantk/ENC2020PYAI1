"""
    Operator Overloading in Python
    with magic functions/methods
"""

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show_point(self):
        print("Point is: {} | {}".format(self.x, self.y))

    def __str__(self):
        return "Point {} | {}".format(self.x, self.y)

    def add(self, point):
        temp = Point()
        temp.x = self.x + point.x
        temp.y = self.y + point.y
        return temp

    # Operator Overloading -> for + we have a customized __add__ function which adds the objects data
    # Overriding of magic method which works with operator
    def __add__(self, point):
        temp = Point()
        temp.x = self.x + point.x
        temp.y = self.y + point.y
        return temp

    # we can use almost all the operators on our objects as well
    # BUT, we need to override a corresponding magic method/function :)
    def __mul__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __floordiv__(self, other):
        pass

    def __cmp__(self, other):
        pass

    # Assignment:
    def __copy__(self): # SHALLOW COPY
        pass

    # Assignment:       # DEEP COPY
    def __deepcopy__(self, memodict={}):
        pass

def main():

    pRef1 = Point(10, 20)
    pRef2 = Point(30, 40)

    # pRef3 = pRef1.add(pRef2)
    pRef3 = pRef1 + pRef2 # => pRef3 = pRef1.__add__(pRef2)
    print(pRef1)
    print(pRef2)
    print(pRef3)


if __name__ == '__main__':
    main()