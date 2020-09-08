import matplotlib.pyplot as plt

X = list(range(0, 11)) # 0 to 10
Y1 = [n for n in X]
Y2 = [n*n for n in X]
Y3 = [n*n*n for n in X]


# plt.plot(X, Y1, label="Y1")
# plt.plot(X, Y2, label="Y2")
# plt.plot(X, Y3, label="Y3")

# plt.plot(X, Y1, "y", label="Y1")
# plt.plot(X, Y2, "m", label="Y2")
# plt.plot(X, Y3, "black", label="Y3")

# plt.plot(X, Y1, "o", label="Y1")
# plt.plot(X, Y2, "^", label="Y2")
# plt.plot(X, Y3, "D", label="Y3")

plt.plot(X, Y1, ".", label="Y1")
plt.plot(X, Y2, "-.", label="Y2")
plt.plot(X, Y3, ":", label="Y3")

plt.legend() # in order to show labels on graph

plt.xlabel("X-AXIS")
plt.ylabel("Y-AXIS")

plt.title("Polymomial Graphs")


plt.show()