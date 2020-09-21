import cv2
import numpy as np

image = cv2.imread("restaurant.jpeg", 1) # Colored

print("ORIGINAL IMAGE")
print(image)

print("ORIGINAL IMAGE SHAPE")
print(image.shape)

resized_image = cv2.resize(image, (image.shape[1]//2, image.shape[0]//2)) # 350 X 233


print("RESIZED IMAGE")
print(resized_image)

print("RESIZED IMAGE SHAPE")
print(resized_image.shape)


# cv2.imshow("MyResizedRestaurant", resized_image)
# cv2.waitKey(0) # User can press any key on the keyboard to exit
# cv2.destroyAllWindows() # release memory resources

rotated_resized_image = np.rot90(resized_image)

cv2.imwrite("rot_res_restaurant.jpeg", rotated_resized_image)
print("Image Saved :)")

cv2.imshow("MyRotatedResizedRestaurant", rotated_resized_image)
cv2.waitKey(0) # User can press any key on the keyboard to exit
cv2.destroyAllWindows() # release memory resources