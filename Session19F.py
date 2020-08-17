
# below function evaluates a single expression
def area_of_circle(radius = 1.1):
    # area = 3.14 * radius * radius
    # return area
    return 3.14 * radius * radius

print(area_of_circle)
print("Area of Circle is:", area_of_circle())
print("Area of Circle is:", area_of_circle(5))
print("Area of Circle is:", area_of_circle(radius=7))

print()

# Lambdas in Python
# used to express functions with single expression

lRef1 = lambda radius = 1.1: 3.14 * radius * radius
print(lRef1)

print("Area of Circle is:", lRef1())
print("Area of Circle is:", lRef1(5))
print("Area of Circle is:", lRef1(radius=7))

lRef2 = lambda x, y: x**y
lRef3 = lambda x=int(input("Enter X: ")), y=int(input("Enter Y: ")): x**y

print("2 power 5 is:", lRef2(x=2, y=5))
print(lRef3())

lRef4 = lambda x=int(input("Enter X: ")), y=int(input("Enter Y: ")): lRef1(x) + lRef2(x, y)
print("lRef4 result is:", lRef4())