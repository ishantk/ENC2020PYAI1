"""
    Functions in Python - Part II
"""

def show():
    print("This is show")


def add(num1, num2):
    sum = num1 + num2
    return sum


# we will get hashcodes in output
print("show is:", show, id(show), hex(id(show)))
print("add is:", add)

# reference copy
display = show
addition = add

print("display is:", display)
print("addition is:", addition)

# PS: show and add are references which holds hash codes to the functions

# Execution of Functions:
show()
display()

print("Sum of 10 and 20 is:", add(10, 20))
print("Sum of 11 and 22 is:", addition(11, 22))
