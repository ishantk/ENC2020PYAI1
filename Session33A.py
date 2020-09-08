import numpy as np
import matplotlib.pyplot as plt

# Histogram
# https://www.mathsisfun.com/data/histograms.html

X = np.random.randn(50)
print(X)

plt.hist(X, 20)
plt.show()