"""
    ANN Tensorflow APIs
    Using Standardization from sklearn on DataSet

    For DataSet
    https://www.kaggle.com/uciml/forest-cover-type-dataset
    https://archive.ics.uci.edu/ml/datasets/Covertype

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

import tensorflow as tf
from tensorflow import keras

# https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html
from sklearn import preprocessing

data_set = pd.read_csv("covtype.csv")
print(data_set)

# Extract all the Input Features
X = data_set[data_set.columns[:55]]

# Target
Y = data_set.Cover_Type

# Split the Data
x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.7, random_state=90)

# Normalizing the Data
train_normalized = x_train[:10] # 1st 10 Training columns to be normalized/standardized:)
test_normalized = x_test[:10]   # 1st 10 Testing columns to be normalized/standardized:)

# Standardization technique on our training data
std_scale = preprocessing.StandardScaler().fit(train_normalized)
x_train_normalized = std_scale.transform(train_normalized)

print(x_train_normalized, type(x_train_normalized))

# Standardization technique on our testing data
std_scale = preprocessing.StandardScaler().fit(test_normalized)
x_test_normalized = std_scale.transform(test_normalized)

print(x_test_normalized, type(x_test_normalized))

# Conversion of numpy arrays to data frames
training_normalized_columns = pd.DataFrame(x_train_normalized,
                                           index=train_normalized.index,
                                           columns=train_normalized.columns)

# in our original training dataset we updated the columns or replaced the column values with standardized values
x_train.update(training_normalized_columns)

# Conversion of numpy arrays to data frames
testing_normalized_columns = pd.DataFrame(x_test_normalized,
                                           index=test_normalized.index,
                                           columns=test_normalized.columns)

# in our original training dataset we updated the columns or replaced the column values with standardized values
x_test.update(testing_normalized_columns)

print(x_train)
print("########################")
print(x_test)

print(x_train.shape)
print(x_train.shape[1])

# Create ANN Model
input_layer = keras.layers.Dense(64, activation=tf.nn.relu, input_shape=(x_train.shape[1], ))
hidden_layer = keras.layers.Dense(32, activation=tf.nn.relu)
output_layer = keras.layers.Dense(8, activation=tf.nn.softmax) # 8 classes to be predicted

ann = [input_layer, hidden_layer, output_layer]

model = keras.Sequential(ann)

# Compile the ANN Model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Training the Model
history = model.fit(x_train, y_train, epochs=5, batch_size=120)

# Training the model over n epochs generates a history in return
print("^^^^^^^^^^^^^^")
print("HISTORY")
print("^^^^^^^^^^^^^^")
print(history.history)
print(history.history.keys())

print()

print("^^^^^^^^^^^^^^")
print("METRICS")
print("^^^^^^^^^^^^^^")
test_loss, test_acc = model.evaluate(x_test, y_test)

print("LOSS:", test_loss)
print("ACCURACY:", test_acc)


epochs = [0, 1, 2, 3, 4]
accuracy_over_epochs = history.history["accuracy"]

plt.plot(epochs, accuracy_over_epochs)
plt.xlabel("EPOCHS")
plt.ylabel("ACCURACY")
plt.show()


# Predictions
probability_model = keras.Sequential([model, keras.layers.Softmax()])
predictions = probability_model.predict([x_test])
print(predictions)
print(predictions[0]) # very 1st prediction
print(np.argmax(predictions[0])) # class of the forest type :)



