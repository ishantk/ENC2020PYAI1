"""
    Random Forest Trees
    1. n -> how many Decision Trees to be used in our Model
    2. DataSet shall be divided into n number of subsets :)

    Assuming DataSet of 100 Records
    We choose 3 Trees to Solve problem

    Records anr randomized and feed to trees

    T1 -> 33 records
    T2 -> 33 records
    T3 -> 34 records

    Predictions will be given by T1, T2 and T3 and we will use them to finally give the prediction

    COVID-19 DataSets
    https://github.com/datasets/covid-19

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# import pandas_profiling # pip install pandas_profiling

"""
data_set = pd.read_csv("covid19-world.csv")
# print(data_set)

india_data_set = data_set[data_set['Country']=='India']
print(india_data_set)

X = india_data_set['Date']
Y = india_data_set['Confirmed']

print("Date")
print(X)
print(len(X))

print("Confirmed")
print(Y)
print(len(Y))

plt.plot(X, Y)
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.show()
"""


data_set = pd.read_csv("covid19-world.csv")


india_data_set = data_set[data_set['Country'] == 'India']
print(india_data_set)


X = india_data_set['Date'].values
print(X)

confirmed_cases = india_data_set['Confirmed'].values


# Lets do Data Pre-Processing, we will convert date into day of year
# make date as a mathematical number

days = []

for date in X:
    # print(date)
    # print(pd.Period(date, freq='D').dayofyear)
    days.append(pd.Period(date, freq='D').dayofyear)

# got numpy version of list :)
days = np.array(days)
print(days)

# plt.plot(days, confirmed_cases)
# plt.xlabel("Days")
# plt.ylabel("Confirmed Cases")
# plt.show()

# We will create ML Model -> RandomForestRegressor -> 10 Trees :)
model = RandomForestRegressor(n_estimators=100)

# Input Filed is 2-D Array :)
days = days[:, np.newaxis]
x_train, x_test , y_train, y_test = train_test_split(days, confirmed_cases, test_size=0.2, random_state=1)

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("Expected Output")
print(y_test)

print("Predicted Output")
print(y_pred)

print(model.score(x_train, y_train))

# print("Predicted Cases on 120th Day")
# cases = model.predict([[120]])
# print(cases)

date_from_user = input("Enter Date in Format yyyy-mm-dd") # 2020-03-23
day = pd.Period(date_from_user, freq='D').dayofyear

cases = model.predict([[day]])
print("Cases on", date_from_user, "may be", cases[0])

# Assignment: COVID Tracker with RandomForest on DataSet from github :)