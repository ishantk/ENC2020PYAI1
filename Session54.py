"""
    Feature Extraction / Dimensioanlity Reduction
"""

# Variance Threshold
# It uses variance and removes some low variance features
# Algo shall work only on Inputs and not the outputs
# Here, we are not reducing the rows i.e. records remain same
# BUT, Feature or Columns are Reduced

from sklearn.feature_selection import VarianceThreshold

# X = [
#      [0, 2, 0, 3],
#      [0, 1, 4, 3],
#      [0, 1, 1, 3],
# ]

X = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    [0, 1, 1],
    [0, 1, 0],
    [0, 1, 1]
]

print("X BEFORE")
print(X)

# selector = VarianceThreshold()
# Var[X] = p(1 - p)
selector = VarianceThreshold(0.8 * (1 - 0.8))
X = selector.fit_transform(X)


print("X AFTER")
print(X)

