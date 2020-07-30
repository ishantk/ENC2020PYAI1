data = [1, 2, 3, 4, 5]
squared_data = []

for i in range(len(data)):
    squared_data.append(data[i]*data[i])
    # print(data[i]*data[i], end=" ")


print("data:", data)
print("squared_data:", squared_data)

# List Comprehension
squared_data1 = [x**2 for x in data]
cube_data1 = [x*x*x for x in data]
print("squared_data1:", squared_data1)
print("cube_data1:", cube_data1)

print()

product_prices = [1245, 3453, 3112, 4532, 2345]
discounted_prices = [0.5*x for x in product_prices]

print("product_prices:", product_prices)
print("discounted_prices:", discounted_prices)

# Assignment: Explore can we use conditions in List Comprehensions
# i.e. we need to give 50%off for the prices > 2500 and 30% off otherwise