from sklearn.neighbors import KNeighborsClassifier
# from sklearn.neighbors import KNeighborsRegressor

# Vehicle Classification | Weight and Engine
training_data = [
    [100, 100],
    [150, 110],
    [180, 150],
    [200, 180],
    [800, 1000],
    [1000, 1200],
    [1200, 1300],
    [1500, 1500],
]

# Labels
bike = 0
car = 1

labels = ["Bike", "Car"]

training_labels = [bike, bike, bike, bike, car, car, car, car]

# k is 3 for us which is 3 nearest neighbours
model = KNeighborsClassifier(n_neighbors=3)
model.fit(training_data, training_labels)

sample_input = [250, 300]
predicted_label = model.predict([sample_input])
print(predicted_label)
print(labels[predicted_label[0]])
