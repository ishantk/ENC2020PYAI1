"""
    Integrating FLASK with ML/DL
"""


import tensorflow as tf
from tensorflow import keras
import numpy as np

from flask import *

app = Flask("MyApp")

model = None
test_images = None
test_labels = None

# 10 labels for 10 images in fashion mnist dataset
labels = ["TShirt/Top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle Boot"]

@app.route("/")
def index():
    return render_template("dl-index.html")


@app.route("/train")
def train_model():

    global model
    global labels
    global test_images
    global test_labels

    fashion_mnist_dataset = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist_dataset.load_data()

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

    return render_template("dl-training-success.html", message="LABELS:{} LOSS: {} ACCURACY: {}".format(str(labels), test_loss, test_accuracy))

@app.route("/predict", methods=["POST"])
def predict_class():

    global test_images
    global test_labels
    global model

    probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
    predictions = probability_model.predict([test_images])

    index = int(request.form["index"])

    print(predictions[index])
    print(np.argmax(predictions[index]))
    print(test_labels[index])

    # return "LABEL PREDICTED IS {} and CLASS IS {}".format(predicted_label, NAMES[predicted_label[0]])
    return render_template("dl-prediction.html", predicted_class="{} | {}".format(test_labels[0], labels[test_labels[0]]))

if __name__ == '__main__':
    app.run(debug=True)
