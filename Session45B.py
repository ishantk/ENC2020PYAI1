from sklearn.datasets import load_iris
# from sklearn import tree
from sklearn.naive_bayes import GaussianNB

iris_data_set = load_iris()
print(iris_data_set)

FEATURES = iris_data_set.data
LABELS = iris_data_set.target
NAMES = iris_data_set.target_names

# 1. Create the Model
model = GaussianNB()

# 2. Train the Model with Data
model.fit(FEATURES, LABELS)

# 3. Make Predictions
input_data1 = [5.1, 3.5, 1.4, 0.2]
input_data2 = [5.9, 3.0, 5.1, 1.8]

predicted_targets = model.predict([input_data1, input_data2])
print(predicted_targets)

# In the same program implement test_train_split and compute accuracy
# Share, do we have accuracy for IRIS Data Classification more in DecisionTrees or Naive Bayes

