numbers = [10, 20, 30, 40, 50]
print(numbers, hex(id(numbers)))

numbers = numbers + [60, 70]
print(numbers, hex(id(numbers)))

# Basic Functions on Sequences
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))
print("Len:", len(numbers))
