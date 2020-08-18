# requests is not a built in module
# it was installed due to firebase for us :)

import requests
import json

api_key = "YOUR_API_KEY"
url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={}".format(api_key)
response = requests.get(url)
print(response.text)

# JSON Data as String
print(type(response.text))


news_data = json.loads(response.text)
print()
print(news_data)
print(type(news_data))

print(news_data['status'])
print(news_data['totalResults'])

print(news_data['articles'][0])
print(news_data['articles'][0]['author'])
print(news_data['articles'][0]['title'])

print()

print("====Tech Crunch News====")
print()
for i in range(len(news_data['articles'])):
    print(news_data['articles'][i]['title'])
    print(news_data['articles'][i]['author'])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()


# Assignment:
# Perform a Network Request, extract JSON data and parse it to show COVID Cases Statewise
# https://api.covid19india.org/data.json

# Zomato Developer API for Exploration : https://developers.zomato.com/documentation
