import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://api.covid19india.org/data.json"
response = requests.get(url)

covid_data = json.loads(response.text)
print(covid_data)
print(type(covid_data))

statewise_covid_table = pd.DataFrame(covid_data['statewise'])
print(statewise_covid_table)

print("STATES")
print(statewise_covid_table.state)

print("ACTIVE CASES")
print(statewise_covid_table.active)

# Assignment: Show the graph by fixing the errors :)
# Share the Matplotlib/Seaborn Snippet to draw the data on graph :)
sns.pairplot(data=statewise_covid_table, hue="state")
plt.show()
