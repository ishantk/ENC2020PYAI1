"""

    Matplotlib -> For Data Visualization in Graphical Form for better analysis in business
    Reference : https://matplotlib.org/

import matplotlib as lib
print(lib.__version__)

"""

import matplotlib.pyplot as plt
# data = [0, 1, 2, 3, 4, 5]
# plt.plot(data)
# plt.show()

X = list(range(0, 11)) # 0 to 10
Y1 = [n for n in X]
Y2 = [n*n for n in X]
Y3 = [n*n*n for n in X]

print(X)
print(Y1)
print(Y2)
print(Y3)

plt.plot(X, Y1, label="Y1")
plt.plot(X, Y2, label="Y2")
plt.plot(X, Y3, label="Y3")

plt.legend() # in order to show labels on graph

plt.xlabel("X-AXIS")
plt.ylabel("Y-AXIS")

plt.title("Polymomial Graphs")

# plt.xlim(0, 20)
# plt.ylim(0, 20)

plt.grid(True)

plt.savefig("MyGraph")

plt.show()

# Form Previous Session32D Assignment, Plot Temperatures of 3 cities month wise on the graph to have a better understanding how temp flows :)
