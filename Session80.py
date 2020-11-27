"""
    R-CNN           50 seconds
    Fast-RCNN       2  seconds
    Faster-RCNN     0.2 seconds (Reference Research Paper: https://arxiv.org/abs/1506.01497)

"""

import torchvision
from torchvision import transforms
import cv2
from PIL import Image
import matplotlib.pyplot as plt

model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
info = model.eval()
print(info)

# N/A Class Labels were removed from the Coco DataSet
COCO_DATASET_LABELS = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A',
    'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
    'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table',
    'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',
    'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]


def predictions(imagePath, threshold):

    # Load Image
    image = Image.open(imagePath)

    # Pre-Processing the Image before we give it to Model
    preprocess = transforms.Compose([
        transforms.ToTensor()
    ])

    # Apply transform to the image
    image = preprocess(image)

    # Pass the image to the model
    predictions = model([image])
    print(predictions)

    # Get the Prediction Score
    predictionClass = [COCO_DATASET_LABELS[i] for i in list(predictions[0]['labels'].numpy())]

    # Bounding boxes
    predictionBoxes = [[(i[0], i[1]), (i[2], i[3])] for i in list(predictions[0]['boxes'].detach().numpy())]

    # Prediction Scores
    predictionScore = list(predictions[0]['scores'].detach().numpy())

    # Get list of indexes with score greater than threshold
    predictionWithThresholds = [predictionScore.index(x) for x in predictionScore if x > threshold][-1]

    # Prediction Boxes and Prediction Classes
    predictionBoxes = predictionBoxes[:predictionWithThresholds + 1]
    predictionClass = predictionClass[:predictionWithThresholds + 1]

    return predictionBoxes, predictionClass

def fasterrcnn(imagePath, threshold=0.5, rect_th=3, text_size=3, text_th=3):

    # Get predictions
    boxes, predictedClass = predictions(imagePath, threshold)

    # Read image with cv2
    image = cv2.imread(imagePath)

    # Convert to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    for i in range(len(boxes)):

        # Draw Rectangle with the coordinates
        cv2.rectangle(image, boxes[i][0], boxes[i][1], color=(0, 255, 0), thickness=rect_th)

        # Write the prediction class
        cv2.putText(image, predictedClass[i], boxes[i][0],  cv2.FONT_HERSHEY_SIMPLEX, text_size, (0,255,0),thickness=text_th)

    plt.figure(figsize=(10, 5))  # display the output image
    plt.imshow(image)
    plt.xticks([])
    plt.yticks([])
    plt.show()


def main():
    # fasterrcnn('traffic.jpg', rect_th=4, text_th=5, text_size=2)
    fasterrcnn('kidbroc.jpg', rect_th=4, text_th=5, text_size=2)

if __name__ == '__main__':
    main()
