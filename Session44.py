"""
    Decision Tree Classifier
    sklearn APIs - Iris Flower Data Set
"""


from sklearn.datasets import load_iris
from sklearn import tree

# loading a built in data set from sklearn
iris_data_set = load_iris()

# print("==IRIS DATA SET==")
# print(iris_data_set)

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

# 1. Create the Model
model = tree.DecisionTreeClassifier()

# 2. Train the Model
# model.fit(iris_data_set.data, iris_data_set.target)
model.fit(FEATURES, LABELS)

# 3. Predictions
known_iris1 = [4.9, 3.1, 1.5, 0.1]      # setosa
known_iris2 = [5.2, 2.7, 3.9, 1.4]      # versicolor

predicted_labels = model.predict([known_iris1, known_iris2])
print(predicted_labels)

print()
print("For {} predicted label is {} and name is {}".format(known_iris1, predicted_labels[0], NAMES[predicted_labels[0]]))
print("For {} predicted label is {} and name is {}".format(known_iris2, predicted_labels[1], NAMES[predicted_labels[1]]))

