"""
    1. Logistic Regression
    2. Set Up Your Machines for Tensorflow and PyTorch
       Tensorflow: https://www.tensorflow.org/install
       PyCharm: https://pytorch.org/get-started/locally/
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


data_set = pd.read_csv("purchases.csv")
print(data_set)

# sns.countplot("Age", hue="Purchased", data=data_set)
# sns.countplot("Gender", hue="Purchased", data=data_set)
# plt.show()

X = data_set.drop("Gender", axis=1)

Y = data_set["Gender"]

print("X: ")
print(X)

print()

print("Y: ")
print(Y)

# Always train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)

# Create the Model
model = LogisticRegression()

# Train the Model (with the training data)
model.fit(x_train, y_train)

# Make prediction on testing inputs i.e. x_test
predictions = model.predict(x_test)

print("EXPECTED OUTPUTS")
print(y_test)

print()

print("PREDICTED OUTPUTS")
print(predictions)

print()

print("ACCURACY SCORE", accuracy_score(y_test, predictions))

"""
    Classification Reports
    ----------------------
    Displays: precision, recall, f1-score and support
    
    precision: level upto which predictions made by model are precise
    recall: amount upto which model and predict the output
    f1-score and support: amount of data tested for the predictions
    
"""

cls_report = classification_report(y_test, predictions)
print(cls_report)

"""
    Confusion Matrix
    ----------------
    
    Its a table which describes performance of a model
    It contains actual values and predicted values
    From data in confusion matrix we can also compute accuracy scores
    
"""

matrix = confusion_matrix(y_test, predictions)
print(matrix)

# Confusion Matrices are plotted as heatMaps
# Explore here more on HeatMaps :)

matrix_data_set = pd.DataFrame(matrix)
sns.heatmap(matrix_data_set)
plt.show()

# Assignment: Work on the data set purchases.csv
# convert gender male and feamle to 1 and 0 may be and see if score goes up or not :)

