# Know the DataSet for SVM
# Images :) -> Digits

import matplotlib.pyplot as plt
from sklearn import datasets


digits = datasets.load_digits()
print(digits)

print("IMAGES AS INPUTS WITH FEATURES")
# print(digits.images)
print(digits['images'])
print(len(digits['images']))

print()

print("LABELS")
# print(digits.target)
print(digits['target'])
print(len(digits['target']))


print("IMAGE at 0th Index")
print(digits['images'][0])
print(digits['images'][0].shape)
print("IMAGE LABEL at 0th Index")
print(digits['target'][0])


print("IMAGE at 9th Index")
print(digits['images'][9])
print(digits['images'][9].shape)
print("IMAGE LABEL at 9th Index")
print(digits['target'][9])

print("IMAGE at 9th Index")
print(digits['images'][99])
print(digits['images'][99].shape)
print("IMAGE LABEL at 99th Index")
print(digits['target'][99])

"""
plt.subplot(2, 4, 1)
plt.imshow(digits['images'][0], cmap=plt.cm.gray_r)

plt.subplot(2, 4, 2)
plt.imshow(digits['images'][1], cmap=plt.cm.gray_r)

plt.subplot(2, 4, 3)
plt.imshow(digits['images'][2], cmap=plt.cm.gray_r)

plt.subplot(2, 4, 4)
plt.imshow(digits['images'][3], cmap=plt.cm.gray_r)

plt.subplot(2, 4, 5)
plt.imshow(digits['images'][13], cmap=plt.cm.gray_r)

plt.subplot(2, 4, 6)
plt.imshow(digits['images'][10], cmap=plt.cm.gray_r)

plt.subplot(2, 4, 7)
plt.imshow(digits['images'][11], cmap=plt.cm.gray_r)

plt.subplot(2, 4, 8)
plt.imshow(digits['images'][12], cmap=plt.cm.gray_r)
"""


position = 1
for i in range(8):
    plt.subplot(2, 4, position)
    plt.imshow(digits['images'][position], cmap=plt.cm.gray_r)
    position += 1

plt.show()
