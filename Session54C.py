from sklearn.datasets import load_iris
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel

X, y = load_iris(return_X_y=True)
print(X.shape)


# Model here is not to do predictions but to work on features
model = ExtraTreesClassifier(n_estimators=50)
model.fit(X, y)
print(model.feature_importances_)

# Selector to select features based on importance
selector = SelectFromModel(model, prefit=True)
X1 = selector.transform(X)
print(X1.shape)
print(X1)

