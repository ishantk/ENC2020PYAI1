"""
    Regression with ANN
    Tensorflow APIs

    DataSet -> cars.csv
    prediciting sales value from the features

    PreProcessing -> MinMaxScaler from sklearn
    https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow import keras

data_set = pd.read_csv("cars.csv")
print(data_set)

X = data_set.iloc[:, 0:5]
# X = data_set[data_set.columns[0:5]].values
Y = data_set.sales.values

print("FEATURES")
print(X)

print("TARGET")
print(Y)

print(Y.shape)
Y = np.reshape(Y, (-1, 1))
print(Y.shape)


scaler_features = MinMaxScaler()
scaler_target = MinMaxScaler()

scaler_features.fit(X)
scaler_target.fit(Y)

x_scaled = scaler_features.transform(X)
y_scaled = scaler_target.transform(Y)

print("TRANSFORMED FEATURES")
print(x_scaled)

print("TRANSFORMED TARGET")
print(y_scaled)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y_scaled)

# Create ANN Model for Regression
# Input Layer is same number of perceptrons as of features
# Output layer is number of perceptrons we are expecting as classes
# hidden layer perceptrons can be fine tuned

# IL    HL    OL
# 5     4     1

# While creating ANN
# 1. We can fine tune by increasing decreasing neurons
# 1. We can fine tune by increasing decreasing layers also


input_layer = keras.layers.Dense(12, input_dim=5, activation='relu')
hidden_layer = keras.layers.Dense(8, activation='relu')
output_layer = keras.layers.Dense(1, activation='linear')

# ann = [input_layer, hidden_layer, output_layer]

model = keras.Sequential()
model.add(input_layer)
model.add(hidden_layer)
model.add(output_layer)

print("OUR ANN MODEL SUMMARY")
print(model.summary())

# Compile the Model
model.compile(loss="mse", optimizer="adam", metrics=["mse", "mae", "accuracy"])

history = model.fit(x_scaled, y_scaled, epochs=25, batch_size=60, validation_split=0.2)

print(history.history.keys())

plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.legend()
plt.xlabel("EPOCHS")
plt.ylabel("LOSS")
plt.show()

# Prediction :)
x_to_predict = np.array([[40, 1, 15, 7254, 6472]])
x_to_predict_scaled = scaler_features.transform(x_to_predict)
y_predicted = model.predict(x_to_predict_scaled)

# Invert Normalization o.e. get the real value again from standardized value
y_predicted = scaler_target.inverse_transform(y_predicted)

print("FOR {} PREDICTION IS {}".format(x_to_predict, y_predicted))

# Weekend Assignment
# Fine tune the model to take the predicted value as close as it can be
