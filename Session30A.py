import numpy as np

array1 = np.array([10, 20, 30, 40, 50])
print(array1[1]) # indexing :)

array1[2] = 333 # update operation
print(array1)

print(len(array1))

print("Elements in Array [Basic For]:")
for i in range(len(array1)):
    print(array1[i])


print("Elements in Array [Enhanced For/For-Each]:")
for element in array1:
    print(element)

print()
array2 = np.append(array1, [99, 88, 77, 66, 55])
print(array1)
print(array2)

