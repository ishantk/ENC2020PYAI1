# default arguments in a function
# i.e. inputs with some default values for the case when user will not pass any input for the same

def add(num1, num2, num3=0):
    sum = num1 + num2 + num3
    print("sum is:", sum)


add(10, 20, 30)
add(num3=101, num1=40, num2=10)

add(10, 20)

# error: we cannot give default value in between
# def add(num1, num2=0, num3):
#     pass # no function definition yet

# error: we cannot give default value from left
# def add(num1=0, num2, num3):
#     pass

# Rule -> PS: default arguments must start from RHS
def add(num1, num2=1, num3=0): # OK
    pass