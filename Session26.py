"""
    Misc Concepts in Python
"""

# private and protected in Python
class Point:

    def __init__(self, x, y):
        self._x = x     # _x means protected -> x must not be accessed directly [warning] :)
        self.__y = y    # __y means private -> cannot be accessed [error] :)

    def show_point(self):
        print("Point is: {} | {}".format(self._x, self.__y))

    # We defined __dict__ in our class and now its kind of overriding :)
    # Hence, no one can access the data in our object now :)
    def __dict__(self):
        return None

def main():
    pRef = Point(10, 20)
    pRef.show_point()

    # Directly access x and y here from Point object referred by pRef
    # print("x in pRef is:", pRef._x)  # accessing a protected warning -> we try to tell developer dont use it directly, it is meant for some internal use
    # print("y in pRef is:", pRef.__y) # accessing private member y is error now

    # protected -> starts with _   -> accessible everywhere with a warning
    # private   -> starts with __  -> accessible within the class and not outside

    print(pRef.__dict__)
    # Output of above line: {'_x': 10, '_Point__y': 20}
    # _x remains same
    # BUT, __y is modified to _Point__y -> NAME MANGLING

    print("y in pRef is:", pRef._Point__y)

if __name__ == '__main__':
    main()