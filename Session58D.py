import requests
from bs4 import BeautifulSoup

from nltk.corpus import stopwords
from nltk import FreqDist

url = "https://about.google/?utm_source=google-IN&utm_medium=referral&utm_campaign=hp-footer&fg=1"
response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
text = soup.text

tokens = [token for token in text.split()]
print(tokens)

# Text Pre Processing
tokens_without_stop_words = tokens[:] # Copy the token list data from 0 to last index in tokens_without_stop_words

for token in tokens:

    if token in stopwords.words("english"):
        tokens_without_stop_words.remove(token)

print(tokens_without_stop_words)

frequency = FreqDist(tokens_without_stop_words)
frequency.plot(20)

# Assignment: Take the textual content of PM or President's Speech from the web and examine what they wish to say in their speech