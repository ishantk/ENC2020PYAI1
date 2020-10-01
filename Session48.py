"""
    Multiple Linear Regression
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# pip install statsmodels
import statsmodels.api as sm

data_set = pd.read_csv("company_profits.csv")
print(data_set)

# Tip: Must check if data has linearity or not ?
"""
plt.scatter(data_set['R&DSpend'], data_set['Profit'])
plt.title("R&DSpend Vs Profit", fontsize=14)
plt.xlabel("R&DSpend", fontsize=14)
plt.ylabel("Profit", fontsize=14)
plt.grid(True)
plt.show()
"""

"""
plt.scatter(data_set['MarketingSpend'], data_set['Profit'])
plt.title("MarketingSpend Vs Profit", fontsize=14)
plt.xlabel("MarketingSpend", fontsize=14)
plt.ylabel("Profit", fontsize=14)
plt.grid(True)
plt.show()
"""

X = data_set[['R&DSpend', 'MarketingSpend']]
Y = data_set['Profit']

# X are Features or attributes and is Input
print(X)

print()

# Y is Output Value
print(Y)

# LinearRegression:          Y = b0 + b1*X
# MultipleLinearRegression:  Y = b0 + b1*X1 + b2*X2

# MultipleLinearRegression:  Profit = b0 + b1*R&DSpend + b2*MarketingSpend

# Create the Model
model = LinearRegression()

# Split DataSet
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)

# Training the Model
# PS: x_train here will have multiple columns
model.fit(x_train, y_train)

# Predict the Model for Metrics
y_pred = model.predict(x_test)

print("Interceptor:", model.intercept_)
print("Coefficients:", model.coef_)

# Profit = 48591.08 + 0.7712254*R&DSpend + 0.03033984*MarketingSpend

RDSpend = 144372.41
MKSpend = 383199.62

predicted_profit = model.predict([[RDSpend, MKSpend]])
print("predicted_profit is:", predicted_profit)

print("==========StatsModel API===========")

# From Stats, For Regression Models
# https://en.wikipedia.org/wiki/Linear_least_squares
# OLS, WLS and GLS | Please refer extra reading here :)

# Creating and Training the Model
stats_model = sm.OLS(Y, X).fit() # Y i.e. Output comes first here
# stats_model = sm.GLS(Y, X).fit() # Y i.e. Output comes first here
# stats_model = sm.WLS(Y, X).fit() # Y i.e. Output comes first here
stats_model_summary = stats_model.summary()
print(stats_model_summary)

predictions = stats_model.predict(X)
print(predictions)