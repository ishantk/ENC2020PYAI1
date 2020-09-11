import pandas as pd
import numpy as np

odd_numbers = np.arange(1, 100, 2)
even_numbers = np.arange(0, 100, 2)

numbers = {"odd_numbers": odd_numbers, "even_numbers": even_numbers}
print(numbers)

table = pd.DataFrame(numbers)
print(table)

print()
print("SUM")
print(table.sum())

print()
print("MAX")
print(table.max())

print()
print("MIN")
print(table.min())

print()
print("STD")
print(table.std()) # explore more about standard deviation