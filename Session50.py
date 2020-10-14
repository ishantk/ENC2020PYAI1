"""
    Decision Trees - Regression

    CART Algo -> Classification and Regression Trees

    1. As Classifier
       When we have categorical DataSet, i.e. we wish to predict some classes
    2. As Regresser
       When we have Numerical DataSet, we wish to predict some real number


    Decision Tree Algos
    1. Entropy and Information Gain
    2. Gini Index
    3. Chi Square


    1. -> We have seen in classification problems

    2. Gini Index
    -------------
    If we have 2 items from a population and are chosen randomly
    then they must be of same class and probability for this is 1 if population is pure

    Target is: Play Or NotPlay
               Success Or Failure
               Positive Or Negative

    Calculations
    Sum of Square of Probability of Success P(S) and Sum of Square of Probability of Failure P(F)
    P(S)*P(S) + P(F)*P(F)

    Gini for attribute Gender
    Female: P(S) = 0.20
            P(F) = 1-P(S) => 0.80

    (0.20*0.20) + (0.80*0.80)
    => 0.68

    Male:   P(S) = 0.65
            P(F) = 1-P(S) => 0.35

    (0.65*0.65) + (0.35*0.35)
    => 0.55

    Weighted Gini for Attribute Gender
    Weighted Gini = (10/30 * 0.68)  + (20/30 * 0.55)
                  = 0.59

    Gini Impurity => 1 - Gini


    3. Chi Square
    -------------
      Shall find statistical difference between children and parent node


      Nodes     Play    NotPlay     Total   ExpectedPlay    ExpectedNotPlay
      ---------------------------------------------------------------------
      Female    2       8           10      5               5
      Male      13      7           20      10              10


      Deviations
      ----------
      Nodes     DeviationPlay(Play-ExpectedPlay)      DeviationNotPlay(NotPlay - ExpectedNotPlay)
      Female    -3(2-5)                               3(8-5)
      Male      3(13-10)                              -3(10-13)

      Chi Square of Node = sqrt [ ((Actual-Expected) * (Actual-Expected)) /Expected ]

      Chi Square of Node Female for Playing Cricket -> sqrt [ ((2-5) * (2-5)) / 5 ]
                                                    -> sqrt [9/5]
                                                    -> sqrt 1.8
                                                    -> 1.34

      Chi Square of Node Female for Not Playing Cricket -> sqrt [ ((8-5) * (8-5)) / 5 ]
                                                        -> 1.34

      Chi Square of Node Male for Playing Cricket ->    sqrt 9/10  -> 0.95
      Chi Square of Node Male for Not Playing Cricket -> sqrt 9/10 -> 0.95

      Total Chi Square of Attribute Gender -> 1.34 + 1.34 + 0.95 + 0.95
                                           -> 4.5

      Similarly we evaluate for other attributes :)



"""

from sklearn.tree import DecisionTreeRegressor
import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn import tree
import graphviz

# boston_data_set = datasets.load_boston()
# print(boston_data_set)

data_set = pd.read_csv("corona-india-cases.csv")
print(data_set)

X = data_set['Day']
y = data_set['Cases']

# Transform 1-D to 2-D
X = X[:, np.newaxis]
y = y[:, np.newaxis]

model = DecisionTreeRegressor()
model.fit(X, y)

Y = model.predict(X)

print("Actual Cases")
print(y)


print("Predicted Cases")
print(Y)

print("Model Score", model.score(X, Y))

predicted_case = model.predict([[12], [201]])
print(predicted_case)

# plt.figure(figsize=(12, 8))
# plt.scatter(X, y, color="red")
# plt.plot(X, y, color="green")
# plt.xlabel("Days")
# plt.ylabel("Cases")
# plt.show()

# PS: Get the DataSet populated with correct values and implement DTR :)

data = tree.export_graphviz(model, out_file=None)
graph = graphviz.Source(data)
graph.render("COVID-19 CASES TREE")
graph.view()