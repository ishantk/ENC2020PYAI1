"""
    Image Classification Problem with Tensorflow
    Everything in Machine Learning can be done with Tensorflow

    APIs called keras to solve ML Problems
    keras are high level APIs in tensorflow

"""

import tensorflow as tf
from tensorflow import keras # used for creating training models as ANNs for solving ML Problems

import matplotlib.pyplot as plt

import numpy as np

# DataSet from keras known as fashion mnist which contains 70,000 gray scaled images
# 10 different categories
# Resolution of image is quite low -> 28 X 28

# Image Classification | DataSet of 70,000 images
# 60,000 Images for training
# 10,000 Images for testing


fashion_mnist_dataset = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist_dataset.load_data()

print("Training Data Length")
print(len(train_images), len(train_labels))

print("Testing Data Length")
print(len(test_images), len(test_labels))

# 10 labels for 10 images in fashion mnist dataset
labels = ["TShirt/Top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle Boot"]

print()

print("Training Image at 0th Index")
print(train_images[0])
print(train_images[0].shape)
print(train_labels[0])
print(labels[train_labels[0]])

print()

print("Training Image at 9th Index")
print(train_images[9])
print(train_images[9].shape)
print(train_labels[9])
print(labels[train_labels[9]])

# plt.subplot(2, 4, 1)
# plt.imshow(train_images[0], cmap=plt.cm.gray_r)
#
# plt.subplot(2, 4, 2)
# plt.imshow(train_images[9], cmap=plt.cm.gray_r)

# for i in range(0, 8):
#     plt.subplot(2, 4, (i+1))
#     plt.imshow(train_images[i], cmap=plt.cm.gray_r)
#
# plt.show()


# Deep Learning Steps
# 1. Explore the DataSet (more deeper the exploration more better the ANN can be created)
# 2. to create ANN with layers and we call it as model :)
# 3. compile the ANN with optimizer, loss and metrics :)
# 4. To train the model and here also we have fit function as terminology
# 5. Predict the outputs

# 2. to create ANN with layers and we call it as model :)

# ANN
# Input Layer   | image with shape of 28X28 and we will flatten this array as 1-D array
# Hidden Layer  | n number of perceptrons they are kind of fine tuned, activation function is going to relu
# Output Layer  | 10 perceptrons with softmax as activation function

input_layer = keras.layers.Flatten(input_shape=(28, 28))
hidden_layer = keras.layers.Dense(units=64, activation=tf.nn.relu)
output_layer = keras.layers.Dense(units=10, activation=tf.nn.softmax)


ann = [input_layer, hidden_layer, output_layer]
model = keras.Sequential(ann)

# 3. compile the ANN with optimizer, loss and metrics :)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 4. Train the Model
model.fit(x=train_images, y=train_labels, epochs=8)

# Lets evaluate our model
test_loss, test_accuracy = model.evaluate(x=test_images, y=test_labels)
print("TEST LOSS:", test_loss)
print("TEST ACCURACY:", test_accuracy)

print("================================")


probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
predictions = probability_model.predict([test_images])


print(predictions[0]) # for the 0th testing image we will have 10 different probability scores :)
print(np.argmax(predictions[0])) # np.argmax we will get the index of the highest probability which is our prediction :)
print(test_labels[0])

# print(labels[np.argmax(predictions[0])])