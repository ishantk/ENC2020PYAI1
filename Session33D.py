import requests
import json
import matplotlib.pyplot as plt

# Write Algo for fetching statewise active cases for dictionary

url = "https://api.covid19india.org/data.json"
response = requests.get(url)

covid_cases = json.loads(response.text)

statewise = covid_cases['statewise']
print(statewise)

cases = {}
for case in statewise:
    cases[case['state']] = int(case['active'])

print(cases)

for i, key in enumerate(cases):
    plt.barh(key, cases[key])

plt.xlabel("State")
plt.ylabel("Active Cases")

plt.title("India COVID Active Cases")

plt.show()


