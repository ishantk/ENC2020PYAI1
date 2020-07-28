# Mathematical Functions:
# f(x) = x*x + 1
# exp(x) = 2 power x
# add(x, y) = x+y

# creation of function
def f(x):
    result = x*x + 1
    print("Result from f is:", result)

def exp(x):
    result = 2**x
    print("Result from exp is:", result)

def add(x, y):
    result = x+y
    print("Result from add is:", result)

# In functions we can use return statement
# it is the last statement i.e. any statement below it wont be executed in function
def square_of_number(number):
    return number*number
    print("This is Awesome") # will not be executed


# execution of function
f(1)
f(2)
f(3)

exp(2)
exp(4)
exp(8)

add(10, 20)
add(11, 19)
add(-11, 19)
add(11, -19)

# Here, square_of_number functions acknowledge us back with some data :)
result = square_of_number(5)
print("result returned from square_of_number is:", result)

# FAQ: should we create a function with return or without return. what is preferable ?
#      this is totally dependent on the use case of the problem
#      example: max function should acknowledge us with max number
#               evaluation of marks for a student towards grading -> we can show the results instead returning grade

#      we return form function when the returned data is suppose to be further processed
#      i.e. we may do some computations on it :)

def apply_promo_code(amount, promo_code):

    if promo_code == "ZOMATO":
        return 0.40*amount
    elif promo_code == "BINGO":
        return 0.50*amount
    else:
        return 0.10*amount

    print("This is Awesome") # this will not be executed | Not Reachable Code


result1 = apply_promo_code(5000, "ZOMATO")
result2 = apply_promo_code(5000, "BINGO")

if result1 > result2:
    print("I will Use ZOMATO")
else:
    print("I will Use BINGO")
