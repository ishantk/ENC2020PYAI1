"""
    CONTROLLER
        1. Operators
            computations
        2. Conditional Flows
            decisions
        3. Iterations
            loops

    CS is all about solving problems:
    Solution to the problem is a logic i.e. algorithm which can be made by above 3 modules
"""

# Operators
# 1. Arithmetic -> +, -, *, %, /, //, **

product_price = 2544
taxes = 0.18

final_price = product_price + product_price * taxes
print("Final Price to Pay \u20b9", final_price)

number = 10
# result = number / 3             # Floating Point Div
result = number // 3              # Integral Div
print("result is:", result)

base = 2
result = base ** 3                # 2 power 3
print("result is:", result)

hash_code = number % 8
print("HashCode is:", hash_code)

# 2. Assignment Operators
# =, +=, -=, *=, /=, //=, **=, %=

# Optimization: We create less storage container
# product_price = product_price + 0.18*product_price
product_price += 0.18*product_price
print(product_price)

i = 0
i+=1
i+=1
i-=1
i*=2
i**=2

print("i is:", i) # 4

