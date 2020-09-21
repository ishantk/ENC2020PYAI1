"""
    Exploring OpenCV
"""

import cv2
import numpy as np
# image = cv2.imread("restaurant.jpeg", 1) # Colored
image = cv2.imread("restaurant.jpeg", 0) # BW

print("IMAGE")
print(image) # is numpy array -> Mathematical representation of an Image as RGB Values :)

print("-----------")
print(image[0])
print("-----------")

roatated_image = np.rot90(image)
roatated_image = np.rot90(roatated_image)

print("IMAGE AFTER ROTATE 90")
print(roatated_image)

print("-----------")
print(roatated_image[0])
print("-----------")

cv2.imshow("MyRotatedRestaurant", roatated_image)
# cv2.waitKey(0) # User can press any key on the keyboard to exit
cv2.waitKey(5000) # after 5 secs screen will be gone :)
cv2.destroyAllWindows() # release memory resources

