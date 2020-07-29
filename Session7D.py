# *args -> variable arguments
# *anyName -> args can be any name of your choice
# *args is basically a tuple
def add_numbers(*args):
    print(args)
    print(type(args))

    sum = 0
    for i in range(len(args)):
        sum += args[i]

    print("Sum is:", sum)
    print()


add_numbers(10, 20, 30)
add_numbers(10, 20, 30, 40, 50)
add_numbers(10, 20, 30, 40, 50, 60, 70, 80, 90)