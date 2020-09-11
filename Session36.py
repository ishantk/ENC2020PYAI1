"""
    Pandas
    Data Analysis Library
        Series    -> 1-D Array
        DataFrame -> 2-D Array (Table)
    Reference Link: https://pandas.pydata.org/
"""

import numpy as np
import pandas as pd

array1 = np.arange(1, 101, 2)       # numpy array
array2 = list(range(1, 101, 2))     # list

print(array1)
print(type(array1))

print()

print(array1)
print(type(array2))

print("Creating Series in Pandas")

S1 = pd.Series(array1)
S2 = pd.Series(array2)

print(S1)
print()
print(S2)

print("AXES:")
print(S1.axes) # indexes of Series Data Structure

print("VALUES:")
print(S1.values) # values in Series Data Structure

print("HEAD")
print(S1.head()) # first 5 records

print("TAIL")
print(S1.tail()) # last 5 records

print("CUSTOM HEAD")
print(S1.head(10)) # first 10 records

print("CUSTOM TAIL")
print(S1.tail(10)) # last 10 records



