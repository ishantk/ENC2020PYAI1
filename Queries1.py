"""
import requests

url = "https://developers.zomato.com/api/v2.1/categories"
headers = {"user-key": "YOUR_KEY_HERE"}

# For Headers
response = requests.get(url, headers=headers)
print(response.text)

# For POST requests
# data = {"name": "John", "age":30}
# response = requests.post(url, data=data)
# print(response.text)
"""

import copy

class Product:

    def __init__(self):
        self.pid = 101                    # int
        self.name = "iPhoneX"             # string
        self.memory_specs = [4, 8, 128]   # list

    def show_product(self):
        print(self.pid, self.name, self.memory_specs)


    """
    def __copy__(self):
        cls = self.__class__ # obtain reference of class
        result = cls.__new__(cls) # use __new__ to create a new object of the class
        result.__dict__.update(self.__dict__)
        return result
    """

    """
    def __deepcopy__(self, memodict):
        cls = self.__class__  # obtain reference of class
        result = cls.__new__(cls) # use __new__ to create a new object of the class
        memodict[id(self)] = result

        for k, v in self.__dict__.items():
            setattr(result, k, copy.deepcopy(v))

        return result
    """

product1 = Product()
product1.name = "Apple iPhone X"
product1.show_product()

# product2 = copy.copy(product1)
product2 = copy.deepcopy(product1)
product2.show_product()

print(hex(id(product1)))
print(hex(id(product2)))

# Change data in product2 memory_specs
product2.memory_specs[2] = 256

product1.show_product()
product2.show_product()




