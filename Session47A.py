from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

iris_data = load_iris()

FEATURES = iris_data.data

# k value
clusters = 3

# Here we are not training the model with Labels
model = KMeans(n_clusters=clusters)
model.fit(FEATURES)

predicted_results = model.predict(FEATURES)
print(predicted_results)

# 1 setosa
# 2 versicolor
# 3 virginica


"""
    Assignment:
        Compare all the classification models, till now for their metrics
"""