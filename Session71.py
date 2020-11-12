"""
    Convolutional Neural Network
     or CNN
     or ConvNet
"""

import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Images can be preprocessed on our end
# we can make an image pixel value to be in the range of 0 and 1
# Normalize the Image (RGB Image -> Pixel can be from 0 to 255)
train_images, test_images = train_images/255.0, test_images/255.0

print(train_images[0])
print(train_images[0].shape)
print(train_labels[0])

class_names = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

"""
plt.figure(figsize=(10, 20))
for i in range(25):
    plt.subplot(5, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i][0]])

plt.show()
"""

# CNN Model Construction
model = models.Sequential()

# kernel function number must be in the poser of 2 and we increase them as we increases conv layers

model.add(layers.Conv2D(32, (3, 3), activation="relu", input_shape=(32, 32, 3))) # input_shape=train_images[0].shape)
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Conv2D(64, (3, 3), activation="relu")) # input_shape=train_images[0].shape)
model.add(layers.MaxPooling2D((2, 2)))

# Add Neural Network
model.add(layers.Flatten())
model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(10, activation="softmax"))

model.compile(optimizer="adam", loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=["accuracy"])

history = model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

print(history.history)

test_loss, test_accuracy = model.evaluate(test_images, test_labels)
print("LOSS: {} ACCURACY: {}".format(test_loss, test_accuracy))

# Assignment: Work on Predicting the Images :)
# Write snippets to perform predictions :)

# Also add an additional ConvNet+MaxPool Layer and see the results :)

