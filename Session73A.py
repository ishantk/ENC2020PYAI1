from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten

# to prepare data set for images
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import matplotlib.pyplot as plt

import cv2
import numpy as np

from flask import *

app = Flask("CNN APP")

model = None

@app.route("/")
def index():
    return render_template("ic-cnn-index.html")

@app.route("/train")
def train_model():

    global model

    # STEP-1 Prepare DataSet
    training_images_generator = ImageDataGenerator(rescale=1.0 / 255.0)
    testing_images_generator = ImageDataGenerator(rescale=1.0 / 255.0)

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

    # 3. compile the ANN with optimizer, loss and metrics :)
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)))
    model.add(MaxPooling2D((2, 2)))

    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))

    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    history = model.fit_generator(training_images, epochs=8, validation_data=testing_images)

    # STEP-3 Evaluate Model for Accuracy and Losses
    accuracy = history.history['accuracy']
    loss = history.history['loss']

    return render_template("ic-cnn-training-success.html", message="LOSS: {} ACCURACY: {}".format(loss, accuracy))

@app.route("/upload-image", methods=['POST'])
def upload_image():

    labels = ["NORMAL", "COVID"]

    file = request.files['image']
    file.save(file.filename)

    image = cv2.imread(file.filename)
    image = cv2.resize(image, (64, 64))
    image = np.reshape(image, [1, 64, 64, 3])

    predicted_class = model.predict_classes(image)
    print(predicted_class)
    print(labels[predicted_class[0][0]])

    return render_template("ic-cnn-results.html",
                           message="LABEL: {}".format(labels[predicted_class[0][0]]))


if __name__ == '__main__':
    app.run(debug=True)