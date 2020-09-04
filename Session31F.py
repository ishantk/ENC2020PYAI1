import numpy as np

data = [
    (8, 9),
    (10, 18),
    (12, 14),
]

array1 = np.array(data)
print(array1)
print(array1[0:2, 1])

print(array1.min())
print(array1.max())
print(array1.sum())

# Axis -> 0 [Column Wise]
# Axis -> 1 [Row Wise]
print("Column Wise min max sum")
print("MIN:", array1.min(axis=0))
print("MAX:", array1.max(axis=0))
print("SUM:", array1.sum(axis=0))

print("Row Wise min max sum")
print("MIN:", array1.min(axis=1))
print("MAX:", array1.max(axis=1))
print("SUM:", array1.sum(axis=1))