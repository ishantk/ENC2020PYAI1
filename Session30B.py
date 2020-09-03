import numpy as np
import time


numbers = list(range(1, 1000001)) # Creational Statement

time_stamp1 = time.time()
for n in numbers:
    pass
time_stamp2 = time.time()


array = np.array(list(range(1, 1000001))) # Creational Statement

time_stamp3 = time.time()
for n in array:
    pass
time_stamp4 = time.time()

print("Time Stamp for List: ", time_stamp2-time_stamp1)
print("Time Stamp for numpy array: ", time_stamp4-time_stamp3)


# Compare performance for below operations:
# 1. finding the max of list/ndarray
# 2. summation of all the elements of list/ndarray
# Use the APIs and see the results :)