"""
    Modules
    Lambdas
    Maps
    Filters
"""

print("Welcome to Session19")
print("Session 19 name is: ", __name__)

def fun():
    print("This is fun in Session19")


class CA:
    def __init__(self):
        print("CA Object Constructed in Session19")


def main():
    print("This is main in Session19")
    fun()
    cRef = CA()


if __name__ == '__main__':
    main()