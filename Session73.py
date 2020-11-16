"""
    CNN Model in Flask Web App
    COVID-19 Chest XRay
"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten

# to prepare data set for images
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import matplotlib.pyplot as plt

import cv2
import numpy as np


# STEP-1 Prepare DataSet
training_images_generator = ImageDataGenerator(rescale=1.0/255.0)
testing_images_generator = ImageDataGenerator(rescale=1.0/255.0)

training_images = training_images_generator.flow_from_directory(
                                    'covid19dataset/train',
                                    target_size=(64, 64),
                                    batch_size=8,
                                    class_mode='binary')

testing_images = testing_images_generator.flow_from_directory(
                                    'covid19dataset/test',
                                    target_size=(64, 64),
                                    batch_size=8,
                                    class_mode='binary')

# DirectoryIterator
print(type(training_images))
print(type(testing_images))

# In Order to get the Images from we will use next method i.e. to pull data from generator :)
sample_training_images, _ = next(training_images)
print(sample_training_images[0])
print(sample_training_images[0].shape)


def plot_images(images):
    fig, axes = plt.subplots(1, 5, figsize=(20, 20))
    axes = axes.flatten()
    for img, ax in zip(images, axes):
        ax.imshow(img)
        ax.axis('off')

    plt.tight_layout()
    plt.show()

# plot_images(sample_training_images[:5])


# STEP-2 Prepare and Train ANN Model

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit_generator(training_images, epochs=5, validation_data=testing_images)

# STEP-3 Evaluate Model for Accuracy and Losses
accuracy = history.history['accuracy']
loss = history.history['loss']

val_accuracy = history.history['val_accuracy']
val_loss = history.history['val_loss']

print(accuracy)
print(val_loss)

epochs = range(5)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs, accuracy, label="TRAINING ACCURACY")
plt.plot(epochs, val_accuracy, label="VALIDATION ACCURACY")
plt.legend(loc='lower right')
plt.title('ACCURACY')

plt.subplot(1, 2, 2)
plt.plot(epochs, loss, label="TRAINING LOSS")
plt.plot(epochs, val_loss, label="VALIDATION LOSS")
plt.legend(loc='upper left')
plt.title('LOSS')

# plt.show()

# STEP-4 Make Predictions

labels = ["NORMAL", "COVID"]

# Testing Image to make prediction on
# image = cv2.imread("covid19dataset/test/covid/nejmoa2001191_f3-PA.jpeg") # 1 -> COVID INFECTED
image = cv2.imread("covid19dataset/test/normal/NORMAL2-IM-1423-0001.jpeg") # 0 -> NORMAL
image = cv2.resize(image, (64, 64))
image = np.reshape(image, [1, 64, 64, 3])

predicted_class = model.predict_classes(image)
print(predicted_class)
print(labels[predicted_class[0][0]])

# Assignment:
# Just put the data in covind19mask directory and do the same program for COVID-19 Mask Detection

