"""
    When we execute functions,
    in the memory we have function frames stacked up : PUSH (add the frame in Stack)
                                                       POP  (remove the frame from stack)
"""


def add(num1, num2):
    print("add started")
    sum = num1 + num2
    print("sum of {} and {} is {}".format(num1, num2, sum))
    print("add finished")

# quite resembling the other programming languages| java, c++, c, dart etc...
# main means starting of the program i.e. execution begins from the main
# In python by default whatever you write is executed and is considered to be in the main
def main():
    print("main started")

    # number and name are created in the main and are the property of main
    number = 10
    quote = "When we have Dark, look at Stars"

    add(10, 20)

    print("main finished")


# number wont be accessible outside the main :)
# print("number is:", number) # Error


# as a developer if i need main in my python program
# we need to check the name and execute it ourselves
if __name__ == '__main__':
    main()