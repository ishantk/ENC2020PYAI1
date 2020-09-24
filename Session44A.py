"""
    Decision Tree Classifier
    sklearn APIs - Iris Flower Data Set
"""


from sklearn.datasets import load_iris
from sklearn import tree
from sklearn import metrics     # Accuracy Scores
from sklearn.model_selection import train_test_split # Break the DataSet randomly into testing and training

# loading a built in data set from sklearn
iris_data_set = load_iris()

print("FEATURES")
FEATURES = iris_data_set.data
print(FEATURES)

print()

print("LABELS")
LABELS = iris_data_set.target
print(LABELS)

print()

print("LABELS WITH NAMES")
NAMES = iris_data_set.target_names
print(NAMES)

# 1. Split the DataSet in 2 parts
# 1. Training Data | 70
# 2. Testing Data  | 30

x_train, x_test, y_train, y_test = train_test_split(FEATURES, LABELS, test_size=0.3, random_state=1)

print("SPLIT DATA SET")

print(len(FEATURES), len(LABELS))

print()

print(x_train)
print(y_train)
print(len(x_train), len(y_train))

print()
print(x_test)
print(y_test)
print(len(x_test), len(y_test))


# 2. Create the Model
model = tree.DecisionTreeClassifier()

# 3. Train the Model with Split Data Set
model.fit(x_train, y_train)

# 4. Check for Accuracy by making predictions on test data set
y_pred = model.predict(x_test)
accuracy = metrics.accuracy_score(y_test, y_pred) # original and predicted y
print("ACCURACY SCORE:", accuracy)
print()

# 4. Predictions
known_iris1 = [4.9, 3.1, 1.5, 0.1]      # setosa
known_iris2 = [5.2, 2.7, 3.9, 1.4]      # versicolor

predicted_labels = model.predict([known_iris1, known_iris2])
print(predicted_labels)

print()
print("For {} predicted label is {} and name is {}".format(known_iris1, predicted_labels[0], NAMES[predicted_labels[0]]))
print("For {} predicted label is {} and name is {}".format(known_iris2, predicted_labels[1], NAMES[predicted_labels[1]]))

# Assignment:
# Obtain the DataSet for COVID-19 Positive and Negative Cases with various attributes from kaggle
# Run DecisionTreeClassifier to examine a case to be positive or negative
# https://www.kaggle.com/search?q=covid+patients

