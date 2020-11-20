"""
    Re Visiting OpenCV for Deep Learning

    PreDefined CNN Architectures:
    LeNet,
    AlexNet,
    VGG,
    GoogLeNet,
    ResNet and many more every day being added by community

    Caffe -> FW to develop DL Models just like Tensorflow

    caffemodel with txt file having information of the model
    https://caffe.berkeleyvision.org/

    Steps:
    1. Download available and trained caffemodel
    2. Download its prototxt file which will contain the structure for your ann model
    3. Use open cv APIs to load the model and perform predictions

"""

import numpy as np
import cv2

# Model Shall Recognize Faces in an Image/Video :)
model_data = {
    "prototxt": "deploy.prototxt.txt",
    "model": "res10_300x300_ssd_iter_140000.caffemodel",
    "confidence": 0.5
}

# Load the Neural Network with OPEN CV API
neural_network = cv2.dnn.readNetFromCaffe(model_data["prototxt"], model_data["model"])

# Make Predictions
# Read the Image first
image = cv2.imread("group-photo.jpg")
print(image)
print(image.shape)

# Height and width of Image
(h, w) = image.shape[:2]

# Caffe Models shall read images as binary images -> BLOB (Binary Lage Object) format
# Pre Processing of Image before we feed it to the Neural Network for predictions
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300))

# Feed the model with blob image as input :)
neural_network.setInput(blob)

# Fetch all the predictions for the faces in the image
predictions = neural_network.forward()

print("===PREDICTIONS===")
print(predictions)
print(len(predictions))
print(predictions.shape)
print(predictions[0][0][0]) # -> out of 200 predictions, 0th index of prediction whose 2nd index is confidence
print("=================")

faces = 0

# Iterating in the predictions
for i in range(0, predictions.shape[2]):
    confidence = predictions[0, 0, i, 2]

    if confidence > model_data["confidence"]:
        print(confidence)
        faces += 1

        box = predictions[0, 0, i, 3:7] * np.array([w, h, w, h])
        (start_x, start_y, end_x, end_y) = box.astype("int")

        text = "{:.2f}%".format(confidence*100)

        cv2.rectangle(image, (start_x, start_y), (end_x, end_y), (0, 0, 255), 2)

        y = start_y-10 if start_y-10 > 10 else start_y + 10
        cv2.putText(image, text, (start_x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)


print("{} Faces Found in Image".format(faces))

cv2.imshow("PREDICTED FACES", image)
cv2.waitKey(0)

