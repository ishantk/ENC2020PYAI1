import numpy as np

# ndarray = 1-D
array1 = np.array([10, 20, 30])
# ndarray of ndarrays = 2-D
array2 = np.array([[10, 20, 30], [30, 40, 50], [50, 60, 70]])       # evenly shaped
# ndarray of lists = 1-D
array3 = np.array([[10, 20], [30, 40, 50, 60, 70], [50, 60, 70]])   # not evenly shaped

print(array1)
print(array2)
print(array3)

# Shape for ndarray

print("array1.shape: ", array1.shape)
print("array2.shape: ", array2.shape)
print("array3.shape: ", array3.shape)

print("array1 length: ", len(array1))
print("array2 length: ", len(array2))
print("array3 length: ", len(array3))

print(array1[1])    # 20
print(array2[2])    # [50 60 70]
print(array3[0])    # list([10, 20])

print(array2[2][0]) # 50
print(array3[0][1]) # 20