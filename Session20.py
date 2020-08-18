"""
    Generators
    Functions
    Built IN Modules
"""

def hello():
    print("This is hello")
    return "Hello"
    return "Heya" # will not be executed | Not Reachable Code


print(hello)        # HashCode
result = hello()
print(result)

def hello_again():
    print("This is hello")
    yield "Hello"
    yield "Hi"
    yield "Heya"
    yield "Thanks"

print(hello_again) # HashCode

# Function can either return or yield
result = hello_again()
print(result)

# If a function has a yield statement, it will return a generator
# In above code snippet, result is a generator

print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result)) # StopIteration Error

# Queue Operation -> First In and First Out