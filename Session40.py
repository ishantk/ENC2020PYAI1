"""
    Linear Regression APIs
    scikit
    scipy
"""


from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np
import pandas as pd


"""
# 1. Create the Data Set
X = np.array([1, 2, 3, 4, 5])  # Independent Input Variable
Y = np.array([2, 4, 5, 4, 5])  # Dependent Output Variable


X = X.reshape((len(X), 1))
Y = Y.reshape((len(Y), 1))

# 2. Create the Model
model = LinearRegression()

# 3. Train the Model
model.fit(X, Y)
"""

# 1. Create the Data Set

table = pd.read_csv("advertising.csv")
print(table)

X = table.TV.values     # return column values as numpy 1-D array
Y = table.Sales.values

# 1-D Arrays
print(X)
print(Y)

X = X.reshape((len(X), 1)) # len num of rows with 1 column -> 2-D array :)
Y = Y.reshape((len(Y), 1))

# 2. Create the Model
model = LinearRegression()

# 3. Train the Model
model.fit(X, Y)

# Examine the Model
b0 = model.intercept_
b1 = model.coef_

print("b0 is:", b0)
print("b1 is:", b1)

# 4.Predictions
# predict on the original know data i.e. X
Y1 = model.predict(X)
print(Y1, Y1.shape)

# 5. Compute the Errors i.e. analyze metrics for the Model
score = r2_score(Y, Y1)
print("R2 Score is:", score)

print("Equation of Line: Y = {} + {} X".format(b0, b1))

unknown_tv_advertising = [250]
predicted_sales = model.predict([unknown_tv_advertising])
print("Predicted Sales is:", predicted_sales)



