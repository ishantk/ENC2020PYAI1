"""
    Functions in Python
        Its a piece of logic written so that we can use it again and again
        Use Cases:
            1. Computing Taxes with some splits on some amounts at many places on eCommerce Platform
            2. calculation of discounts based on promo codes
            3. internet connectivity checks
            4. authenticating the user | register or login
            etc...

         Function is a piece of logic where we group multiple statements to solve our problem.
         this problem occurs multiple times

         Mathematically -> Function
         f(x) = x*x + 1

         f is name of function
         x is input
         x*x + 1 is its definition

         f(1) = 1*1 + 1 -> 2
         f(2) = 2*2 + 1 -> 5
         .
         ...
"""

# COVID CASES
# consider data for 5 states
data_july_27 = [12343, 14121, 2345, 13455, 45678]
data_july_28 = [22343, 18121, 52345, 33455, 49678]

ipl_team_points = [19, 20, 18, 16, 15, 22, 16]

print("Max cases on July 27:", max(data_july_27))
print("Max cases on July 28:", max(data_july_28))

"""
# Why we need Function ?
# Piece of logic may get repeated in our code to solve same or similar problem

max = data_july_27[0]

for i in range(1, len(data_july_27)):  # 0 to 4
    if data_july_27[i] > max:
        max = data_july_27[i]

print("Max is:", max)

max = data_july_28[0]

for i in range(1, len(data_july_28)):  # 0 to 4
    if data_july_28[i] > max:
        max = data_july_28[i]

print("Max is:", max)
"""

# Create a Function
# def creates a function with name max_cases
# () -> input list takes data as a variable input
def max_cases(data):
    max = data[0]

    for i in range(1, len(data)): # 0 to 4
        if data[i] > max:
            max = data[i]

    print("Max Cases for {} is {}".format(data, max))


# Function is Re-Defined: Previous definition is removed and new is created
# so use, different names :)
def max_in_range(data, point1, point2):
    max = data[0]

    for i in range(1, len(data)): # 0 to 4
        if data[i] > max:
            max = data[i]

    print("Max Cases for {} is {}".format(data, max))


# What function can do for us ?
# execution of Function by single line of code | Same Problem
max_cases(data_july_27)
max_cases(data_july_28)

max_cases(ipl_team_points)                      # Similar Problem

max_in_range(data_july_27, 1000, 30000)         # -> assignment







