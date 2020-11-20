import numpy as np
import cv2

# Model Shall Recognize several classes in images
model_data = {
    "prototxt": "MobileNetSSD_deploy.prototxt",
    "model": "MobileNetSSD_deploy.caffemodel",
    "confidence": 0.2
}

class_names = {
    0: "background",
    1: "aeroplane",
    2: "bicycle",
    3: "bird",
    4: "boat",
    5: "bottle",
    6: "bus",
    7: "car",
    8: "cat",
    9: "chair",
    10: "cow",
    11: "dining table",
    12: "dog",
    13: "horse",
    14: "motorbike",
    15: "person",
    16: "plant in pot",
    17: "sheep",
    18: "sofa",
    19: "train",
    20: "tv monoitor",
}

# Load the Neural Network with OPEN CV API
neural_network = cv2.dnn.readNetFromCaffe(model_data["prototxt"], model_data["model"])

# Video Stream from web cam
capture = cv2.VideoCapture(0)

while True:
    # Capture Frame and Analyze each and Every Frame
    ret, frame = capture.read()

    # Caffe Models shall read images as binary images -> BLOB (Binary Large Object) format
    # Pre Processing of Image before we feed it to the Neural Network for predictions
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300))

    # Height and width of Image
    (h, w) = frame.shape[:2]

    # Feed the model with blob image as input :)
    neural_network.setInput(blob)

    # Fetch all the predictions for the faces in the image
    predictions = neural_network.forward()

    # Iterating in the predictions
    for i in range(0, predictions.shape[2]):
        confidence = predictions[0, 0, i, 2]

        if confidence > model_data["confidence"]:
            print(confidence)

            class_id = int(predictions[0, 0, i, 1])  # Class Index available at 1st index of predictions

            text = "{:.2f}%".format(confidence*100)
            label = class_names[class_id] + " : " + text

            box = predictions[0, 0, i, 3:7] * np.array([w, h, w, h])
            (start_x, start_y, end_x, end_y) = box.astype("int")

            cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (0, 0, 255), 2)

            y = start_y-10 if start_y-10 > 10 else start_y + 10
            cv2.putText(frame, label, (start_x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

    # cv2.namedWindow("FRAME", cv2.WINDOW_NORMAL)
    cv2.imshow("PREDICTED FACES", frame)

    if cv2.waitKey(1) >= 0:
        break