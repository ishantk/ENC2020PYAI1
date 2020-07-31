"""
    Sequences in Python - Part-II

"""

# Conversions
numbers1 = (10, 20, 30, 40, 50, 20, 40)
print(numbers1, type(numbers1), hex(id(numbers1)))

print()

numbers2 = list(numbers1)
print(numbers2, type(numbers2), hex(id(numbers2)))

print()

numbers3 = set(numbers2)
print(numbers3, type(numbers3), hex(id(numbers3)))

print()

numbers4 = tuple(numbers3)
print(numbers4, type(numbers4), hex(id(numbers4)))

print()

str_data = str(numbers4)
print(str_data)
print(str_data[0])

print()

# Dictionary is a key value pair, all above doesnt not posses any key value pair
# hence, we cannot convert above structures into dictionary
# dict_data = dict(numbers3) # ERROR

# Reverse of tuple or list
print(numbers1)
print(numbers1[::-1])