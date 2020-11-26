"""
> R-CNN and Mask R-CNN
> Matterport Mask R-CNN Project
> Object Detection with Mask R-CNN

R-CNN
Ref Reading Paper for Selective Search: http://www.huppelen.nl/publications/selectiveSearchDraft.pdf
Bounding boxes are proposed by the “selective search” algorithm, each of which is stretched and features are
extracted via a deep convolutional neural network, such as AlexNet, before a final set of object classifications
are made with linear SVMs.


Mask R-CNN
Ref Reading: https://arxiv.org/abs/1703.06870
Extension of Faster R-CNN that adds an output model for predicting a mask for each detected object.

Matterport Mask R-CNN Project
Mask R-CNN is a sophisticated model to implement,
especially as compared to a simple or even state-of-the-art deep convolutional neural network model.

Ref Link for Mask R-CNN:    https://github.com/matterport/Mask_RCNN
DataSet:                    http://cocodataset.org/#home
Matterport 3D:              https://matterport.com/blog/announcing-matterport3d-research-dataset

Library MisMatch which we must try to rectify:
tensorflow -> 2.1
mrcnn -> 0.2 | pip intall mrcnn

"""

# import the necessary packages
from mrcnn.config import Config
from mrcnn import model as modellib
from mrcnn import visualize
import numpy as np
import colorsys

import imutils
import random
import cv2
import os


args = {
	"weights":"mask_rcnn_coco.h5",
	"labels":"coco_labels.txt",
	"image":"parking.jpg"
}

# load the class label names from disk, one label per line
CLASS_NAMES = open(args["labels"]).read().strip().split("\n")

# generate random (but visually distinct) colors for each class label
# given by matterport to classify various objects in various colors
hsv = [(i / len(CLASS_NAMES), 1, 1.0) for i in range(len(CLASS_NAMES))]
COLORS = list(map(lambda c: colorsys.hsv_to_rgb(*c), hsv))
random.seed(42)
random.shuffle(COLORS)

class SimpleConfig(Config):
	# give the configuration a recognizable name
	NAME = "coco_inference"

	# set the number of GPUs to use along with the number of images
	# per GPU
	GPU_COUNT = 1
	IMAGES_PER_GPU = 1

	# number of classes (we would normally add +1 for the background
	# but the background class is *already* included in the class
	# names)
	NUM_CLASSES = len(CLASS_NAMES)


# initialize the inference configuration
config = SimpleConfig()

# initialize the Mask R-CNN model for inference and then load the
# weights
print("[INFO] loading Mask R-CNN model...")
model = modellib.MaskRCNN(mode="inference", config=config, model_dir=os.getcwd())
model.load_weights(args["weights"], by_name=True)

# load the input image, convert it from BGR to RGB channel
# ordering, and resize the image
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = imutils.resize(image, width=512)

# perform a forward pass of the network to obtain the results
print("[INFO] making predictions with Mask R-CNN...")
r = model.detect([image], verbose=1)[0]

# print(r)
# print(r["rois"])
# print(r["rois"].shape)
# print(r["rois"].shape[0]) # we got 59 objects detected inside the image :)


# loop over of the detected object's bounding boxes and masks
for i in range(0, r["rois"].shape[0]):
	# extract the class ID and mask for the current detection, then
	# grab the color to visualize the mask (in BGR format)
	classID = r["class_ids"][i]
	mask = r["masks"][:, :, i]
	color = COLORS[classID][::-1]

	# visualize the pixel-wise mask of the object
	image = visualize.apply_mask(image, mask, color, alpha=0.5)

# convert the image back to BGR so we can use OpenCV's drawing
# functions
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

print(">> TOTAL VEHICLES PARKED:", len(r["scores"]))

# loop over the predicted scores and class labels
for i in range(0, len(r["scores"])):
	# extract the bounding box information, class ID, label, predicted
	# probability, and visualization color
	(startY, startX, endY, endX) = r["rois"][i]
	classID = r["class_ids"][i]
	label = CLASS_NAMES[classID]
	score = r["scores"][i]
	color = [int(c) for c in np.array(COLORS[classID]) * 255]

	# draw the bounding box, class label, and score of the object
	cv2.rectangle(image, (startX, startY), (endX, endY), color, 2)
	text = "{}: {:.3f}".format(label, score)
	y = startY - 10 if startY - 10 > 10 else startY + 10
	cv2.putText(image, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX,
		0.6, color, 2)

# show the output image
cv2.imshow("Output", image)
cv2.waitKey()