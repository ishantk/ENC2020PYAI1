"""
    Recursion in Functions
    To understand Function Execution Stack :)
"""

def printNumber(number):

    if number == 0:
        return                          # return nothing when number becomes 0
    else:
        printNumber(number-1)           # Recursion: executing a function from a function | Kind of an infinite loop

    print("number is:", number)


def main():
    print("main started")
    printNumber(5)
    print("main finished")

if __name__ == '__main__':
    main()

# assignment -> print the numbers from 5 to 1

print()

for i in range(1, 6):
    print("number is:", i)