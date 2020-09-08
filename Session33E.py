import matplotlib.pyplot as plt

"""
ages = [21, 22, 23, 4, 5, 6, 77, 8, 21, 10, 31, 32, 66, 54, 90]
bins = 10
plt.hist(ages, bins)
plt.show()
"""

"""
languages = ["python", "java", "c++", "dart", "javascript"]
jobs = [70, 80, 90, 40, 110]

plt.barh(languages, jobs)
plt.show()
"""

years = [2016, 2017, 2018, 2019, 2020]
jobs_in_java = [90, 80, 90, 40, 110]
jobs_in_python = [80, 80, 90, 110, 220]

plt.bar(years, jobs_in_java, 0.60, color="c", label="Java")
plt.bar(years, jobs_in_python, 0.30, color="g", label="Python")

plt.legend() # Please Explore different positions of Legend on Graph
plt.show()
