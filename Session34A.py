"""
 BeautifulSoup ->  Web Scrapping
 Web Scrapping or HTML Parsing
    Extracting meaningful data from the web pages fro the web world
    parses data from the web page with the help of tags and classes in HTML web page

 install -> pip install beautifulsoup4

"""

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# URL to Web Page
url = "https://www.imdb.com/india/top-rated-indian-movies/"

# HTTP Request for getting the web page text as response
response = requests.get(url)

# print("HTML SOURCE")
# print(response.text)

# Create BeautifulSoup Object as HTML PARSER
soup = BeautifulSoup(response.text, "html.parser")

# Extract List of Tags where class is titleColumn
movie_name_tags = soup.find_all("td", class_="titleColumn")
movie_rating_tags = soup.find_all("td", class_="ratingColumn imdbRating")

movie_titles = []
movie_years = []
movie_ratings = []

for tag in movie_name_tags:
    # print(tag)
    # print(tag.text)
    # print(tag.text.strip())

    title = tag.text.strip()
    year = int(title[-5:-1])

    movie_titles.append(title)
    movie_years.append(year)

for tag in movie_rating_tags:
    # print(tag)
    # print(tag.text)
    # print(tag.text.strip())

    rating = float(tag.text.strip())

    movie_ratings.append(rating)


print(movie_titles)
print(movie_years)
print(movie_ratings)

print(len(movie_titles)) # Clean up the title of the movie with String APIs
print(len(movie_years))
print(len(movie_ratings))

plt.barh(movie_years, movie_ratings)
# plt.scatter(movie_years, movie_ratings)
# plt.plot(movie_years, movie_ratings)
plt.show()

# Assignment:
# Explore displaying the data with Seaborn :)
# Compare USA and INDIAN Top Rated Movies on the Seaborn and Matplotlib and share the result of analysis