import numpy as np

array = np.loadtxt("data.txt", dtype=np.int, delimiter=",")

print(array)
print(array.shape)

array = np.arange(10, 200, 10)
print(array)

np.savetxt("my_data.txt", array, fmt="%04d")
print("Data Saved :) ")


# Explore -> numpy with csv files :) explore other functions