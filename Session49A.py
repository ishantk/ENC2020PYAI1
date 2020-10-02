import pandas as pd
import matplotlib.pyplot as plt
import numpy
# For Polynomial PreProcessing on DataSet:
# https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data_set = pd.read_csv("speeds.csv")
print(data_set)

X = data_set['hour'].values
Y = data_set['speed'].values

print(X)
print(Y)

"""
model = numpy.poly1d(numpy.polyfit(X, Y, 3))
line = numpy.linspace(1, len(X), 100)

print(line)

poly_data = model(line)
print(poly_data)

plt.scatter(X, Y)
plt.plot(line, poly_data)

plt.show()
"""

# For sklearn models, we need training data in 2d shape
# Transforming 1-d to 2-D
# X = X.reshape(len(X), 1)
# Y = Y.reshape(len(Y), 1)
#
# print(X)
# print(Y)

# Use numpy to convert 1d to 2d
X = X[:, numpy.newaxis]
Y = Y[:, numpy.newaxis]

print(X)
print(Y)

# For ML Model to come with Polynomial Predictions
# The inputs must be fit into polynomial structure

poly_features = PolynomialFeatures(degree=2)
poly_X = poly_features.fit_transform(X)

model = LinearRegression()
# model.fit(X, Y)       # errors :(
model.fit(poly_X, Y)    # OK :)
Y_pred = model.predict(poly_X)

print("Interceptor:", model.intercept_)
print("Coefficient:", model.coef_)

root_mean_squared_error = numpy.sqrt(mean_squared_error(Y, Y_pred))
r2 = r2_score(Y, Y_pred)

print("root_mean_squared_error", root_mean_squared_error)
print("r2_score", r2)

# predicted_speed = model.predict([[16]])

hour = numpy.array([16])
hour = hour.reshape(len(hour), 1)
hour_input = poly_features.fit_transform(hour)

predicted_speed = model.predict(hour_input)
print(predicted_speed)

# Predict COVID Cases for upcoming times with Polynomial Regression
# User should be able to enter the day as input in the GUI to see the results alongwith graph
