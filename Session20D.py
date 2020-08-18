"""
    We got built in modules in python
    to solve our day to day problems w.r.t. development

    # JSON: Java Script Object

"""
# built in module
import json

employee = {
    "name": "John Watson",
    "phone": "+91 98765 90909",
    "salary": 30000
}

print(employee, type(employee))

# Convert Dictionary to JSON
# JSON is a Dictionary represented as a String
json_data = json.dumps(employee)
print(json_data, type(json_data))

# Convert JSON to Dictionary
dict_data = json.loads(json_data)
print(dict_data, type(dict_data))