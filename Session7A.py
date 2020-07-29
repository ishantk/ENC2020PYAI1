"""
    Value Vs Reference
    Value -> Passing a Single Value Container : eg int
"""

def square_of_number(number):
    print("number is:", number, hex(id(number)))
    number = number * number
    print("number now is:", number, hex(id(number)))


def main():
    num = 11    # we will have no impact on num in the main if something is modified in square_of_number
    print("num is:", num, hex(id(num)))
    square_of_number(num)
    print("num now is:", num, hex(id(num)))


# we must execute main, if we have created it
if __name__ == '__main__':
    main()