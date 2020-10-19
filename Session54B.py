"""
    SelectKBest - Feature Selection
    Select the K Best Features from the DataSet with Highest Scores :)
"""

from sklearn.datasets import load_iris
from sklearn.datasets import load_digits
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# X in upper case means the Input
# y in lower case is the actual Output

# X, y = load_digits(return_X_y=True)
# print(X.shape)
#
# X_new = SelectKBest(chi2, k=20).fit_transform(X, y)
# print(X_new.shape)

X, y = load_iris(return_X_y=True)
print(X)
print(y)

print(X.shape)

selector = SelectKBest(chi2, k=3)
X_new = selector.fit_transform(X, y)

print(X_new.shape)