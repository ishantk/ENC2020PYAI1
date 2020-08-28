# Regular Expressions
# Search and Filtering of data from the Text using some wild cards

import re

quote = "Search the candle rather than cursing the darkness"
# result = re.match("Search", quote) # 0 - 6
# result = re.match("candle", quote)   # None
# print(result, type(result))

# match matches from beginning in the string

# search will search anywhere in the string
# result = re.search("the", quote)
# print(result)

result = re.findall("the", quote)
print(result)

data = re.split("the", quote)
print(data)

print()

data = re.sub("the", "a", quote)
print(data)

message = "Hello George, Your Order ID 101 has been dispatched. Please Pay 3000"
digits = re.findall("\d+", message)
print(digits)

vehicle_number = "PB10AL2937"
user_email = "john@example.com"

# Assignment: Validate above 2 variables if they are formed correctly

pattern = "\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[Z]{1}[A-Z\d]{1}"
# Try Testing the above pattern if its a correct GST number or not

quote = "Work Hard And Get Luckier"
# result = re.findall(".", quote) # -> alphabets with spaces
# result = re.findall("\w", quote)  # -> alphabet without spaces
result = re.findall("\w+", quote)  # -> words
# result = re.findall("\w*", quote)  # -> words alongwith spaces
print(result)
print(len(result))


