"""
    Feature Extraction
    Dictionary Vectorizer -> Converts the Dictionary into Vectors
"""

from sklearn.feature_extraction import DictVectorizer

weather = [
    {'city': 'Delhi', 'temperature': 33.0},
    {'city': 'Mumbai', 'temperature': 41.0},
    {'city': 'Ludhiana', 'temperature': 44.0},
    {'city': 'Chandigarh', 'temperature': 40.0},
    {'city': 'Pune', 'temperature': 36.0}
]

print(weather)

vectorizer = DictVectorizer()
array = vectorizer.fit_transform(weather).toarray()

print(array)

feature_names = vectorizer.get_feature_names()
print(feature_names)