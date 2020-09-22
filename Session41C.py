import cv2
import numpy as np

video = cv2.VideoCapture(0)

frame_count = 0

while True:

    check, frame = video.read()

    frame_count += 1

    # frame = np.rot90(frame)

    print(frame)
    cv2.imshow("MyVideoFrame {}".format(frame_count), frame)

    key = cv2.waitKey(1) # 1 is 1 milli sec

    # for a detected change,
    # cv2.imwrite("anyanme.jpg", rotated_resized_image)

    if key == ord('q'):
        break

print("Video Streaming Closed")
print("Frames Captured:", frame_count)
cv2.destroyAllWindows()

# 1. Capture Video Frames, and Save them as Video the way we saved in our previous session as an image
# 2. In case nothing changes in the video, so all the frames will be same
#      i.e. their mathematical data remains same
#      capture the frames from the video stream whenever a change occurs

#    Thw whole idea is to detect the change which occurred in the video stream and save that frame as an image :)

# We can check if frames are same or different  :)