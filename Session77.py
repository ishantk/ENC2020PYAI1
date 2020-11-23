import tensorflow as tf
import tensorflow_hub as hub #pip install tensorflow_hub
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image #pip install Pillow

# Tensorflow Hub: https://tfhub.dev/

# Tensorflow Hub shall give us pre trained models
# Link to Model on Tensorflow Hub
classifier_url = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4"

# Testing Image
image_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/grace_hopper.jpg"

# How many classes the model can identify
labels_url = "https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt"

IMAGE_SHAPE = (224, 224)
INPUT_IMAGE_SHAPE = (224, 224, 3)

# Deep Learning Model from TF Hub
# Reference Reading: https://keras.io/api/applications/mobilenet/
model = tf.keras.Sequential([hub.KerasLayer(classifier_url, input_shape=INPUT_IMAGE_SHAPE)])

print(model.summary())


# Read the Image from URL
graceHopperImage = tf.keras.utils.get_file('image.jpg', image_url)
graceHopperImage = Image.open(graceHopperImage).resize(IMAGE_SHAPE)

print(graceHopperImage)

print("NORMALIZING THE IMAGE")

# Image PreProcessing for Deep Learning Model Input
graceHopperImage = np.array(graceHopperImage)/255.0
print(graceHopperImage)
print(graceHopperImage.shape)


# Read the Labels and Store them in a list
labelPath = tf.keras.utils.get_file("ImageNetLabels.txt", labels_url)
labels = np.array(open(labelPath).read().splitlines())

print("LABELS")
print(labels)
print(len(labels))

# Reading Classes
# print(open(labelPath).read().splitlines())


# Lets Use the Model for making predictions
result = model.predict(graceHopperImage[np.newaxis, :])
predictedClassLabelIdx = np.argmax(result[0], axis=-1)
print("PREDICTED LABEL INDEX :", predictedClassLabelIdx)
print("PREDICTED LABEL:", labels[predictedClassLabelIdx])

plt.imshow(graceHopperImage)
plt.title(labels[predictedClassLabelIdx])
plt.show()

# Learning now is all about Exploration
# more you now start exploring more you will know :)
# Explore what is Inception Model by Google

# Assignment
# https://www.tensorflow.org/lite/models/pose_estimation/overview

# Explore More Here
# https://www.tensorflow.org/lite/models/image_classification/overview
