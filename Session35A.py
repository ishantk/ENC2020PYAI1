# OOPS for Team Data Web Scrapping

import requests
from bs4 import BeautifulSoup

# Object Representation for IPL Team
class Team:

    def __init__(self, year, name, matches, won, lost, tied, abandoned, points, nrr):
        self.year = year
        self.name = name
        self.matches = matches
        self.won = won
        self.lost = lost
        self.tied = tied
        self.abandoned = abandoned
        self.points = points
        self.nrr = nrr

    def __str__(self):
        return "{},{},{},{},{},{},{},{},{}\n"\
            .format(self.year, self.name, self.matches, self.won, self.lost, self.tied, self.abandoned, self.points, self.nrr)

class FetchTeamDataTask:

    def fetch_data(self, year):
        url = "https://www.espncricinfo.com/table/series/8048/season/{}/indian-premier-league".format(year)

        # Extract HTML Page Response which is source code in property text
        response = requests.get(url)

        # HTML SOURCE CODE
        # print(response.text)

        soup = BeautifulSoup(response.text, "html.parser")

        team_name_tags = soup.find_all("h5", class_="header-title label")
        team_names = []

        for tag in team_name_tags:
            # print(tag.text.strip())
            team_names.append(tag.text.strip())

        del team_names[0]  # Some IPL Heading

        print()

        team_data_tags = soup.find_all("td", class_="")
        team_data = []  # in this list we will add team data as list, hence this will be a list of list

        for i in range(len(team_names)):
            team_data.append([])  # create list of lists :)

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

        team_point_tags = soup.find_all("td", class_="border-right label")
        team_points = []

        for tag in team_point_tags:
            team_points.append(int(tag.text.strip()))

        teams = []

        for i in range(len(team_names)):

            team = Team(
                year=year,
                name=team_names[i],
                matches=team_data[i][0],
                won=team_data[i][1],
                lost=team_data[i][2],
                tied=team_data[i][3],
                abandoned=team_data[i][4],
                nrr=team_data[i][5],
                points=team_points[i]
            )

            teams.append(team)

        return teams

class DataSetGenerator:

    def generate_data_set(self, file_name, data):
        file = open(file_name, 'a')
        for line in data:
            file.write(str(line))

        print("DataSetGenerated...")

def main():

    year = int(input("Enter Team Year [2008 till 2020]: "))

    fetch_task = FetchTeamDataTask()
    teams = fetch_task.fetch_data(year)

    for team in teams:
        print(team)

    ds_gen = DataSetGenerator()
    ds_gen.generate_data_set(file_name="IPL-DATA-SET-{}.csv".format(year), data=teams)


if __name__ == '__main__':
    main()

# Assignment: Create DataSet by Web Scrapping ICMR website for COVID-19 in INDIA