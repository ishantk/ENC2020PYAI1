"""
    Support Vector Machines for Classification
"""

"""
    Vehicle Classification Model

   [feature1    feature2    label]
    weight      engine      vehicle | 0: bike and 1: car
1.  200         100         0
2.  220         150         0
3.  250         200         0
4.  280         250         0
5.  300         280         0

6.  800         800         1
7.  1000        1100        1
8.  1200        1250        1
9.  1500        1450        1
10. 1800        1700        1

"""

# Support Vector Machine API for classification
from sklearn import svm

# 1. Create the DatSet (Features and Labels)
# This is input X
data_set_features = [
    [200, 100],
    [220, 150],
    [250, 200],
    [280, 250],
    [300, 280],
    [800, 800],
    [1000, 1100],
    [1200, 1250],
    [1500, 1450],
    [1800, 1700],
]

#         0       1
labels = ["BIKE", "CAR"]

# This is output Y
data_set_labels = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

# 2. Create ML Model
# Above data set is known and accurate as per the feature label modeling
model = svm.SVC()

# 3. Feed Features and Labels as Data to ML Model
# 4. Train the Model
# both feeding data and training the model is done with fit function :)
model.fit(data_set_features, data_set_labels)

# 5. Make Predictions
known_observation1 = [220, 150]
unknown_observation1 = [350, 280]

known_observation2 = [1500, 1450]
unknown_observation2 = [1780, 1280]

result = model.predict([known_observation1, unknown_observation1, known_observation2, unknown_observation2])
print(result)
# print(type(result))

print("For Known Observation1:", known_observation1)
print(labels[result[0]])

print("For UnKnown Observation1:", unknown_observation1)
print(labels[result[1]])

print("For Known Observation2:", known_observation2)
print(labels[result[2]])

print("For UnKnown Observation2:", unknown_observation2)
print(labels[result[3]])

