# write the main or don't write the main function execution stack remains the same :)

print("main started")
# creation statement
number = 10

# creation statement
quote = "search the candle, rather than cursing the darkness"

# creation statement
def add(num1, num2):
    print("add started")
    sum = num1 + num2
    print("sum is:", sum)
    print("add finished")

# execution statement
add(10, 20)

# printing statement
print("number is:", number)
print("quote is:", quote)


print("main finished")