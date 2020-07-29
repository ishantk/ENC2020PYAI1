"""
    Inputs to Function
"""

def add(num1, num2):
    num1 += 10
    num2 += 20

    sum = num1 + num2

    print("sum of num1:{} and num2:{} is {}".format(num1, num2, sum))


# add(11, 21)
# Named inputs during execution
add(num1=11, num2=21)  # specify inputs by name
add(num2=30, num1=70)  # specify inputs by name

def add_numbers(num1, num2):
    print("Sum is:", (num1+num2))

print(add_numbers)

# re-defining means function will be a new function
# and ref var add_numbers shall now point to it

def add_numbers(num1, num2, num3):
    print("Sum is:", (num1+num2+num3))

print(add_numbers)


# add_numbers(10, 20) # Error
add_numbers(10, 20, 30)
