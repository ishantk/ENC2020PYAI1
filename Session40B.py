"""
    OpenCV Reference: https://opencv.org/
    In case of errors, make sure you have latest pip -> pip install --upgrade pip
    pip install opencv-python
"""
import cv2
print(cv2.__version__)

image = cv2.imread("restaurant.jpeg", 1) # 1 reads the image as colored and 0 as B/W
print("IMAGE")
print(image)

print()

print("IMAGE TYPE")
print(type(image))

print()

print("IMAGE SHAPE")
print(type(image.shape))

print("IMAGE at 0th Index")
print(image[0])

print("Length of IMAGE")
print(len(image))