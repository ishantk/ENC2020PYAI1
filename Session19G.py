def discount(amount):
    return amount - 0.20*amount

discount_lambda = lambda amount : amount - 0.20*amount

# Exploratory Task: why we should or why we should not prefer lambdas over the functions :)

product_prices = [1234, 3452, 5443, 3255, 8788, 5323]
for price in product_prices:
    print("Original Price:", price)
    # print("Discounted Price:", discount(price))
    print("Discounted Price:", discount_lambda(price))
    print()

# map function -> a built in function in python

# result = map(discount, product_prices)
# result = map(discount_lambda, product_prices)
result = map(lambda amount : amount - 0.20*amount, product_prices)
print(result)           # map object
print(list(result))     # map object shall be printed as list

# Flat 50%Off
print(list(map(lambda price: price/2, product_prices)))

print()

numbers = list(range(10, 21))
print(numbers)

# Lambda for Even Number Check
l1 = lambda num : num%2 == 0    # True for Even and False for Odd

# Lambda for Odd Number Check
l2 = lambda num : num%2 != 0    # True for Odd and False for Even

print(list(map(l1, numbers)))
print(list(map(l2, numbers)))

# map function, maps lambda to every single element of the list
# filter function, filters the data with lambda

print(list(filter(l1, numbers)))
print(list(filter(l2, numbers)))

from functools import reduce

# lRef = lambda x, y: x+y
# numbers = [1, 2, 3]
# sum = reduce(lRef, numbers) # reduce shall reduce the data to a single number :)
# print(sum)

print(reduce(lambda x, y: x*y, [10, 20, 30, 40, 50]))

# Generally, Looping Operations with some Computations can be done in short hand expressions:
# map -> applies the same logic on all the elements
# filter -> applies the same logic on all the elements and extract selective elements as per the function
# reduce -> applies a computation on all the elements to return a single value :)

# Assignment: Explore the functions, map, filter and reduce with Tuple, Set and Dictionary :)