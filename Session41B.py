import cv2
import time

video = cv2.VideoCapture(0)

check, frame = video.read()

print("CHECK")
print(check)

print("FRAME")
print(frame)

# Halt the program for 5 secs
time.sleep(5)

print("Releasing Video")
video.release()

cv2.imshow("MyVideoFrame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()