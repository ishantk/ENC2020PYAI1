"""
    Matplotlib
    Exploring various graphs in matplotlib library
"""
import requests
import json
import matplotlib.pyplot as plt

url = "https://api.covid19india.org/data.json"
response = requests.get(url)

covid_cases = json.loads(response.text)
# print(covid_cases)

cases_time_series = covid_cases['cases_time_series']
print(cases_time_series)

total_confirmed = []
for case in cases_time_series:
    total_confirmed.append(int(case['totalconfirmed']))


print()

print(total_confirmed)
print(len(total_confirmed))

plt.plot(total_confirmed)
plt.show()

# Draw all the state wise graphs for covid cases and compare them :)
# Share the graph in Whatsapp group