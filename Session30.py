"""
    Data Science:
        numpy
        matplotlib
        seaborn
        panadas
        scikit -> Machine Learning

    Introduction to numpy - I
    Reference : https://numpy.org/
"""

import numpy as np # we will get lot of numpy APIs to use for the solution
print(np.__version__)

# In numpy we have 1 data structure -> ndarray

numbers = [10, 20, 30, 40, 50]
print(numbers, type(numbers))

print()

# array1 = np.array([10, 20, 30, 40, 50])
array1 = np.array(numbers)
print(array1, type(array1))

print()

# tuple, set, string, dictionary
array2 = np.array((10, 20, 30, 40, 50))
print(array2, type(array2))

print()

array3 = np.array({10, 20, 30, 40, 50})
print(array3, type(array3))

print()

array4 = np.array(("Hello", "Hi"))
print(array4, type(array4))


print()

# array5 = np.array({"name": "John", "age":20}) # ndarray with 1 single element as dictionary
array5 = np.array(({"name": "John", "age":20}, {"name": "Fionna", "age":22}))
print(array5, type(array5))

print()

array6 = np.array(60)
print(array6)

# Length function from python will not work on numpy ndarray
# print(len(array6))

# Find the length of ndarray :)
print(np.size(array5))