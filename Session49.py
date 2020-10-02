"""
    Polynomial Regression
"""

import matplotlib.pyplot as plt
import numpy

X = list(range(1, 21))
print(X)

Y = [100, 90, 80, 60, 60, 55, 60, 65, 75, 70, 71, 73, 75, 76, 78, 79, 90, 100, 120, 125]
print(Y)


model = numpy.poly1d(numpy.polyfit(X, Y, 3))
line = numpy.linspace(1, 20, 100)

print(line)

poly_data = model(line)
print(poly_data)

plt.scatter(X, Y)
plt.plot(line, poly_data)

plt.show()