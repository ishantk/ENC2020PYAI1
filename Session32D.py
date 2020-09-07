"""
    numpy Assignment
    mathematical basic data analysis
"""
import numpy as np

array = np.genfromtxt("CityTemps.csv", delimiter=",", dtype=np.float)

columns = ["Year,Month,City1,City2,City3"]

print(columns)
print(array)

print(array[0])
print(array[1])
print(array[1][0])
print(array[5][4])

"""
    Tasks:
    1. display the data in correct format
    2. how many years we have in data set -> 2 i.e. 2014 and 2015
    3. city wise min and max temp
    4. city wise min and max temp alongwith which month
    5. sort the months as per temp for a particular city
    6. Explore COVID-19 data sets on kaggle and use numpy to perform similar use cases as given above

    USE numpy and do not write your algos :)
    If needed explore on google the API required in numpy

"""