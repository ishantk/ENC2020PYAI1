from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# 1. Create the Data Set
X = [1, 2, 3, 4, 5]  # Independent Input Variable
Y = [2, 4, 5, 4, 5]  # Dependent Output Variable

# 2. LinearRegression is 1 line of code :)
data = stats.linregress(X, Y)

print(data, type(data))

print("Slope of Line is:", data[0])
print("Interceptor is:", data[1])

print("Equation of Line is: Y = {} + {} X".format(data[1], data[0]))

# We are kind of creating a Range :)
max_x = np.max(X) + 10
min_y = np.min(Y) - 10

print(max_x)
print(min_y)

# Lets Create some Data POints for Linear Regression. Instead of just 5 points, we will have somewhere 100
x = np.linspace(min_y, max_x, 100)
y = data[1] + data[0] * x

print(x)
print(y)

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True)
plt.plot(x, y, color="red", label="Regression Line")
plt.scatter(X, Y, color="blue", label="Data Points")
plt.legend()
plt.show()


# Assignment
# Apply Linear Regression on IPL Data Set
# You can choose Year as X and Points as Y for your favourite Team
# Draw the Regression Line on the Graph
# Use only sklearn LinearRegression API to solve this problem with r2 core :)
