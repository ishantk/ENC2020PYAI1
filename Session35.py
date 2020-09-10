"""
    IPL ESPN CrickInfo DataSet Generation
    Web Scrapping with BeautifulSoup
"""

import requests
from bs4 import BeautifulSoup

year = int(input("Enter Team Year [2008 till 2020]: "))
url = "https://www.espncricinfo.com/table/series/8048/season/{}/indian-premier-league".format(year)

# Extract HTML Page Response which is source code in property text
response = requests.get(url)

# HTML SOURCE CODE
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")


print("Parsing Team Names......")
team_name_tags = soup.find_all("h5", class_="header-title label")
team_names = []

for tag in team_name_tags:
    # print(tag.text.strip())
    team_names.append(tag.text.strip())

del team_names[0] # Some IPL Heading
print("{} Teams for IPL {}".format(len(team_names), year))
print(team_names)

print()

print("Parsing Team Data......")
team_data_tags = soup.find_all("td", class_="")
team_data = [] # in this list we will add team data as list, hence this will be a list of list

for i in range(len(team_names)):
    team_data.append([]) # create list of lists :)

# Algo to extract team data as list of lists
i = 0
j = 0

for tag in team_data_tags:
    # print(tag.text.strip())
    text = str(tag.text.strip())
    if text.isdigit():
        team_data[i].append(int(tag.text.strip()))
    else:
        team_data[i].append(float(tag.text.strip()))
    j += 1

    if j % 6 == 0:
        # print("Team {} Data Added".format(i))
        i += 1

print()
print("Team Data")
print(team_data)

print()

print("Parsing Points for Teams......")
team_point_tags = soup.find_all("td", class_="border-right label")
team_points = []

for tag in team_point_tags:
    team_points.append(int(tag.text.strip()))


print()
print("Team Points")
print(team_points)

print("TEAM WISE DETAILS")
print()
print("===========================================")

for i in range(len(team_names)):
    print(team_names[i])
    print(team_data[i])
    print(team_points[i])
    print("===========================================")